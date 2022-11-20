<template>
  <div>
    <h1>CREATE 부분</h1>
    <form @submit.prevent="createComment">
      <label for="comment">내용</label>
      <input type="text" id="comment" v-model.trim="comment"><br>
      <input type="submit" id="submit">
    </form>

  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'CreateComment',
  data() {
    return {
      comment: null
    }
  },
  methods: {
    // createComment() {
    //   const comment = this.comment
    //   const movie_id = $route.params.id
    //   if (!comment) {
    //     alert('내용을 입력하시오')
    //     return
    //   }
    //   axios({
    //     method: 'post',
    //     url: `${API_URL}/backend/movies/${movie_id}/comments/`,
    //     data: {
    //       'comment':comment
    //     }
    //   })
    //     .then((res) => {
    //       console.log(res)
    //     })
    //     .catch(err => console.log(err))
    // }
  },
}
</script>

<style>

</style>