<template>
  <div>
    <div class="fill">
      <div>
        <b-carousel 
          id="carousel-1"
          v-model="slide"
          :interval="4000"
          controls
          indicators
          background="#ababab"
          img-width="100"
          img-height="480"
          style="text-shadow: 1px 1px 2px #333;"
          @sliding-start="onSlideStart"
          @sliding-end="onSlideEnd"
        >
          <b-carousel-slide :img-src="url+randommovie" v-for="(randommovie, index) in RandomMovies"
      :key="index">
          </b-carousel-slide>
        </b-carousel>
      </div>
    </div>
    
    <div class="container fill">
      <div>
        <MainListItem
        v-for="movie in movies"  
        :key="movie.id"
        :movie="movie"
        />
      </div>
    </div>

  </div>
  </template>

<script>
import _ from 'lodash';
import MainListItem from '@/components/MainListItem'
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
        return el.backdrop_path
      })
      return arr_sample
    },
    url(){
      const url = 'https://image.tmdb.org/t/p/w500'
      return url
    }

  },
  data() {
      return {
        randommovie:'',
        slide: 0,
        sliding: null
      }
    },
    methods: {
      onSlideStart() {
        this.sliding = true
      },
      onSlideEnd() {
        this.sliding = false
      }
    }
}
</script>

<style>
</style>