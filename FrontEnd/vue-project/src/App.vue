<script setup></script>

<template>
  <div id="app">
    <router-view></router-view>

    <div class="router-links">
      <router-link to="/">Home</router-link>
      <br />
      <router-link to="/login">Login</router-link>
      <!-- 添加登录链接 -->
      <br />
      <router-link to="/app">App</router-link>
    </div>
  </div>
</template>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* 确保应用至少占满整个视口高度 */
}

.router-links {
  margin-top: auto; /* 将链接推到底部 */
}
</style>
