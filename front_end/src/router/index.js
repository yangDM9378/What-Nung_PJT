import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '@/views/MainView'
import MyPageView from '@/views/MyPageView'
import MovieDetailview from '@/views/MovieDetailview'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import GenreView from '@/views/GenreView'
import AllGenreView from '@/views/AllGenreView'
import InformationList from '@/components/InformationList'
import CommentList from '@/components/CommentList'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainView',
    component: MainView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  {
    path:'/mypage',
    name: 'MyPageView',
    component: MyPageView
  },
  {
    path: '/Genre',
    name: 'AllGenreView',
    component: AllGenreView
  },
  {
    path: '/Genre/:genre',
    name: 'GenreView',
    component: GenreView
  },
  {
    path: '/:id',
    name: 'detail',
    component: MovieDetailview,
    children: [
      {
        path:'information',
        component: InformationList,
        name:'InformationList',
        props:true
      },
      {
        path:'comment',
        component: CommentList,
        name:'CommentList',
      }
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
