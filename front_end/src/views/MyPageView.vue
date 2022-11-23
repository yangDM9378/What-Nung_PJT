<template>
  <div class="container text-center">
    <div class="row">
      <h1 style="margin-top:80px;">{{ nickname }} 일찍 왔누?</h1>
    </div>
    <div class="row">
      <div class="col p-3">
        <div class="row">
          <p style="font-size:1.5em;">왓눙 추천하는 영화</p>
        </div>
        <div class="row">
          <div
            v-for="sm in sortmovie" 
            :key="sm.pk"
            class="col-lg-4 col-sm-12">
            <img :src="`https://image.tmdb.org/t/p/original/${sm.poster_path}`" class='b-card' style="width: 10rem; height: 13rem;margin: 4px;">
          </div>
        </div>


      </div>
      <div class="col p-3">
        <div class="row">
          <p style="font-size:1.5em;">{{ nickname }} 찜한 영화</p>
        </div>
        <div class="row" style="border-left-style: solid;">
          <div
            v-for='mydata in mydatas'
            :key="mydata.id" 
            class="col-lg-4 col-sm-12"
            ><img :src="`https://image.tmdb.org/t/p/original/${mydata.poster_path}`" class='b-card' style="width: 10rem; height: 13rem;margin: 4px;">
          </div>
        </div>


      </div>  

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
    nickname() {
      return this.$store.state.nickname
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
    sortarr() {
      this.sortmovie=this.$store.state.movies.sort(function(a,b) {
        return b.click - a.click
      }).slice(0,5)
    },
  },
  created() {
    this.getmypage()
    this.sortarr()
  }
}

</script>

<style>

</style>

