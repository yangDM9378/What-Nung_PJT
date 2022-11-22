<template>
  <div>
    <div  class="items">
      <AllGenreListItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
      />
    </div>
    <hr>
  </div>
</template>

<script>
import AllGenreListItem from '@/components/AllGenreListItem'
export default {
  name: 'AllGenreView',
  components: {
    AllGenreListItem
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
  },
}
</script>

<style>

</style>
