<template>
  <div>
    <h1>커맨트</h1>
    <CommentListItem/>
    <CreateComment/>
    {{ $route.params.id }}
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem'
import CreateComment from '@/components/CreateComment'
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