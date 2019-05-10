<template>
<div class="container-card">
  <form>
    <div class="text-header">欢迎来到挣闲钱</div>
    <hr>
    <div class="container-input">
      <span>账号：</span>
      <input type="text" v-model="account" placeholder="账号">
    </div>
    <div class="container-input">
      <span>密码：</span>
      <input type="password" v-model="password" placeholder="密码">
    </div>
    <div id="warning">{{warning}}</div>
    <div class="button-sign" @click="signupClick">注册</div>
    <div class="button-sign" @click="signinClick">登录</div>
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
      warning: null
    }
  },
  methods: {
    signupClick: function () {
      this.$router.push({ path: '/signup' })
    },
    signinClick: function () {
      if (this.isNULL(this.account)) {
        this.warning = '请输入账号！'
      } else if (this.isNULL(this.password)) {
        this.warning = '请输入密码！'
      } else {
        this.warning = ''
        //
        axios
          .post('http://localhost:8081/users/signin', {
            account: this.account,
            password: this.password
          })
          .then((response) => {
            console.log(response)
          })
          .catch((error) => alert(error))
      }
    },
    isNULL: function (data) {
      if (data == null || data.length === 0) {
        return true
      }
      return false
    },
    isValidId: function (data) {
      if (data.match(/^([0-9]*)$/) && data.length === 8) {
        return true
      }
      return true
    }
  }
}
</script>

<style scoped>
.container-card {
  margin-left: calc(50vw - 300px);
  margin-top: calc(50vh - 230px);
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
  margin-left: 70px;
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

#warning {
  text-align: left;
  color: #f00;
  margin-top: 20px;
  margin-left: 170px;
  height: 20px;
}

.button-sign {
  margin: auto;
  margin-top: 15px;
  padding-top: 5px;
  width: 230px;
  height: 35px;
  color: white;
  background-color: var(--cyan);
  font-size: 19px;
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
  /* Opera */
}

.button-sign:hover {
  background-color: var(--cyan-hover);
  cursor: pointer;
}
</style>
