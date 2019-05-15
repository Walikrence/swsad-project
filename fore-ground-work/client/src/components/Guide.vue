<template>
<div>
  <header>
    <div class="header-nav">
      <div class="header-title">挣闲钱</div>
      <div class="header-nav-cell">创建问卷</div>
      <div class="header-nav-cell">我的问卷</div>
      <div class="header-nav-cell">帮助中心</div>
    </div>
    <div class="header-account">
      <div class="button-sign" @click="jumpToSignin">登录</div>
    </div>
  </header>
  <router-view></router-view>
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
    jumpToSignin: function () {
      this.$router.push({ path: '/signin' })
    }
  }
}
</script>

<style scoped>
header {
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

.header-nav-cell {
  display: inline-block;
  width: 100px;
  line-height: 60px;
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
  padding-top: 5px;
  width: 100px;
  height: 30px;
  color: white;
  background-color: var(--cyan);
  font-size: 16px;
  font-weight: bold;
  border: none;
  /*radius*/
  border-radius: 3px;
  transition: 0.3s;
  -moz-transition: 0.3s;
  /* Firefox 4 */
  -webkit-transition: 0.3s;
  /* Safari 和 Chrome */
  -o-transition: 0.3s;
}
</style>
