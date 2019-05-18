import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
/* ant-design */
/* import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.less'
import Button from "ant-design-vue/lib/button";

Vue.use(Antd)

Vue.component(Button.name, Button) */

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
