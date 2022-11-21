<template>
 <div class="parent">
  <div class="movieparent">
    <div class="back" :style="{backgroundImage:  `url('${ImgSrc}')`}" ></div>
    <div class="content">
      <div>
        <h1>{{this.movie?.title}}</h1>
        <button>내가 너 찜했다!</button>
      </div>
      <h3>별점 | {{this.movie.vote_avg}} 점 </h3>
      <div class="overviewcontaioner">
      <h3 class="overview col-5">줄거리 | {{ this.movie?.overview.substr(0,150) }}...</h3>
      <div class="gencontainer">
        <p>장르 | </p>
        <p v-for="(genre,index) in this.movie?.genres"
        :key="index">{{ genre.name }}</p>
      </div>
      </div>
      
    </div>
   
  </div>
    

      <!-- <p v-for="(cast,idx) in this.movie?.credit_set"
      :key="`case-${idx}`">{{cast.cast_name}}</p> -->
    
    <hr>
      <!-- <nav>
        <router-link :to="{ name: 'InformationList', params: { 'actor': movie.credit_set } }">상세정보</router-link>|
        <router-link :to="{ name: 'CommentList' }">리뷰</router-link>
        <router-view></router-view>
      </nav> -->
    <div class="back2">
    <router-link :to="{ name: 'InformationList', params: { 'actor': movie.credit_set } }">상세정보</router-link>|
    <router-link :to="{ name: 'CommentList' }">리뷰</router-link>
    <router-view></router-view>
    </div>
   
    
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
      const url = 'https://image.tmdb.org/t/p/original'
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
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');


.gencontainer{
  display: flex;
  gap:10px;
}
/* .movieparent{
  display : flex;
  flex-direction : column
} */
.back{
  background-size: cover;
  width: 100%;
  height: 80%;
  color: #fff;
  position: absolute;
  opacity: 0.9;
  margin-bottom: 30px;
  background-position: center;
}

.content{
  background-color: rgba(11, 7, 7, 0.3);
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
.back2{
  float: left;
  font-size: 30px;
  column-gap: 30px;
}


</style>