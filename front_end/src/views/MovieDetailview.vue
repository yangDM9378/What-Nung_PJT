<template>
 <div class="Container-fluid" v-if="movie">
  <div style="width: 100%; height: 100%;">
    <div class="row"
    id="backdrop"
    :style="{backgroundImage: `linear-gradient(to top, rgb(0, 0, 0) 0%, rgba(0, 0, 0, 0) 30%), linear-gradient(to right, rgb(0, 0, 0) 20%, rgba(0, 0, 0, 0) 60%, rgba(0, 0, 0, 0.1) 30%), url('${ImgSrc}')`}"
    >
      <div class="row"
      id="content">
        <h1>{{this.movie?.title}}
          <font-awesome-icon icon="fa-solid fa-heart-circle-plus" v-if="!ismymoive" @click="myMovie"/>
          <font-awesome-icon icon="fa-solid fa-heart-circle-check" v-if="ismymoive" @click="myMovie"/>

  
        </h1>

         <h3>별점 | {{this.movie.vote_avg}} 점 </h3>
         <h4>줄거리 | {{ this.movie?.overview.substr(0,100) }}...</h4>
         <div clas="row">
          <div class="column"
          id="genrename">
            <p>장르 | </p>
            <p v-for="(genre,index) in this.movie?.genres"
            :key="index">{{ genre.name }}</p>
          </div>
         </div>
        </div> 
        <hr>
        <div class="row">
          <div id="routerbox">
            <router-link :to="{ name: 'InformationList', params: { 'actor': movie.credit_set } }" style="margin-right:15px">출연진</router-link>|
            <router-link :to="{ name: 'CommentList' }" style="margin-left:10px">리뷰</router-link>
            <router-view></router-view>
          </div>
        </div>
    </div>
  </div>
</div>


</template>
<script> 
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name:'MovieDetailview',
  data (){
    return {
      movie: null,
      tf: null,
    }
  },
  computed: {
    token() {
      return this.$store.state.token
    },
    moviedetail() {
      return this.$store.state.movie
    },
    ImgSrc() {
      const url = 'https://image.tmdb.org/t/p/original'
      return url+this.movie.backdrop_path
    },
    ismymoive: {
      get() {
        return this.$store.state.ismymoive
      },
      set(data) {
        this.$store.state.ismymoive = data
      }
    },
  },
  methods: {
    getMovieById() {
      axios({
        method:'get',
        url:`${API_URL}/backend/movies/${this.$route.params.id}/`,
      })
      .then((res) => {
        this.movie=res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },

    myMovie() {
      this.$store.dispatch('myMovie', this.$route.params.id)
    }, 
    myisMovie() {
      axios({
        method:'get',
        url: `${API_URL}/auth/${this.$route.params.id}/movie`,
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
      .then((res) => {
        this.ismymoive=res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created() {
    window.scrollTo(0,0)
    this.getMovieById()
    if (this.token) {
      this.myisMovie()
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');


.container{
  margin: 0px;
}


#content{
  position: relative;
  padding-top: 40vh;
  padding-left: 40px;
  text-align: left;
  font-weight: bold;
  color: rgb(243, 237, 237);
  width:30%;
  row-gap: 5px;
}

#genrename{
  display: flex;
  color: rgb(243, 237, 237);
  gap: 10px;
  border-bottom:1px solid #626262

  
}


#backdrop {
  height: 700px;
  background-size: cover;
  text-overflow: ellipsis;
  background-repeat: no-repeat;
  background-position: center 20%;
}

#routerbox{
  text-align: left;
  margin-left: 30px;
 
;
}
  /* padding-bottom: 500px; */
  /* width: 100%; */
#routerbox a{
  color: #777;
  font-size: 20px;
  text-decoration: none;
  font-weight: bold;

}

#routerbox a.router-link-exact-active {
  color: #9090ee;
  text-decoration: underline;


}
</style>