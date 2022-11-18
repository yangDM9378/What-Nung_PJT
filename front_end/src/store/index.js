import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from "vuex-persistedstate";
import router from '@/router'


Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    movies:[],
    movie:{},
    token:null,
  },
  getters: {
  },
  mutations: {
    GET_MAIN(state, movies) {
      state.movies = movies
    },
    CLICK_MOVIE(state, movie) {
      state.movie = movie
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      // console.log(token)
      router.push({ name: 'MainView' })
    }
  },
  actions: {
    getMain(context) {
      axios({
        method: 'get',
        url: `${API_URL}/backend/main/`,
      })
      .then((res) => {
        // console.log(res.data)
        context.commit('GET_MAIN',res.data)
        
      })
      .catch((err) => {
        console.log(err)
      })
    },
    clickMovie(context, movie) {
      context.commit('CLICK_MOVIE', movie)
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },

  },
  modules: {
  }
})
