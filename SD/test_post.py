import requests

# 替换为你的服务器地址
url = 'http://172.30.207.108:5000/generate'
data = {
    "prompt": "a beautiful cool girl",
    "num_inference_steps": 50,
    "width": 512,
    "height": 512
}

# 发送 POST 请求
response = requests.post(url, json=data)

# 检查响应状态
if response.status_code == 200:
    with open('generated_image.png', 'wb') as f:
        f.write(response.content)
    print("图像已保存为 generated_image.png")
else:
    print("请求失败，状态码:", response.status_code)
