import Vue from 'vue'
import Router from 'vue-router'

import Guide from '@/components/Guide.vue'
import Home from '@/components/Home.vue'

import Signin from '@/components/account/Signin.vue'
import Signup from '@/components/account/Signup.vue'

import QnHome from '@/components/questionnaire/QnHome.vue'
import NewQn from '@/components/questionnaire/NewQn.vue'
import AllQnList from '@/components/questionnaire/AllQnList.vue'
import FillQn from '@/components/questionnaire/FillQn.vue'
import MyQnList from '@/components/questionnaire/MyQnList.vue'
import EditQn from '@/components/questionnaire/EditQn.vue'

import TaskHome from '@/components/task/TaskHome.vue'
import TaskList from '@/components/task/TaskList.vue'
import NewTask from '@/components/task/NewTask.vue'
import TaskDetail from '@/components/task/TaskDetail.vue'

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
        // qn
        { path: 'qnHome', name: 'qnHome', component: QnHome },
        { path: 'newQn', name: 'newQn', component: NewQn },
        { path: 'allQnList', name: 'allQnList', component: AllQnList },
        { path: 'fillQn', name: 'fillQn', component: FillQn },
        { path: 'myQnList', name: 'myQnList', component: MyQnList },
        { path: 'editQn', name: 'editQn', component: EditQn },
        // task
        { path: 'taskHome', name: 'taskHome', component: TaskHome },
        { path: 'taskList', name: 'taskList', component: TaskList },
        { path: 'newTask', name: 'newTask', component: NewTask },
        { path: 'taskDetail', name: 'taskDetail', component: TaskDetail }
      ]
    },
    { path: '/signin', name: 'signin', component: Signin },
    { path: '/signup', name: 'signup', component: Signup }
  ]
})
