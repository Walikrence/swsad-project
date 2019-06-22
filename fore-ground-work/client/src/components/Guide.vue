<template>
<div>
  <div class="header-container">
    <div class="header-nav">
      <div class="header-title" @click="homeClick">挣闲钱</div>
      <div class="header-nav-cell" @click="qnClick">问卷系统</div>
      <div class="header-nav-cell" @click="taskClick">小任务系统</div>
      <div class="header-nav-cell">社区系统</div>
    </div>
    <div class="header-account">
      <a-button type="primary" class="button-sign" @click="jumpToSignin">登录</a-button>
    </div>
  </div>
  <div class="container-guide-display">
    <router-view></router-view>
  </div>
</div>
</template>

<script>
// import axios from 'axios'

export default {
  data: function () {
    return {
    }
  },
  methods: {
    homeClick: function () {
      this.$router.push({ path: '/guide' })
    },
    jumpToSignin: function () {
      this.$router.push({ path: '/signin' })
    },
    qnClick: function () {
      this.$router.push({ path: '/guide/qnHome' })
    },
    taskClick: function () {
      this.$router.push({ path: '/guide/taskHome' })
    }
  }
}
</script>

<style scoped>
.header-container {
  position: fixed;
  width: 100%;
  height: 60px;
  top: 0;
  left: 0;
  background-color: white;
  /*shadow*/
  box-shadow: 1px 1px 5px var(--grey-shadow);
  z-index: 100;
}

.header-nav {
  display: block;
  margin: auto;
  width: 1024px;
  font-size: 17px;
}

.header-title {
  display: inline-block;
  width: 160px;
  line-height: 60px;
  font-size: 24px;
  font-weight: bolder;
  color: var(--cyan);
}

.header-title:hover {
  cursor: pointer;
}

.header-nav-cell {
  display: inline-block;
  width: 120px;
  line-height: 60px;
}

.header-nav-cell:hover {
  cursor: pointer;
}

.header-account {
  display: block;
  position: absolute;
  top: 0;
  right: 120px;
  font-size: 13px;
  text-align: center;
}

.button-sign {
  margin-top: 15px;
  width: 100px;
  height: 30px;
}

.container-guide-display {
  margin-top: 60px;
  height: calc(100vh - 60px);
  overflow: auto;
}
</style>
