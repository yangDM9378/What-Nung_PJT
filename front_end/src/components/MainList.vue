<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      indicators
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    > 
      <b-carousel-slide :img-src="url+randommovie.backdrop_path" v-for="(randommovie, index) in RandomMovies"
      :key="index">
      </b-carousel-slide>
    </b-carousel>
    <h1>전체 영화</h1>
    <div class="row">
      <MainListItem
      v-for="movie in movies"  
      :key="movie.id"
      :movie="movie"
      class="items col-lg-2 col-md-4 col-sm-6"/>
    </div>
  </div>
</template>

<script>
import _ from 'lodash';
import MainListItem from '@/components/MainListItem'
import router from '@/router';
export default {
  name:'MainList',
  components:{
    MainListItem
  },
  computed:{
    movies(){
      return this.$store.state.movies
    },
    RandomMovies(){
      const arr_sample = _.sampleSize(this.movies,5).map((el) =>{
        return el
      })
      return arr_sample
    },
    url(){
      const url = 'https://image.tmdb.org/t/p/original'
      return url
    },
    getactActiveIdx(){
      return this.activeIdx
    }

  },
  data() {
      return {
        randommovie:'',
        slide: 0,
        sliding: null,
        activeIdx: 0,
      }
    },
  methods: {
    onSlideStart() {
      this.sliding = true
    },
    onSlideEnd() {
      this.sliding = false
    },
    removie() {
      if (!this.$store.state.token) {
        router.push({ name: 'LogInView' })
      }
    }
  }
}
</script>

<style>
.container {
  object-fit: fill;
}
.items{
  display: grid;
  grid-template-columns: repeat(6,1fr);
}


</style>