<template>
  <div>
    <h1>내페이지</h1>
    <div
    v-for='(algomovie, index) in algo'
    :key="index" 
    >{{ algomovie.title }} {{ algomovie.poster_path }}</div>
    <hr>
    
    <div
    v-for='mydata in mydatas'
    :key="mydata.id" 
    >{{ mydata.title }}  {{ mydata.poster_path}}
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MyPageView',
  data() {
    return {
      mydatas:null,
      almovie:[],
      algo: []
    }
  },
  computed: {
    ourmovie() {
      return this.$store.getters.ourmovie
    },
    myclick() {
      return this.$store.getters.myclick
    }
  },
  methods: {
    getmypage() {
      const API_URL = 'http://127.0.0.1:8000'
      const token = this.$store.state.token
      axios({
        method:'get',
        url: `${API_URL}/auth/mymovie/`,
        headers: {
          Authorization: `Token ${token}`
        }
      })
        .then((res) => {
          this.mydatas=res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    algorithm() {
      for (let i of this.ourmovie) {
        if (!this.myclick.includes(Number(i))) {
          this.almovie.push(Number(i))
          if (this.almovie.length === 5){
            break
          }
        }
      }  
      for (let al of this.almovie) {
        for (let mo of this.$store.state.movies) {
          if (mo.id == al) {
            this.algo.push(mo)
          }
        }
      }
    }
  },
  created() {
    this.getmypage()
    this.algorithm()
  }
}

</script>

<style>

</style>

