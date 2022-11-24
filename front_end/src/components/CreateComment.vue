<template>
  <div>
    <form @submit.prevent="createComment"  v-if="this.$store.state.token">
      <input required type="text" id="info-comment" cols="30" rows="2" v-model="comment" placeholder=" 이 영화에 대한 리뷰를 적어주세요." style="color:white; margin-bottom:16px">
      <input type="submit" id="info-submit" value="등록" style="width:15%;">
    </form>
    <form @submit.prevent="createComment"  v-if="!this.$store.state.token">
      <input disabled  type="text" id="info-comment" cols="30" rows="2" v-model="comment" placeholder="   댓글 작성을 위해 로그인이 필요합니다." style="color:white; margin-bottom:16px">
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
#info-comment{
  width: 95%;
  height: 100px;
  border-top:none;
  border-left:none;
  border-right:none;
  border-bottom: none;
  background-color:#1c1c1c;
}

#info-submit{
  background-color: white;
  color: black;
  border: 2px solid #555555;
}

#info-submit:hover {
  color:black;
}
#info-submit:active{
  box-shadow: 1px 1px 0 rgb(0,0,0,0.5);
  position: relative;
  top:2px;
}


</style>