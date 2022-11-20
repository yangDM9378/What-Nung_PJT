<template>
  <div>
    <h1>커맨트</h1>
    <CommentListItem
    v-for='comment in comments'
    :key="comment.id"
    :comment='comment'/>
    <CreateComment/>

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

</style>