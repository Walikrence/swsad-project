import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// ant-design
import 'ant-design-vue/dist/antd.css'
import {Button, Divider, Input, Checkbox, Icon, Radio, InputNumber, List, Card, Progress, Affix} from 'ant-design-vue'
// axios config
// import axios from 'axios'
// axios.defaults.baseURL = 'http://localhost:8000'

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

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
