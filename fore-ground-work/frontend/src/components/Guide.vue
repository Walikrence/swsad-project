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
      <!-- not login -->
      <div v-if="userInfo==null">
        <a-button type="primary" class="button-sign" @click="jumpToSignin">登录</a-button>
        <a-button type="primary" class="button-sign" @click="signoutClick">登出</a-button>
      </div>
      <!-- already login -->
      <div v-else class="header-account-avatar">
        <a-dropdown :trigger="['click']">
          <a class="ant-dropdown-link" href="#">
            <img class="header-account-avatar-img" src="@/assets/avatar.jpg" />
          </a>
          <a-menu slot="overlay" class="header-account-menu">
            <a-menu-item key="0">账户详情</a-menu-item>
            <a-menu-divider />
            <a-menu-item key="3" @click="signoutClick">退出登录</a-menu-item>
          </a-menu>
        </a-dropdown>
        <span class="header-account-username">{{userInfo}}</span>
      </div>
    </div>
  </div>
  <div class="container-guide-display">
    <router-view></router-view>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import { mapState, mapMutations } from 'vuex'

export default {
  data: function () {
    return {
    }
  },
  computed: {
    ...mapState(['userInfo'])
  },
  methods: {
    ...mapMutations(['setUserInfo']),
    homeClick: function () {
      this.$router.push({ path: '/guide' })
    },
    jumpToSignin: function () {
      this.$router.push({ path: '/signin' })
    },
    signoutClick: function () {
      axios
        .post('/users/signout/', {
          username: this.userInfo
        })
        .then((response) => {
          var resp = response.data
          console.log(resp)
          if (resp.code === 1) { // not login yet
            this.$message.warning(resp.message)
            this.$router.push({ path: '/signin' })
            return
          }
          if (resp.code === 2) { // signout success
            this.setUserInfo(null)
            this.$router.push({ path: '/signin' })
          }
        })
        .catch((error) => this.$message.error(error))
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
  margin-left: 5px;
  width: 100px;
  height: 30px;
}

.header-account-avatar {
  margin-top: 14px;
  font-size: 15px;
  line-height: 32px;
  vertical-align: text-bottom;
}

.header-account-avatar-img {
  width: 32px;
  height: 32px;
  border-radius: 5px;
}

.header-account-menu {
  margin-top: 10px;
  width: 120px;
  text-align: center;
}

.header-account-username {
  margin-left: 15px;
}

.container-guide-display {
  margin-top: 60px;
  height: calc(100vh - 60px);
  overflow: auto;
  background-color: var(--grey-background);
}
</style>
