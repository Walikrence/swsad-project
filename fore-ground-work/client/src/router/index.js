import Vue from 'vue'
import Router from 'vue-router'

import Guide from '@/components/Guide.vue'
import Signin from '@/components/Signin.vue'
import Signup from '@/components/Signup.vue'
import Home from '@/components/Home.vue'

import NewQn from '@/components/NewQn.vue'

import AllQnList from '@/components/AllQnList.vue'
import FillQn from '@/components/FillQn.vue'

import MyQnList from '@/components/MyQnList.vue'
import EditQn from '@/components/EditQn.vue'

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
        { path: 'allQnList', name: 'allQnList', component: AllQnList },
        { path: 'fillQn', name: 'fillQn', component: FillQn },
        { path: 'myQnList', name: 'myQnList', component: MyQnList },
        { path: 'editQn', name: 'editQn', component: EditQn }
      ]
    },
    { path: '/signin', name: 'signin', component: Signin },
    { path: '/signup', name: 'signup', component: Signup }
  ]
})
