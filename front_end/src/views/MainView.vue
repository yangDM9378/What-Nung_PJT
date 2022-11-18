<template>
  <div>
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
  }
}
</script>

<style>

</style>