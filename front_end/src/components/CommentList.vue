<template>
  <div class="reviewbox mt-3">
    <div class="create">
      <CreateComment />
    </div>
    <div class="commentbox ">
    <CommentListItem 
    v-for='comment in comments'
    :key="comment.id"
    :comment='comment'
    />
  </div>

  </div>
</template>

<script>
import CreateComment from '@/components/CreateComment'
import CommentListItem from '@/components/CommentListItem'

export default {
  name: 'CommentList',
  data() {
    return {
      movie_id: this.$route.params.id
    }
  },
  computed: {
    comments() {
      return this.$store.state.comment.filter((el) => {
        if (el.movie == this.movie_id) {
          return el
        }
      })
    }
  },
  components: {
    CreateComment,
    CommentListItem,
  },
  methods: {
    getComment() {
      return this.$store.dispatch('getComment')
    }
  },
  mounted() {
    this.getComment()
  }
}
</script>

<style>
.reviewbox {
  display: flex;
  justify-content: space-between;
  
}
.createbox {
  display: flex;
  flex-direction: column;
  width:50%;
  

}
.commentbox{
  display: flex;
  flex-direction: column;
  width:60%;
  
}
</style>