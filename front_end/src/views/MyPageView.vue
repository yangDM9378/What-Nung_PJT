<template>
  <div class="container text-center"> 
    <div class="row">
      <h1 style="margin-top:80px; color: #f1f1f6;opacity: 0.8;">{{ nickname }} 님</h1>
      <p> WAT-NUNG</p>
    </div>
    <div class="row">
      <div class="col p-3" style="border-right-style: solid;">
        <div class="row">
          <p style="font-size:1.5em;  color: #f1f1f6; opacity: 0.6;">WAT-NUNG이 추천하는 영화</p>
        </div>
        <br>
        <div class="row">
          <div
            v-for="sm in sortmovie" 
            :key="sm.pk"
            class="col-lg-4 col-md-6 col-sm-12">
            <img :src="`https://image.tmdb.org/t/p/original/${sm.poster_path}`" class='b-card' style="width: 10rem; height: 13rem; margin: 4px;" @click="detailpage(sm.id)">
          </div>
        </div>
      </div>
      <div class="col p-3" style="border-left-style: solid; border:3px">
        <div class="row">
          <p style="font-size:1.5em; color: #f1f1f6; opacity: 0.6;">{{ nickname }} 님이 찜한 영화</p>
        </div>
        <br>
        <div class="row" >
          <div
            v-for='mydata in mydatas'
            :key="mydata.id" 
            class="col-lg-4 col-md-6  col-sm-12"
            @click="detailpage(mydata.id)"
            ><img :src="`https://image.tmdb.org/t/p/original/${mydata.poster_path}`" class='b-card' style="width: 10rem; height: 13rem; margin: 4px;">
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
      }).slice(0,12)
    },
    detailpage(id) {
      this.$router.push({ name:'detail', params:{ id }})
    },
    getMain() {
      this.$store.dispatch('getMain')
    }
  },
  created() {
    this.getmypage()
    this.sortarr()
    this.getMain()
  }
}

</script>

<style>

</style>

