<template>
  <div id="con">
    <div id="login">
    <div id="login_form">
    <form @submit.prevent="signUp">
        <h3 class="login" style="letter-spacing:-1px;">영화 추천 받을래?</h3>
        <hr>
        <label for="username">
          <p style="text-align: left; font-size:12px; color:#666">username</p>
          <input type="text" id="username" v-model="username" placeholder="아이디" class="size">
        </label>
        <p></p>
        <div>
        <label for="password1">
          <p style="text-align: left; font-size:12px; color:#666">Password </p>
          <input type="password" id="password1" v-model="password1" placeholder="비밀번호" class="size">
        </label>
        </div>
        <div>
        <label for="password2">
          <p style="text-align: left; font-size:12px; color:#666"> </p>
          <input type="password" id="password2" v-model="password2" placeholder="비밀번호 확인" class="size">
        </label>
        </div>
        <p></p>
        <label for="nick_name">
          <p style="text-align: left; font-size:12px; color:#666">NickName</p>
          <input type="nick_name" id="nick_name" v-model="nick_name" placeholder="닉네임" class="size">
        </label>
        <p></p>

    <br>
      <p>
        <input type="submit" value="Create Acoout" class="signup_btn">
      </p>
    </form>

    <hr>
    <p class="find">
        <span><a href="/login" >로그인 가실?</a></span>
    </p>
    </div>
  </div>
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
    },
  }
}
</script>
<style>
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
    background-image:url("");
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
    padding:30px 50px;
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

.signup_btn{
    width:310px;
    height: 40px;
    font-size:15px;
    background-color: #df3278;
    color:#fff;
    border:none;
    cursor: pointer;
    border-radius: 5px;
}
.signup_btn:hover{
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
.num1{
    width:60px;
    text-align: left;
}
.num2{
    width:235px;
}

</style>
