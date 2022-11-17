import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '@/views/MainView'
import MovieDetailview from '@/views/MovieDetailview'
import SignUp from '@/views/SignUp'
import LogIn from '@/views/LogIn'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainView',
    component: MainView
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/login',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/:id',
    name: 'detail',
    component: MovieDetailview
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
