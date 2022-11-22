<template>
  <div>
    <h1>CREATE 부분</h1>
    <form @submit.prevent="createComment">
      <!-- <label  for="comment">내용</label> -->
      <input type="text" id="comment" cols="30" rows="2" v-model="comment" placeholder="이 콘텐츠의 어떤 점이 좋았는지 싫었는지 어쩌구 다른 사람들에게 도움을 어쩌구 ">
      <!-- <textarea id="comment reviewbox" cols="30" rows="2" v-model="comment"></textarea><br> -->
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'CreateComment',
  data() {
    return {
      comment: null
    }
  },
  computed: {
    nickname() {
      return this.$store.state.nickname
    }
  },
  methods: {
    createComment() {
      const comment = this.comment
      const movie_id = this.$route.params.id
      const nickname = this.nickname
      if (!comment) {
        alert('내용을 입력하시오')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/backend/moives/${movie_id}/comments/`,
        data: {
          movie_id: movie_id,
          comment: comment,
          nickname: nickname
        },
      })
        .then((res) => {
          console.log(res)
          this.$router.go()
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
}
</script>

<style>
#comment{
  width: 600px;
  height: 300px;
  border-top:none;
  border-left:none;
  border-right:none;
  background-color:rgb(54, 50, 50);
  border-bottom: 3px solid white;

}


</style>