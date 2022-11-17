<template>
  <div>
    <!-- <span :src="user_data">{{user_data}}</span> -->
    <MainList/>
  </div>
</template>

<script>
// import axios from 'axios'
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
  mounted() {
    // this.getMe()
  },
  methods:{
    // getMe() {
    //   axios
    //     .get('http://127.0.0.1:8000/accounts/api/v1/users/me/')
    //     .then(response => {
    //       console.log(response)
    //       this.user_data = response.data.username
    //     })
    //     .catch(error => {
    //       console.log(error)
    //     })
    // },
    getMain(){
      this.$store.dispatch('getMain')
    },
  }
}
</script>

<style>

</style>