<!--This is the welcome screen with first attention check. -->
<template>
  <div id="container">
    <div class="mainContainer">
      <h1>Instructions</h1>
      <h2>Please read these instructions carefully before you continue. A summary will also be present at the top of every browsing session.</h2>
      <p>Based on the movie you selected, several sets of recommendations will be presented to you. Please inspect the recommendation lists in the next screen and rate how you perceive their ordering from top to bottom before performing any actions. <b><u>You cannot move the lists or select a movie before you do this!</u></b> After this, you are now tasked with rearranging them to an order that fits your preference. Ordering can be done in two ways. Either by dragging the list or clicking the arrow buttons as illustrated below:</p>

      <figure>
        <img src="../assets/dragDrop.gif" />
        <figCaption
          > <p><b>Method 1 seen above:</b> By clicking and holding the left-click down while hovering over the "
          <svg
            aria-hidden="true"
            focusable="false"
            data-prefix="fas"
            data-icon="arrows-alt-v"
            id="example"
            role="img"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 256 512"
          >
            <path
              fill="currentColor"
              d="M214.059 377.941H168V134.059h46.059c21.382 0 32.09-25.851 16.971-40.971L144.971 7.029c-9.373-9.373-24.568-9.373-33.941 0L24.971 93.088c-15.119 15.119-4.411 40.971 16.971 40.971H88v243.882H41.941c-21.382 0-32.09 25.851-16.971 40.971l86.059 86.059c9.373 9.373 24.568 9.373 33.941 0l86.059-86.059c15.12-15.119 4.412-40.971-16.97-40.971z"
            ></path>
          </svg>" symbol next to a list, you can drag the list to move it down or up the order. The doublesided arrow will be grey when you hover over it and red when you are dragging it. </p>
        </figCaption>
      </figure>
      <figure>
        <img src="../assets/buttonClick.gif" />
        <figcaption>
            <p><b>Method 2 seen above:</b> Each list has two sets of arrows - Up and down. By performing a single left-click on an arrow, the list will move into the arrow's direction.</p>
        </figcaption>
      </figure>
      
      <p><b>To summarize:</b> First, evaluate the list order presented to you and rate their order. Then use either or both ordering methods described above to rearrange the list to more closely fit what you would consider being the best order. When both these tasks are done, hover over a movie and click the "Watch later" button to continue. You will not be able to proceed if you do not rate the selection.</p>

      <button class="btnconf" v-on:click.once="nextScreen()"> Continue
      </button>
      <!--div id="container">
      <button class="btnconf" v-if="timerCount == 0" v-on:click.once="nextScreen()">
        Continue
      </button>
      <div v-if="timerCount != 0">
         <p>You can continue in {{timerCount}} seconds</p>
      </div>
      </div-->
    </div>
  </div>
</template>

<script>
export default {
  name: "Instruction",
  data() {
    return {
      timerCount: 20,
    };
  },
  //retrieves current condition from database and sets
  methods: {
    concatPath(id) {
      return "/Browse/" + id;
    },
    nextScreen() {
      this.$router.push({ path: this.concatPath(this.$parent.tempIDStore) });
    },
  },

  watch: {
    timerCount: {
      handler(value) {
        if (value > 0) {
          setTimeout(() => {
            this.timerCount--;
          }, 1000);
        }
      },
      immediate: true, // This ensures the watcher is triggered upon creation
    },
  },
};
</script>

<style scoped>
#container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.mainContainer {
  background-color: black;
  border: 1px solid white;
  padding: 10px;
  max-width: 1200px;
  display: block;
}
p,
h1 {
  color: white;
  padding: 10px;
  text-align: left;
  font-size: 1.1em;
}
h1 {
  font-size: 2em;
  color: #e50914;
  font-weight: bold;
  text-align: center;
}
p {
  margin-top: 3px;
  padding: 10px;
  margin-left: 10px;
  margin-right: 10px;
}
h2 {
    color:white;
    padding:10px;
}
.btnconf {
  padding: 1rem 1.5rem;
  transition: 0.3s;
  border-radius: 3px;
  background-color: #404040;
  font-size: 1.2em;
  border: none;
  color: white;
  margin: 1em;
}
.btnconf:hover {
  background-color: darkgray;
  cursor: pointer;
}
#example {
  height: 1.2em;
}
</style>
