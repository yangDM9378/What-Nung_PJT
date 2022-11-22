<template>
    <div id="con">
    <div id="login">
    <div id="login_form">
    <form @submit.prevent="logIn">
      <h3 class="login" style="letter-spacing:-1px;">로그인 해줘!</h3>
      <hr>
    <div>
      <label for="username">
      <p style="text-align: left; font-size:12px; color:#666">Username</p>
      <input type="text" id="username" v-model="username" placeholder="너의 아이디는?" class="size">
      </label>
      <p></p>
    </div>
    <div>
      <label for="password">
      <p style="text-align: left; font-size:12px; color:#666">Password </p>
      <input type="password" id="password" v-model="password" placeholder="너의 비번은?" class="size">
      </label>
      <p></p>
    </div>
      <p>
      <input type="submit" value="logIn" class="login_btn">
      </p>
    </form>
    <hr>
    <p class="find">
        <span><a href="signup" >회원가입하실?</a></span>
    </p>
    <!-- <p class="find">
        <span><a href="">아이디 찾기</a></span>
        <span><a href="">비밀번호 찾기</a></span>
        <span><a href="signup.html" >회원가입</a></span>
    </p> -->
    </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>


<style>
/* @import url('http://fonts.googleapis.com/earlyaccess/nanumgothic.css'); */
@font-face {font-family: 'Noto Sans KR';font-style: normal;font-weight: 100;src: url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Thin.woff2) format('woff2'),url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Thin.woff) format('woff'),url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Thin.otf) format('opentype');}
@font-face {font-family: 'Noto Sans KR';font-style: normal;font-weight: 300;src: url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Light.woff2) format('woff2'),url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Light.woff) format('woff'),url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Light.otf) format('opentype');} @font-face {font-family: 'Noto Sans KR';font-style: normal;font-weight: 400;src: url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Regular.woff2) format('woff2'),url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Regular.woff) format('woff'),url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Regular.otf) format('opentype');} @font-face {font-family: 'Noto Sans KR';font-style: normal;font-weight: 500;src: url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Medium.woff2) format('woff2'),url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Medium.woff) format('woff'),url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Medium.otf) format('opentype');} @font-face {font-family: 'Noto Sans KR';font-style: normal;font-weight: 700;src: url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Bold.woff2) format('woff2'),url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Bold.woff) format('woff'),url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Bold.otf) format('opentype');} @font-face {font-family: 'Noto Sans KR';font-style: normal;font-weight: 900;src: url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Black.woff2) format('woff2'),url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Black.woff) format('woff'),url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Black.otf) format('opentype');}

body{
   margin:0 auto;
}
/* body, table, div, p ,span{font-family:'Nanum Gothic';} */
body, table, div, p ,span{font-family:'Noto Sans KR';}

a{
    text-decoration: none;
    color:#333;
}
#con{
    width:100%;
    height: 100vh;
    background-color:#f5f1ee;
    background-image:;
    background-position: center center;
    background-repeat: no-repeat;
    background-size:cover;
    padding:0;
}
#login{
    width:600px;
    height: 600px;
    margin:0 auto;
    /* position: relative; */
    /* background:#ddd; */
}
#login_form{
    /* text-align:center; */
    border-radius: 10px;
    padding:50px;
    background: #fff;
    text-align: center;
    position: absolute;
    top:50%;
    left:50%;
    transform: translate(-50%, -50%);
}
.login{
    font-size:25px;
    font-weight: 900;
    color:#333;
}

.size{
    width:300px;
    height:30px;
    padding-left:10px;
    background-color: #f4f4f4;
    /* margin-left:10px; */
    border:none;
    border-radius: 5px;
}

.login_btn{
    width:310px;
    height: 40px;
    font-size:15px;
    background-color: #df3278;
    color:#fff;
    border:none;
    cursor: pointer;
    border-radius: 5px;
}
.login_btn:hover{
    background:#ca296a;
}
hr{
    margin-top:20px;
    background:#eee;
    
}
.find{
    color:#ddd;
    font-size:12px;
}
.find span{
    padding-left:10px;
}
.find span::before{
    content:'|';
    color:#333;
    padding-right: 10px;
}
.find span:nth-child(1):before{
    content:none;
}

.find span:nth-child(1){
    padding-left:0px;
}

.find a:hover{
    color:#707070;
}
</style>
[출처] HTML/CSS 로그인, 회원가입 폼 실습|작성자 김써니의 코딩기록