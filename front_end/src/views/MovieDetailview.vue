<template>
  <div>
    <div class="back" :style="{backgroundImage:  `url('${ImgSrc}')`}" >
    <div class="content">
      <h1>{{this.movie?.title}}</h1>
      <h3>별점: </h3>
      <div class="overviewcontaioner">
      <h3 class="overview col-4">줄거리: {{ this.movie?.overview.substr(0,150) }}...</h3>
      </div>
      <div class="gencontainer">
        <h2 v-for="(genre,index) in this.movie?.genres"
        :key="index">{{ genre.name }}</h2>
      </div>
    </div>
    </div>
      <!-- <p v-for="(cast,idx) in this.movie?.credit_set"
      :key="`case-${idx}`">{{cast.cast_name}}</p> -->
    
    <hr>
    <nav>
      <router-link :to="{ name: 'InformationList', params: { 'actor': movie.credit_set } }">상세정보</router-link>|
      <router-link :to="{ name: 'CommentList' }">리뷰</router-link>
      <router-view></router-view>
    </nav>
    </div>
</template>
<script> 
export default {
  name:'MovieDetailview',
  data (){
    return {
      movie: null,
    }
  },

  computed: {
    moviedetail() {
      return this.$store.state.movie
    },
    ImgSrc(){
      const url = 'https://image.tmdb.org/t/p/w500'
      return url+this.movie.backdrop_path
    }
  },
  methods: {
    getMovieById() {
      const id = this.$route.params.id
      if ( this.$store.state.movie.id === Number(id)) {
        this.movie = this.$store.state.movie
      }
    }
  },
  created() {
    this.getMovieById()
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');.gencontainer{
  display: flex;
  gap:10px;
}
.back{
  background-size: cover;
  width: 100%;
  color: #fff;
  position: absolute;
  opacity: 0.9;
  background-position: center;
}

.content{
  background-color: rgba(11, 7, 7, 0.3);
  /* padding-bottom: 80px; */
  position: relative;
  padding-top: 30%;
  padding-left: 20px;
  text-align: left;
  font-weight: bold;
  color: rgb(243, 237, 237);
  font-family: Noto Sans KR,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Fira Sans,Droid Sans,Helvetica Neue,sans-serif;
}

.overviewcontaioner{
  display: grid;
  font-family: Noto Sans KR,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Fira Sans,Droid Sans,Helvetica Neue,sans-serif;
  

}
/* .overview{
  

} */

</style>