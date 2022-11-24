<template>
  <div style="margin-top: 4rem">
    <div class="row">
      <GenreListItem 
      v-for="genre in genre_select"
      :key=genre.id
      :genre="genre"
      class="col-lg-2 col-md-4 col-sm-6"
      />
    </div>
    <hr>
  </div>
</template>

<script>
import GenreListItem from '@/components/GenreListItem'
export default {
  name: 'GenreView',
  components: {
    GenreListItem
  },
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
