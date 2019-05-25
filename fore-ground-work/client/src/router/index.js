import Vue from 'vue'
import Router from 'vue-router'

import Guide from '@/components/Guide.vue'
import Signin from '@/components/Signin.vue'
import Signup from '@/components/Signup.vue'
import Home from '@/components/Home.vue'
import NewQn from '@/components/NewQn.vue'
import QnList from '@/components/QnList.vue'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', redirect: '/guide' },
    {
      path: '/guide',
      name: 'guide',
      component: Guide,
      redirect: '/guide/home',
      children: [
        { path: 'home', name: 'home', component: Home },
        { path: 'newQn', name: 'newQn', component: NewQn },
        { path: 'qnList', name: 'qnList', component: QnList }
      ]
    },
    { path: '/signin', name: 'signin', component: Signin },
    { path: '/signup', name: 'signup', component: Signup }
  ]
})
