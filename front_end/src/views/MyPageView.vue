<template>
  <div>
    <h1>내페이지</h1>
    {{ mydata }}
    <MyPageList/>
  </div>
</template>

<script>
import MyPageList from '@/components/MyPageList'
import axios from 'axios'

export default {
  name: 'MyPageView',
  data() {
    return {
      mydata:null
    }
  },
  components: {
    MyPageList
  },
  methods: {
    getmypage() {
      const API_URL = 'http://127.0.0.1:8000'
      const token = this.$store.state.token
      console.log(token)
      axios({
        method:'get',
        url: `${API_URL}/auth/mymovie/`,
        headers: {
          Authorization: `Token ${token}`
        }
      })
        .then((res) => {
          this.mydata=res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getmypage()
  }
}


// myMovie(context, movie_id) {
//   console.log(`Token ${context.state.token}`)
//   console.log(`${API_URL}/auth/${movie_id}/movie/`)
//   axios({
//     method:'post',
//     url: `${API_URL}/auth/${movie_id}/movie`,
//     headers: {
//       Authorization: `Token ${context.state.token}`
//     }
//   })
//   .then((res) => {
//     console.log(res)
//   })
//   .catch((err) => {
//     console.log(err)
//   })
</script>

<style>

</style>

