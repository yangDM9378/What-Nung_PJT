<template>
  <div class="totalbox">
    <h1 class="typing-text">WELCOME,
      THIS IS WAT-NUNG</h1>
      <div class="wrapper">
      <div class="link_wrapper">
        <button class="button1">추천 받으시겠습니까?</button>
      <div class="icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 268.832 268.832">
        <path d="M265.17 125.577l-80-80c-4.88-4.88-12.796-4.88-17.677 0-4.882 4.882-4.882 12.796 0 17.678l58.66 58.66H12.5c-6.903 0-12.5 5.598-12.5 12.5 0 6.903 5.597 12.5 12.5 12.5h213.654l-58.66 58.662c-4.88 4.882-4.88 12.796 0 17.678 2.44 2.44 5.64 3.66 8.84 3.66s6.398-1.22 8.84-3.66l79.997-80c4.883-4.882 4.883-12.796 0-17.678z"/>
      </svg>
    </div>
  </div>
</div>
</div>
      <!-- <button class="button5">영화를 추천 받으시겠습니까? </button>
      <button>그냥 구경하겠습니다.</button>
  </div> -->
</template>

<script>
export default {
  name:'LoadingView'
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Rubik+Glitch&family=Rubik+Mono+One&display=swap');

.totalbox{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
}
/* .imgbox{
  background: url("https://mblogthumb-phinf.pstatic.net/20150401_278/gojinmo_14278673400970moD9_JPEG/%C5%B8%C0%CC%C5%B8%B4%D0.jpg?type=w2");
  height: 100vh;
  width: 100%; 

}  */

/* .imgbox:before{
  content:'';
  background: linear-gradient(to top,rgb(255, 254, 254),transparent);
  position: absolute;
  left: 0;
  height: 100%;
  width: 80%;

} */
.typing-text{
  font-family: 'Rubik Glitch', cursive;
font-family: 'Rubik Mono One', sans-serif;
  font-size: 2rem;
  font-weight: bold;
  color: rgb(243, 229, 229);
  border-right: 3px solid white;
  animation: blink .5s infinite , typing 1.5s steps(22);
  white-space: nowrap;
  overflow: hidden;

}
@keyframes blink {
  50%{
    border-color: transparent;
  }
}
@keyframes typing {
  from {
    width: 0;
  }
  to {
    width: 690px;
  }
}


.wrapper{
  position: fixed;
  top: 55%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.link_wrapper{
  position: relative;
}

.button1{
  display: block;
  width: 400px;
  height: 50px;
  line-height: 50px;
  font-weight: bold;
  text-decoration: none;
  background: rgb(189, 53, 53);
  text-align: center;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: 1px;
  border: 3px solid #333;
  transition: all .35s;
}

.icon{
  width: 50px;
  height: 50px;
  border: 3px solid transparent;
  position: absolute;
  transform: rotate(45deg);
  right: 0;
  top: 0;
  z-index: -1;
  transition: all .35s;
}

.icon svg{
  width: 30px;
  position: absolute;
  top: calc(50% - 15px);
  left: calc(50% - 15px);
  transform: rotate(-45deg);
  fill: #2ecc71;
  transition: all .35s;
}

.button1:hover{
  width: 300px;
  border: 3px solid #2ecc71;
  background: transparent;
  color: #2ecc71;
}

.button1:hover + .icon{
  border: 3px solid #2ecc71;
  right: -25%;
}
</style>