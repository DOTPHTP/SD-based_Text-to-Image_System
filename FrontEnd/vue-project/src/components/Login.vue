<template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div>
        <label for="username">Username:</label>
        <input type="text" v-model="username" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '',
    };
  },
  methods: {
    login() {
        // 假设验证逻辑
        if (this.username === 'user' && this.password === 'pass') {
        localStorage.setItem('isAuthenticated', 'true'); // 设置登录状态
        this.$router.push('/app'); // 登录成功后重定向到应用界面
        } else {
        this.errorMessage = 'Invalid credentials';
        }
    },
    }

};
</script>

<style scoped>
.login {
  max-width: 400px;
  margin: auto;
}
</style>
