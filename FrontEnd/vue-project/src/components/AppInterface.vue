<template>
  <div class="app-interface">
    <div class="header">
      SD-Project
    </div>
    <div class="body">
      <div class="sidebar">
        sidebar
      </div>
      <div class="container">
      
      </div>
    </div>
  </div>
</template>

<style scoped>
.app-interface {
  padding: 0px;
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.container {
  display: flex;
}

.header {
  background: #f8fafc;
  height: 64px;
  font-size: 32px;
  display: flex;
  align-items: center;
  font-weight: 700;
  padding: 20px;
}

.body {
  display: flex;
  flex: 1;
}

.sidebar {
  width: 300px;
  background: royalblue;
  box-sizing: border-box;
  flex-shrink: 0;
}
</style>
