<template>
  <div>
    <h1>커맨트 읽어오자</h1>
    <CommentListItem/>
    <CreateComment/>
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem'
import CreateComment from '@/componenets/CreateComment'
export default {
  name: 'CommentList',
  components: {
    CommentListItem,
    CreateComment
  }
}
</script>

<style>

</style>