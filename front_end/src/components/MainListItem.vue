<template>
  <div>
    <div>
      <img :src="ImgSrc" @click="goDetail(movie.id)"> 
    </div>
        <!-- <img :src="ImgSrc" @click="goDetail(movie.id)"> -->
  </div>
</template>

<script>

export default {
  name:'MainListItem',
  props:{
    movie:Object
  },
  computed:{
    ImgSrc(){
      const urls = 'https://image.tmdb.org/t/p/w500'
      return urls+this.movie.poster_path
    }
  },
  methods: {
    goDetail(id) {
      this.$router.push({ name:'detail', params:{id} })
      return this.$store.dispatch('clickMovie',this.movie)
    }
  }
}
</script>

<style>
.card { 
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  /* grid-gap: 20px; */
  align-items: start;
  }
</style>