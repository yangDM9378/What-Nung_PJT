<template>
  <div>

    <div class="conddtainer">
      <div>
        <b-carousel
          id="carousel-1"
          v-model="slide"
          :interval="4000"
          controls
          label-next = ''
          label-prev=''
          indicators
          background="#ababab"
          img-width="1024"
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
    </div >

    <h1>전체 영화</h1>
      <div class="items">
        <MainListItem
        v-for="movie in movies"  
        :key="movie.id"
        :movie="movie"
        />
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
      console.log(arr_sample)
      return arr_sample
    },
    url(){
      const url = 'https://image.tmdb.org/t/p/w500'
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
      increase() {
        if (this.activeIdx == 4){
          this.activeIdx = 0 
        } else {
          this.activeIdx += 1 
        }
        console.log("increase")
      },
      decrease() {
        if (this.activeIdx == 0){
          this.activeIdx = 4 
        } else {
          this.activeIdx -= 1
        }
        console.log("decrease")
      },
    }
}
</script>

<style>
.container {
  object-fit: fill;
}

</style>