<template>
  <div>
    <h1>장르파트</h1>
    {{ genres_movies.name }}
    <hr>
  </div>
</template>

<script>

export default {
  name: 'GenreView',
  data() {
    return {
      genres_movies: null
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  methods: {
    genre_select() {
      this.genres_movies=this.movies.filter((elment) => {
        for (const el of elment.genres) {
          if (el.name === this.$route.params.genre) {
            return elment
          }
        }
      })
    }
  },
  beforecreated() {
    this.genre_select()
  }
}
</script>

<style>

</style>
