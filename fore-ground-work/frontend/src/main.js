import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// ant-design
import 'ant-design-vue/dist/antd.less'
import { Button, Divider, Input, Checkbox, Icon, Radio, InputNumber, List, Card,
  Progress, Affix, Avatar, Dropdown, Menu, message, Carousel, Modal } from 'ant-design-vue'
// axios config
// import axios from 'axios'
// axios.defaults.baseURL = 'http://localhost:8080'

Vue.prototype.$message = message
// Vue.prototype.$notification = notification;
// Vue.prototype.$info = Modal.info;
// Vue.prototype.$success = Modal.success;
// Vue.prototype.$error = Modal.error;
// Vue.prototype.$warning = Modal.warning;
Vue.prototype.$confirm = Modal.confirm

Vue.use(Button)
Vue.use(Divider)
Vue.use(Input)
Vue.use(Checkbox)
Vue.use(Icon)
Vue.use(Radio)
Vue.use(InputNumber)
Vue.use(List)
Vue.use(Card)
Vue.use(Progress)
Vue.use(Affix)
Vue.use(Avatar)
Vue.use(Dropdown)
Vue.use(Menu)
Vue.use(message)
Vue.use(Carousel)
Vue.use(Modal)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

router.beforeEach((to, from, next) => {
  if (to.path !== '/signin' && to.path !== '/signup') { // if jumping to ~sign page, check if login
    if (store.state.userInfo == null) {
      next('/signin')
    }
  }
  next()
})
