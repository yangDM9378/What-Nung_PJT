<template>
  <div class="container-fluid">
    <div class="row">
      <InformationItem
      v-for="act in actor"
      :key="act.id"
      :act="act"
      class="actoritems col-lg-2 col-md-4 col-sm-6"/>
    </div>
</div>
</template>

<script>
import InformationItem from "@/components/InformationItem"
export default {
  name: 'InformationList',
  components:{
    InformationItem
  } ,
  data() {
    return {
      actor: this.$route.params.actor
    }
  },

}
  
</script>

<style>
.actoritems{
  display: grid;
  grid-template-columns: repeat(6,1fr);
  
}
</style>