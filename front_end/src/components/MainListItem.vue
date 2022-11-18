<template>
    <div>
      <b-card-group>
    <b-card title="Title" :img-src="ImgSrc" img-top>
      <template #footer>
        <small class="text-muted">Last updated 3 mins ago</small>
      </template>
    </b-card>

    <b-card title="Title" img-src="https://placekitten.com/g/300/450" img-alt="Image" img-top>

      <template #footer>
        <small class="text-muted">Last updated 3 mins ago</small>
      </template>
    </b-card>
  </b-card-group>
      <img :src="ImgSrc" @click="goDetail(movie.id)"> 
    </div>
  
</template>

<script>

export default {
  name:'MainListItem',
  props:{
    movie:Object
  },
  computed:{
    ImgSrc(){
      const urls = 'https://image.tmdb.org/t/p/w500'
      return urls+this.movie.poster_path
    }
  },
  methods: {
    goDetail(id) {
      this.$router.push({ name:'detail', params:{id} })
      return this.$store.dispatch('clickMovie',this.movie)
    }
  }
}
</script>

<style>

</style>