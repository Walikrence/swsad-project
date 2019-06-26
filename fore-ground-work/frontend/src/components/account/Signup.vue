<template>
<div class="container-card">
  <form>
    <div class="text-header">注册</div>
    <a-divider />
    <div class="container-input">
      <span>账号：</span>
      <input type="text" v-model="account" placeholder="账号">
    </div>
    <div class="container-input">
      <span>密码：</span>
      <input type="password" v-model="password" placeholder="密码">
    </div>
    <div class="container-input">
      <span>确认密码：</span>
      <input type="password" v-model="rpassword" placeholder="确认密码">
    </div>
    <div class="container-input">
      <span>邮箱：</span>
      <input type="text" v-model="email" placeholder="邮箱">
    </div>
    <a-button type="primary" class="button-sign" @click="signupClick">注册</a-button>
    <a-button type="primary" class="button-sign" @click="signinClick">登录</a-button>
  </form>
</div>
</template>

<script>
import axios from 'axios'

export default {
  data: function () {
    return {
      account: null,
      password: null,
      rpassword: null,
      email: null
    }
  },
  methods: {
    signinClick: function () {
      this.$router.push({ path: '/signin' })
    },
    signupClick: function () {
      if (this.isNULL(this.account)) {
        this.$message.warning('请填写账号')
        return
      }
      if (!this.isValidId(this.account)) {
        this.$message.warning('账号格式不正确，请输入6-20个字符')
        return
      }
      if (this.isNULL(this.password)) {
        this.$message.warning('请填写密码')
        return
      }
      if (!this.isValidId(this.password)) {
        this.$message.warning('密码格式不正确，请输入6-20个字符')
        return
      }
      if (this.isNULL(this.rpassword)) {
        this.$message.warning('请重复密码')
        return
      }
      if (this.password !== this.rpassword) {
        this.$message.warning('两次输入的密码不一致')
        return
      }
      if (this.isNULL(this.email)) {
        this.$message.warning('请填写邮箱')
        return
      }
      if (!this.isValidEmail(this.email)) {
        this.$message.warning('邮箱格式不正确，请输入小于20个字符')
        return
      }
      //
      axios
        .post('/api/users/register/', {
          username: this.account,
          password: this.password,
          email: this.email
        })
        .then((response) => {
          var resp = response.data
          console.log(resp)
          if (resp.code === 1) { // username already taken
            this.$message.warning(resp.message)
            return
          }
          if (resp.code === 2) { // success
            this.$message.success('注册成功！')
            this.$router.push({ path: '/signin' })
          }
        })
        .catch((error) => this.$message.error(error))
    },
    isNULL: function (data) {
      if (data == null || data.length === 0) {
        return true
      }
      return false
    },
    isValidId: function (data) {
      if (data.length >= 6 && data.length <= 20) {
        return true
      }
      return false
    },
    isValidEmail: function (data) {
      if (data.length > 0 && data.length <= 20) {
        return true
      }
      return false
    }
  }
}
</script>

<style scoped>
.container-card {
  margin-left: calc(50vw - 300px);
  margin-top: 100px;
  width: 600px;
  text-align: center;
  padding: 30px;
  background-color: white;
  /*radius*/
  border-radius: 3px;
  /*shadow*/
  box-shadow: -1px 1px 5px var(--grey-shadow);
}

.text-header {
  margin: auto;
  font-size: 35px;
  font-weight: 700;
}

.container-input {
  text-align: left;
  margin-top: 20px;
  font-size: 16px;
}

.container-input span {
  display: inline-block;
  font-weight: bold;
  width: 80px;
  margin-left: 75px;
  text-align: right;
}

.container-input input {
  height: 40px;
  width: 230px;
  padding: 0 20px 0 25px;
  background: #f0f0f0;
  border: none;
  border-radius: 3px;
  box-shadow: none;
  transition: all 0.3s ease 0s;
}

.container-input input:focus {
  background: #e0e0e0;
  box-shadow: none;
  outline: 0 none;
}

.button-sign {
  display: block;
  margin: auto;
  margin-top: 15px;
  width: 230px;
  height: 35px;
  font-size: 19px;
  font-weight: bold;
}
</style>
