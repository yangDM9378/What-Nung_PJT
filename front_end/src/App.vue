<template>
  <div id="app">
    <div class="acontainer">
      <nav>
        <router-link :to="{name: 'MainView'}">Main</router-link> |
        <router-link :to="{ name: 'SignUpView'}">회원가입</router-link> |
        <router-link :to="{ name: 'LogInView' }">로그인</router-link>
      </nav>
    </div>
    <router-view/>
  </div>
</template>


<script>
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
  position: fixed;
  background: #000001;
  top: 0;
  right: 0;
  left: 0;
  width: 100%;
  height: 100px;
  display: table;
  margin: 0 auto;
  z-index:1;
}

.acontainer{
  display: flex;
}


nav a {
  justify-content: center;
  text-align: center;
  font-size: 30px;
  font-weight: bold;
  color: #f1f1f6;
}

nav a.router-link-exact-active {
  color: #5656df;
}
</style>
