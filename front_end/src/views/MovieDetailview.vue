<template>
 <div class="Container-fluid">
  <div >
    <div class="row"
    id="backdrop"
    :style="{backgroundImage:  `url('${ImgSrc}')`}"
    > 
    <div >
      <div class="row"
      id="content">
        <h1>{{this.movie?.title}}</h1>
         <button @click="myMovie">내가 너 찜했다!</button>
         <h3>별점 | {{this.movie.vote_avg}} 점 </h3>
         <h3>줄거리 | {{ this.movie?.overview.substr(0,150) }}...</h3>
        </div>
      </div>
      <div class="row"
      id="genrename">
        <p>장르 | </p>
        <p v-for="(genre,index) in this.movie?.genres"
        :key="index">{{ genre.name }}</p>s
      </div>
    </div>
    <div class="row">
      <router-link :to="{ name: 'InformationList', params: { 'actor': movie.credit_set } }">상세정보</router-link>|
      <router-link :to="{ name: 'CommentList' }">리뷰</router-link>
      <router-view></router-view>
    </div>
  </div>
  <!-- <div>
    <div class="back" :style="{backgroundImage:  `url('${ImgSrc}')`}" >
    <div class="content">
      <h1>{{this.movie?.title}}</h1> -->
      <!-- <button @click="myMovie">내가 너 찜했다!</button> -->
      <!-- <h3>별점 | {{this.movie.vote_avg}} 점 </h3>
       <h3 class="overview col-5">줄거리 | {{ this.movie?.overview.substr(0,150) }}...</h3>
      <div class="gencontainer">
        <p>장르 | </p>
        <p v-for="(genre,index) in this.movie?.genres"
        :key="index">{{ genre.name }}</p>
      </div>
    </div>
  </div>
  <div
  style="float:left; margin-top:90vh;"
  >
    <router-link :to="{ name: 'InformationList', params: { 'actor': movie.credit_set } }">상세정보</router-link>|
    <router-link :to="{ name: 'CommentList' }">리뷰</router-link>
    <router-view></router-view>
  </div>
</div> -->
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
    // myMovie() {
    //   this.$store.dispatch('myMovie', this.movie)
    // },
  created() {
    this.getMovieById()
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');


.container{
  margin: 0px;
}





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
  height: 82vh;
  color: #fff;
  position: absolute;
  opacity: 0.9;
  margin-bottom: 30px;
  background-position: center;
}

#content{
  background-color: rgba(11, 7, 7, 0.3);
  position: relative;
  padding-top: 30vh;
  padding-left: 20px;
  text-align: left;
  font-weight: bold;
  color: rgb(243, 237, 237);
  font-family: Noto Sans KR,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Fira Sans,Droid Sans,Helvetica Neue,sans-serif;
}

#genrename{
  display: inline;
  text-align: left;
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

#backdrop {
  height: 700px;
  background-size: cover;
}



</style>