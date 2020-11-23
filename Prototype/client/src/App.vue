<!--This is the root component that renders everything. Handles global variables, initiations and renders components in router-view before forcing entry to welcome component. -->
<template>
  <div id="app">
    <!--Debug Manual Navigation -->
    <div style="display: flex; justify-content:center; align-items:center;">
      <div v-if="debugState">
        <router-link class="link" to="/Welcome">Welcome</router-link>
        <router-link class="link" to="/search">Search</router-link>
        <router-link class="link" to="/Browse/1.json">Browse</router-link>
        <router-link class="link" to="/Survey">Survey</router-link>
      </div>
      <!--button id="testBtn" v-on:click="debugState = !debugState">Disable/enable dev</button-->
    </div>

    <!--Renders views in here -->
    <transition name="fade" mode="out-in">
      <router-view></router-view>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      //Global variables. Stores session ID, itteration and what condition to route. Also list containers
      sessionId: " ",
      itteration: 1,
      condition: 4,
      globalList: [],
      previousSelectedList: "",
      weightList: [],
      timeStart: undefined,
      debugState: false,
      listName: 0,
      previousSelection: [],
      tempIDStore: undefined,
    };
  },

  methods: {
    //Generates random session ID based on time. Probabillity of duplicates less than quantum collapse of spacetime within heat death of the universe.
    generateID() {
      const randomID = (
        Date.now().toString(36) +
        Math.random()
          .toString(36)
          .substr(2, 5)
      ).toUpperCase();
      this.sessionId = randomID;
    },
  },
  //Created is vue for "body.onload()"
  created() {
    this.timeStart = Date.now();
    this.generateID();
    this.$router.push({ path: "/welcome" });
    if (this.debugState) {
      console.log("Created session with ID: " + this.sessionId);
    }
  },
};
</script>

<style>
/*Global styles that apply to the whole application */
@font-face {
  font-family: netflix;
  src: url(./assets/fonts/NetflixSans-Regular-Opt.woff2);
}
#app {
  font-family: netflix;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
  overflow-x: hidden;
  overflow-y: hidden;
}
body {
  font-family: netflix;
  background-image: url(./assets/netflixBackground.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
}
.link {
  color: white;
  justify-content: space-between;
  padding: 10px;
}

/* Global Transition styling */
.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.5s;
  transition-property: opacity;
  transition-timing-function: ease;
}
.fade-enter,
.fade-leave-active {
  opacity: 0;
}
#testBtn {
  font-size: 1em;
  border-radius: 4px;
  background-color: red;
  border: none;
  color: white;
  cursor: pointer;
  transition: 0.3s;
}
#testBtn:hover {
  background-color: grey;
}

/*Loading Icon Pure CSS */
.lds-roller {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-roller div {
  animation: lds-roller 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  transform-origin: 40px 40px;
}
.lds-roller div:after {
  content: " ";
  display: block;
  position: absolute;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #fff;
  margin: -4px 0 0 -4px;
}
.lds-roller div:nth-child(1) {
  animation-delay: -0.036s;
}
.lds-roller div:nth-child(1):after {
  top: 63px;
  left: 63px;
}
.lds-roller div:nth-child(2) {
  animation-delay: -0.072s;
}
.lds-roller div:nth-child(2):after {
  top: 68px;
  left: 56px;
}
.lds-roller div:nth-child(3) {
  animation-delay: -0.108s;
}
.lds-roller div:nth-child(3):after {
  top: 71px;
  left: 48px;
}
.lds-roller div:nth-child(4) {
  animation-delay: -0.144s;
}
.lds-roller div:nth-child(4):after {
  top: 72px;
  left: 40px;
}
.lds-roller div:nth-child(5) {
  animation-delay: -0.18s;
}
.lds-roller div:nth-child(5):after {
  top: 71px;
  left: 32px;
}
.lds-roller div:nth-child(6) {
  animation-delay: -0.216s;
}
.lds-roller div:nth-child(6):after {
  top: 68px;
  left: 24px;
}
.lds-roller div:nth-child(7) {
  animation-delay: -0.252s;
}
.lds-roller div:nth-child(7):after {
  top: 63px;
  left: 17px;
}
.lds-roller div:nth-child(8) {
  animation-delay: -0.288s;
}
.lds-roller div:nth-child(8):after {
  top: 56px;
  left: 12px;
}
@keyframes lds-roller {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
#loading {
  position: fixed;
  top: 50%;
  left: 50%;
  width: 80px;
  height: 80px;
  z-index: 99;
}
</style>
