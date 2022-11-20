<template>
  <div>
    <h1>나는 {{ this.$route.params.genre }}야 </h1>
    <!-- v-for 로 내려서 하기 -->
    <div class="items">
    <GenreListItem 
      v-for="genre in genre_select"
      :key=genre.id
      :genre="genre"
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
