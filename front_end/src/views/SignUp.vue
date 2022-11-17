<template>
  <div class="sign-up-page">
    <h1>Sign Up</h1>
    <form @submit.prevent="submitForm">
      <label>Username:</label>
      <input type="email" name="username" v-model="username"> <br><br>
      <label>password:</label>
      <input type="password" name="password" v-model="password"> <br><br>
      <button type="submit">Sign up</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'SignUp',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitForm() {
      const formData = {
        username: this.username,
        password: this.password, 
      }

      axios
      .post('http://127.0.0.1:8000/accounts/api/v1/users/', formData)
      .then(response => {
        console.log(response)
        console.log('성공')
        this.$router.push('/login')
      })
      .catch(error => {
        console.log(error)
      })
    }
  }

}
</script>

<style>

</style>