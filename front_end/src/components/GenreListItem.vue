<template>
  <div>
    <b-card-group>
      <b-card title= '' :img-src="ImgSrc" img-top @click="goDetail(genre.id)">
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
export default {
  name: 'GenreListItem',
  props:{
    genre:Object 
  },
  computed: {
    ImgSrc(){
      const urls = 'https://image.tmdb.org/t/p/w500'
      return urls+this.genre.poster_path
    },
  },
  methods: {
    goDetail(id) {
      this.$router.push({ name:'detail', params:{ id } })
      this.$store.dispatch('clickMovie',this.genre)
      this.$store.state.ourmovie.push(this.genre.id)
      if (!this.$store.state.myclick.includes(this.genre.id)) {
        this.$store.state.myclick.push(this.genre.id)
      }
    }
  }
}
</script>

<style>

</style>