<template>
  <div>
    <h1>내페이지</h1>
    <div
    v-for="sm in sortmovie" 
    :key="sm.pk">{{ sm.title }}</div>
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
      sortmovie:null
    }
  },
  computed: {
    myclick() {
      return this.$store.getters.myclick
    },
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
    sortarr() {
      this.sortmovie=this.$store.state.movies.sort(function(a,b) {
        return b.click - a.click
      }).slice(0,5)
    }
  },
  created() {
    this.getmypage()
    this.sortarr()
  }
}

</script>

<style>

</style>

