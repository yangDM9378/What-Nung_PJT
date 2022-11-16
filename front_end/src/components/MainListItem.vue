<template>
  <div class="container">
    <div class="card">
      <img :src="ImgSrc" alt="">
    </div>

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
      const url = 'https://image.tmdb.org/t/p/w500'
      return url+this.movie.poster_path
    }
    
  }
}
</script>

<style>
.container{
  display: flex;
  flex-direction: column;
  width: calc((100% / 3) - 2rem);
}
.card{
  width: 50%;
  height: 0;
}
</style>