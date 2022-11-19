<template>
  <div>
    <h1>나는 {{ this.$route.params.genre }}야 </h1>
    {{ this.genre_select }}
    <!-- v-for 로 내려서 하기 -->
    <GenreListItem/>
    <hr>
  </div>
</template>

<script>

export default {
  name: 'GenreView',
  computed: {
    movies() {
      return this.$store.state.movies
    },
    genre_select() {
     return this.movies.filter((elment) => {
        if (elment.genres.length){
          for (const el of elment.genres) {
            if (el.name === this.$route.params.genre) {
              return elment
            }
          }
        }
      })
    }
  },
  methods: {
  },
}
</script>

<style>

</style>
