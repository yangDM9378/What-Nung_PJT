import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    getMain() {
      axios({
        method: 'get',
        url: `${API_URL}/backend/main/`,
      })
      .then((res) => {
        console.log(res)
        
      })
      .catch((err) => {
        console.log(err)
      })

    }
  },
  modules: {
  }
})
