<template>
  <div>
    <button @click="logOut">로그아웃</button>
    <MainList/>
  </div>
</template>

<script>
import MainList from '@/components/MainList'
export default {
  name: 'MainView',
  data() { 
    return {
      user_data: ''
    }
  },
  components:{
    MainList,
  },
  created(){
    this.getMain()
  },
  methods:{
    getMain(){
      this.$store.dispatch('getMain')
    },
    logOut() {
      this.$store.dispatch('logOut')
    }
  }
}
</script>

<style>

</style>