<template>
  <div class="col-lg-2 col-md-4 col-sm-6">
    <img class="card" style="width: 18rem; height: 30rem; margin-bottom: 8px;" :src="ImgSrc" img-top @click="goDetail(movie.id)">
  </div>
</template>

<script>
export default {
  name: 'AllGenreListItem',
  props:{
    movie:Object 
  },
  computed:{
    ImgSrc(){
      const urls = 'https://image.tmdb.org/t/p/w500'
      return urls+this.movie.poster_path
    },
  },
  methods: {
    goDetail(id) {
      this.$router.push({ name:'detail', params:{ id } })
      this.$store.dispatch('clickMovie',this.movie)
      this.$store.dispatch('ourclick', this.movie.id)
      if (!this.$store.state.myclick.includes(this.movie.id)) {
        this.$store.state.myclick.push(this.movie.id)
      }
    }
  }
}
</script>

<style>

</style>