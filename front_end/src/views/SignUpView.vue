<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">아이디입력 : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1">이건 패스워드 : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2">이건 패스워드 확인 : </label>
      <input type="password" id="password2" v-model="password2"><br>
      
      <label for="nick_name">닉네임 입력해 : </label>
      <input type="nick_name" id="nick_name" v-model="nick_name"><br>
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      nick_name: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const nick_name = this.nick_name

      const payload = {
        // username,
        // password1,
        // password2,
        username: username,
        password1: password1,
        password2: password2,
        nick_name: nick_name,
      }
      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>
