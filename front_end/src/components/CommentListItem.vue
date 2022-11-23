<template>
  <div>
    <h5>
    {{ comment.comment }}
    </h5>
    <p>
    {{ comment.nickname }}
    </p>
    <hr style="height:3px">
  </div>

</template>

<script>
export default {
  name: 'CommentListItem',
  props: {
    comment: Object
  },
}
</script>

<style>
.commentbox{
  color: white;
  
}


</style>