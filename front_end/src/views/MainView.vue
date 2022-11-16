<template>
  <div>
    <h1>MainView입니다.</h1>
    이미지 주소 https://image.tmdb.org/t/p/w500/7ABsaBkO1jA2psC8Hy4IDhkID4h.jpg
  </div>
</template>

<script>
export default {
  name: 'MainView',
  created(){
    this.getMain()
  },
  methods:{
    getMain(){
      this.$store.dispatch('getMain')
    }
  }
}
</script>

<style>

</style>