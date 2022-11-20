<template>
  <div>
    <b-card-group>
      <b-card title=''  :img-src="ImgSrc" img-top @click="goDetail(movie.id)">
      </b-card>
    </b-card-group>
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
      return this.$store.dispatch('clickMovie',this.movie)
    }
  }
}
</script>

<style>

</style>