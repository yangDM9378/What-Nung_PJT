import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    movies:[],
    movie:{},

    // 유저회원가입 로그인
    access: '',
    refresh: '',
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

    // 회원
    initializeStore(state) {
      if ( localStorage.getItem('access') ) {
        state.access = localStorage.getItem("access")
        state.refresh = localStorage.getItem("refresh")

      } else {
        state.access=''
        state.refresh=''

      }
    },
    setAccess(state, access) {
      state.access = access
    },
    setRefresh(state, refresh) {
      state.refresh = refresh
    },
    REMOVE_ACCESS (state) {
      state.access = '';
      state.refresh = '';
      state.userdata = '';
      state.isAuthenticated = false;
    },

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
    }
  },
  modules: {
  }
})
