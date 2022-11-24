<template>
  <div class="card mx-2 my-2" style="width: 10rem; transform: scale(1.0);">
    <img class="card-img-top" :src="ActorImg">
    <div class="card-body">
      <p class="card-text">{{act.cast_name}}</p>
    </div>
</div>
</template>

<script>
export default {
  name:'InformationItem',
  props:{
    act:Object
  },
  computed:{
    ActorImg(){
      const urls = 'https://image.tmdb.org/t/p/original'
      return urls+this.act.profile_path
    }
}
}
</script>

<style>

</style>