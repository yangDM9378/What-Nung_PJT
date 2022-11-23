<template>
  <div>
    <div>
      <img class="card" style="width: 18rem; height: 30rem; margin-bottom: 8px;" :src="ImgSrc" img-top @click="goDetail(genre.id)">
    </div>
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
      if (!this.$store.state.myclick.includes(this.genre.id)) {
        this.$store.state.myclick.push(this.genre.id)
      }
      this.$store.dispatch('ourclick', this.genre.id)
    }
  }
}
</script>

<style>

</style>