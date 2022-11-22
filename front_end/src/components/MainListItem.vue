<template>
  <div>
    <b-card-group>
      <b-card title= '' :img-src="ImgSrc" img-top @click="goDetail(movie.id)">
      </b-card>
    </b-card-group>
  </div>
  
</template>

<script>


export default {
  name:'MainListItem',
  props:{
    movie:Object 
  },
  computed:{
    ImgSrc(){
      const urls = 'https://image.tmdb.org/t/p/w500'
      return urls+this.movie.poster_path
    }
  },
  methods: {
    goDetail(id) {
      this.$router.push({ name:'detail', params:{id} })
      return this.$store.dispatch('clickMovie',this.movie)
    }
  }
}
</script>

<style>

.card_group  img-src {
	-webkit-transform:scale(1);
	-moz-transform:scale(1);
	-ms-transform:scale(1);	
	-o-transform:scale(1);	
	transform:scale(1);
	-webkit-transition:.3s;
	-moz-transition:.3s;
	-ms-transition:.3s;
	-o-transition:.3s;
	transition:.3s;
}
.card_group:hover img-src {
	-webkit-transform:scale(1.2);
	-moz-transform:scale(1.2);
	-ms-transform:scale(1.2);	
	-o-transform:scale(1.2);
	transform:scale(1.2);
}

</style>