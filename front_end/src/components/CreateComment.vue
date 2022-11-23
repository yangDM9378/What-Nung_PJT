<template>
   <form @submit.prevent="createComment">
  <div>
    <input type="text" id="comment" cols="30" rows="2" v-model="comment" placeholder="이 콘텐츠의 어떤 점이 좋았는지 싫었는지 어쩌구 다른 사람들에게 도움을 어쩌구 " style="color:white">
    </div>
  <div>
    <input type="submit" id="submit" value="등록" style="width:100px">
  </div>
    </form>
 
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
  height: 100px;
  border-top:none;
  border-left:none;
  border-right:none;
  border-bottom: none;
  background-color:#1c1c1c;

}

#submit{
  background-color: white;
  color: black;
  border: 2px solid #555555;
}

#submit:hover {
  background-color:  #008CBA;
  color:black;
}



</style>