import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
/* ant-design */
import 'ant-design-vue/dist/antd.css'
import {Button, Divider, Input, Checkbox, Icon, Radio, InputNumber} from 'ant-design-vue'

Vue.use(Button)
Vue.use(Divider)
Vue.use(Input)
Vue.use(Checkbox)
Vue.use(Icon)
Vue.use(Radio)
Vue.use(InputNumber)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
