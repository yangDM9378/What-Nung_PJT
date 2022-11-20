<template>
  <div>
    <div class="acontainer">
      <nav>
        <div class="link1">
          <router-link :to="{ name: 'AllGenreView' }">전체</router-link>
          <router-link :to="{ name: 'GenreView', params:{ genre: '드라마' }}">드라마</router-link>
          <router-link :to="{ name: 'GenreView', params:{ genre: '액션' }}">액션</router-link>
          <router-link :to="{ name: 'GenreView', params:{ genre: '코미디' }}">코미디</router-link>
          <router-link :to="{ name: 'GenreView', params:{ genre: '애니메이션' }}">애니메이션</router-link>
          </div>
        <div class="link2">
          <router-link :to="{ name: 'MainView' }">Main</router-link>
          <router-link v-if="!isLogin" :to="{ name: 'SignUpView'}">회원가입</router-link> 
          <router-link v-if="!isLogin" :to="{ name: 'LogInView' }">로그인</router-link> 
          <router-link v-if="isLogin" :to="{ name: 'MainView'}">
            <button class="logout_btn" @click="logOut">로그아웃</button>
          </router-link>
        </div> 
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NaviBar',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    logOut() {
      this.$store.dispatch('logOut')
    }
  }
}
</script>

<style>
.acontainer{
  display: inline;
}
.logout_btn {
    margin-right: 20px;
    justify-content: center;
    font-size: 30px;
    font-weight: bold;
    color: #5656df;
    text-decoration: underline;
    background-color:transparent;
}
.link1{
  text-align: left;
}
.link2{
  text-align: right;
}
</style>