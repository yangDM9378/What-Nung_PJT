<template>
  <div v-if="this.movie">
    <div><img :src="ImgSrc" alt=""></div>
    <h1>{{this.movie?.title}}</h1>
    <h3>overview: {{this.movie?.overview}}</h3>
    <div class="gencontainer">
      <h2 v-for="(genre,index) in this.movie?.genres"
      :key="index">{{ genre.name }}</h2>
    </div>
    <p v-for="(cast,idx) in this.movie?.credit_set"
    :key="`case-${idx}`">{{cast.cast_name}}</p>

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
      return url+this.movie.poster_path
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
    this.getMovieById(this.$route.params.id)
  }
}
</script>

<style>
.gencontainer{
  display: flex;
  margin-left:10px;
}
</style>