import Vue from 'vue'
import Router from 'vue-router'
import vmain from '@/components/vmain'
import mybook from '@/components/mybook'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: vmain
    },
    {
      path: '/mybook',
      name: 'mybook',
      component: mybook
    }
  ]
})
