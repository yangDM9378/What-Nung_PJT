<template>
  <div id="app">
    <nav>
      <router-link :to="{name: 'MainView'}">MainView</router-link> |
      <router-link to="/signup">Sign up</router-link> |
      <router-link to="/login">Log in</router-link> |
      <button @click="logout">logout</button>
    </nav>
    <router-view/>
  </div>
</template>


<script>
import axios from 'axios';

export default{
  name: 'App',
  beforeCreate() {
    this.$store.commit('initializeStore')

    const access = this.$store.state.access
    
    if ( access ) {
      axios.defaults.headers.common['Authorization'] = 'JWT' + access
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  mounted() {
    setInterval(() => {
      this.getAccess()
    }, 10000)
  },
  methods: {
    getAccess() {
      const accessData = {
        refresh: this.$store.state.refresh
      }
      axios
        .post('http://127.0.0.1:8000/accounts/api/v1/jwt/refresh', accessData)
        .then(response => {
          const access = response.data.access
          localStorage.setItem('access', access)
          this.$store.commit('setAccess', access)
        })
      },
    logout () {
      this.$store.commit('REMOVE_ACCESS');
      localStorage.setItem('access', '');
      localStorage.setItem('refresh', '');
    }
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
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
