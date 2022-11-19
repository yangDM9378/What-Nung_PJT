<template>
  <div>
    <h1>전체장르야 나는</h1>
    {{ this.movies }}
    <hr>
  </div>
</template>

<script>

export default {
  name: 'AllGenreView',
  computed: {
    movies() {
      return this.$store.state.movies
    },
  },
}
</script>

<style>

</style>
