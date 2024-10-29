from flask import Flask, request, jsonify, send_file
from diffusers import StableDiffusionPipeline
from datetime import datetime
import torch
import os


app = Flask(__name__)

# 加载模型
pipe = StableDiffusionPipeline.from_single_file(
    "F:\\2024\\coding\\safetensors\\CheckpointYesmix_v50.safetensors",
    torch_dtype=torch.float16,
    local_files_only=True
)

# 设置 GPU 加速（如果有 GPU）
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipe.to(device)

@app.route('/generate', methods=['POST'])
def generate_image():
    # 获取请求中的数据
    data = request.json
    prompt = data.get("prompt", "a beautiful cool girl")
    num_inference_steps = data.get("num_inference_steps", 50)
    width = data.get("width", 512)
    height = data.get("height", 512)

    # 生成图像
    image = pipe(prompt, num_inference_steps=num_inference_steps, width=width, height=height).images[0]

    # 获取当前日期和时间
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    count = len(os.listdir("image")) + 1  # 计算当前目录下已有的图像数量
    image_path = f"image/{timestamp}_{count}.png"

    # 保存图像并返回路径
    image.save(image_path)
    
    return send_file(image_path, mimetype='image/png')

if __name__ == '__main__':
    # 创建保存图像的目录（如果不存在）
    if not os.path.exists("image"):
        os.makedirs("image")
    app.run(host='0.0.0.0', port=5000)
