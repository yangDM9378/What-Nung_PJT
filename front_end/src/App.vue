<template>
  <div id="app"> 
    <NaviBar/>
    <router-view/>
  </div>
</template>


<script>
import NaviBar from '@/components/NaviBar'
export default {
  name: 'App',
  components: {
    NaviBar,
  },
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  display: flex;
  opacity: 0.6;
  position: fixed;
  background: #000001;
  right: 0;
  left: 0;
  width: 100%;
  /* padding: 3px; */
  display: table;
  margin: 0 auto;
  z-index:1;
  transition: all 300ms ease-in-out;
}

.acontainer{
  line-height: 55px;
  text-align:right;
  display: flex;
}


nav a {
  margin-right: 20px;
  justify-content: center;
  font-size: 30px;
  font-weight: bold;
  color: #f1f1f6;
}

nav a.router-link-exact-active {
  color: #5656df;
}
</style>
