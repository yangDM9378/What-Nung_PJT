<template>
  <div>
    <h1>상세정보입니다..</h1>
    {{ actor }}
  </div>
</template>

<script>
export default {
  name: 'InformationList',
  data() {
    return {
      actor: this.$route.params.actor
    }
  }
}
</script>

<style>

</style>