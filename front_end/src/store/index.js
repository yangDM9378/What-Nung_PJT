import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  state: {
    movies:[],
  },
  getters: {
  },
  mutations: {
    GET_MAIN(state,movies){
      state.movies = movies
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

    }
  },
  modules: {
  }
})
