import Vue from 'vue'
import Router from 'vue-router'

import Signin from './components/Signin.vue'
import Signup from './components/Signup.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/', name: 'signin', component: Signin
    },
    {
      path: '/signin', name: 'signin', component: Signin
    },
    {
      path: '/signup', name: 'signup', component: Signup
    }
  ]
})
