<template>
    <div>
   
    <b-card-group>
    <b-card title= '' :img-src="ImgSrc" img-top>
    </b-card>

  </b-card-group>
      <!-- <img :src="ImgSrc" @click="goDetail(movie.id)">  -->
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
      console.log(this.movie)
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

</style>