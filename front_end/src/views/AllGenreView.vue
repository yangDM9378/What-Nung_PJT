<template>
  <div style="margin-top: 80px">
    <div class="row">
      <AllGenreListItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
      class="col-lg-2 col-md-4 col-sm-6"
      />
    </div>
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
