<template>
  <div>
    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
  </ol>
  <div class="carousel-inner" >
    <div class="carousel-item" v-for="(randommovie, index) in RandomMovies"
      :key="index" :class="{active : index === getactActiveIdx}">
      <img class="d-block w-100" :src="url+randommovie" >
    </div>
  </div>
<a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev" @click="decrease">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only"></span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next" @click="increase">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only"></span>
  </a>
</div>
    <!-- <div class="container">
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
    </div> -->
    
    <div>
      <div class='container'>
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
  .container{
    display:grid;
    grid-template-columns: repeat(3,1fr);

  }
</style>