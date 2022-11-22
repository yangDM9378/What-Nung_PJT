<template>
  <div >
    <img class="card" style="width: 18rem; height: 30rem; margin-bottom: 8px;" :src="ImgSrc" img-top @click="goDetail(movie.id)">
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

.card:hover{
  transform: scale(1.2);
}
.card{
  transition: transform .5s;
}

</style>