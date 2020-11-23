<!--This is the welcome screen with first attention check. -->
<template>
  <div id="container">
    <div class="mainContainer">
      <h1>Task Description</h1>
      <table>
        <tr>
          <!--The hardcoded SVG isn't preatty, but it is reliable -->
          <th>
            <svg
              aria-hidden="true"
              focusable="false"
              data-prefix="fas"
              data-icon="exclamation-triangle"
              class="svgData"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 576 512"
            >
              <path
                fill="currentColor"
                d="M569.517 440.013C587.975 472.007 564.806 512 527.94 512H48.054c-36.937 0-59.999-40.055-41.577-71.987L246.423 23.985c18.467-32.009 64.72-31.951 83.154 0l239.94 416.028zM288 354c-25.405 0-46 20.595-46 46s20.595 46 46 46 46-20.595 46-46-20.595-46-46-46zm-43.673-165.346l7.418 136c.347 6.364 5.609 11.346 11.982 11.346h48.546c6.373 0 11.635-4.982 11.982-11.346l7.418-136c.375-6.874-5.098-12.654-11.982-12.654h-63.383c-6.884 0-12.356 5.78-11.981 12.654z"
              ></path>
            </svg>
          </th>
          <th>
            Throughout the study, you will see this type of instruction box at
            the top of every page. Please read it carefully each time! Do not
            refresh the page at any time, or your progress will be lost, and you
            will have to start anew.
            <span id="alerter"
              >In the following, you will receive a task description. Please
              read it carefully to the end.</span
            >
          </th>
          <th></th>
          <th>
            <svg
              aria-hidden="true"
              focusable="false"
              data-prefix="fas"
              data-icon="exclamation-triangle"
              class="svgData"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 576 512"
            >
              <path
                fill="currentColor"
                d="M569.517 440.013C587.975 472.007 564.806 512 527.94 512H48.054c-36.937 0-59.999-40.055-41.577-71.987L246.423 23.985c18.467-32.009 64.72-31.951 83.154 0l239.94 416.028zM288 354c-25.405 0-46 20.595-46 46s20.595 46 46 46 46-20.595 46-46-20.595-46-46-46zm-43.673-165.346l7.418 136c.347 6.364 5.609 11.346 11.982 11.346h48.546c6.373 0 11.635-4.982 11.982-11.346l7.418-136c.375-6.874-5.098-12.654-11.982-12.654h-63.383c-6.884 0-12.356 5.78-11.981 12.654z"
              ></path>
            </svg>
          </th>
        </tr>
      </table>

      <!--Alternates instructions based on condition. -->
      <p>
        Imagine now that you are sitting down to enjoy a movie, but are
        uncertain which one to watch. You decide to explore what the system has
        to offer based on previous movies you have watched to find something new
        to your taste.
      </p>
      <div v-if="[1, 2, 3].includes(this.$parent.condition)">
        <p class="point"><b>1)</b> First, you will be tasked with searching for and
        selecting a movie you have previously enjoyed. This movie will be the
        base for the recommendations in the next step.</p>
        <p class="point"><b>2)</b> We will then provide eleven different sets of recommendations containing
        five movies each. Please take a moment to assess how these lists are
        ranked, from top to bottom, and rate your satisfaction with this order. When done, you
        select a movie by hovering over it and clicking "watch later". The movie selected will influence
        future recommendations</p>
        <p class="point"><b>3)</b> These two steps will be repeated a total of five times. You can view
        which step you are on in the top right corner.</p>
        <p class="point"><b>4)</b> When finished, you will then be asked a few questions that conclude
        the study. Please answer them carefully. When completed, the system will
        generate your mTurk code.</p>
      </div>
      <div v-if="[4, 5, 6].includes(this.$parent.condition)">
        <p class="point"><b>1)</b> First, you will be tasked with searching for and
        selecting a movie you have previously enjoyed. This movie will be the
        base for the recommendations in the next step.</p>
        <p class="point"><b>2)</b> We will then provide eleven different sets of recommendations containing
        five movies each. Please take a moment to assess how these lists are
        ranked from top to bottom and rate your satisfaction with this order. If you are displeased, please reorder these
        lists to your preference. Further information on this will be shown before presenting you to this task. When done, you select a movie by hovering over
        it and clicking "watch later". The movie selected and your ordering will influence future
        recommendations.</p>
        <p class="point"><b>3)</b> These two steps will be repeated a total of five times. You can view
        which step you are on in the top right corner.</p>
        <p class="point"><b>4)</b> When finished, you will then be asked a few questions that conclude
        the study. Please answer them carefully. When completed, the system will
        generate your mTurk code.</p>
      </div>

      <p>
        Note that our survey system only contains a limited number of movies;
        especially newer movies might be missing. If the movie you would like to
        select is not available, please search for another.
      </p>
      <p style="text-align: center;">
        To check that you read the above description carefully, we ask you
        kindly to click
        <button id="hiddenButton" v-on:click.once="proceed(true)">here</button> to
        proceed instead of clicking on the button below.
      </p>
      <p style="text-align: center;">
        Thank you for your participation in this study!
      </p>

      <button class="fakeButton" v-on:click.once="proceed(false)">Continue</button>

      <!--Debug Manual Condition setters -->
      <div v-if="this.$parent.debugState" class="mainContainer">
        <h1>DEV MODE ENABLED</h1>
        <h2>Manual Condition Selection</h2>
        <p style="text-align:center">
          Current condition active = {{ this.$parent.condition }}
        </p>
        <p style="text-align:center">
          Sub condition A: Random sort after each input<br />
          Sub condition B: Previous Order + Last selected in condition 1A<br />
          Sub condition C: Weights applied each itteration based on hierarchy
          Order<br />
        </p>

        <div
          style="display:flex; flex-direction:row; justify-content:center; align-content:center;"
        >
          <div>
            <p style="text-align:center">Condition 1: No control elements.</p>
            <button v-on:click="setCondition(1)">Condition 1A(1)</button>
            <button v-on:click="setCondition(2)">Condition 1B(2)</button>
            <button v-on:click="setCondition(3)">Condition 1C(3)</button>
          </div>
          <div>
            <p style="text-align:center">Condition 2: Control elements.</p>
            <button v-on:click="setCondition(4)">Condition 2A(4)</button>
            <button v-on:click="setCondition(5)">Condition 2B(5)</button>
            <button v-on:click="setCondition(6)">Condition 2C(6)</button>
          </div>
        </div>

        <div>
          <p style="text-align:center;">
            Disable Dev mode: Site will need to be refreshed to enable it again
            <br />
            This setting enables verbose console logging, additional navigation
            elements at the top and manual setting of different parameters.
          </p>
          <button class="fakeButton" v-on:click="disablePanel">Disable</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PostService from "../SearchService";

export default {
  name: "Welcome",

  //retrieves current condition from database and sets
  async created() {
    try {
      var temp = await PostService.getCondition();
      this.$parent.condition = temp[0].condition;
    } catch (err) {
      console.log(err);
    }
  },

  methods: {
    /* Create database entry for this session when user clicks a button to navigate*/

    async createSession(attentionCheck) {
      await PostService.createSession(
        this.$parent.sessionId,
        this.$parent.condition,
        attentionCheck
      );
    },

    /*Handles button actions*/
    setCondition(index) {
      this.$parent.condition = index;
    },
    //Production button handler
    proceed(check) {
      this.createSession(check);
      if (this.$parent.debugState) {
        console.log("passed first attentioncheck: " + check);
      }
      this.$router.push({ path: "/search" });
    },
    disablePanel() {
      this.$parent.debugState = !this.$parent.debugState;
    },
  },
};
</script>

<style scoped>
#container {
  display: flex;
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
  font-size: 1em;
}
h1 {
  font-size: 2em;
  color: #e50914;
  font-weight: bold;
  text-align: center;
}
p {
  margin-top: 5px;
  line-height: 150%;
  font-size: 1.05em;
   padding-left: 50px;
  padding-right: 50px;
}

.point{
  padding-left: 80px;
  padding-right: 80px;
}
th {
  font-weight: normal;
  color: white;
  font-size: 1.1em;
}
#alerter {
  color: #e50914;
}
button {
  padding: 1em;
  margin: 1em;
  border-radius: 4px;
  background-color: #404040;
  font-size: 1em;
  border: none;
  color: white;
  cursor: pointer;
}
.fakeButton {
  width: 7em;
  height: 3em;
  font-size: 2em;
}
.fakeButton:hover {
  background-color: darkgray;
}
#hiddenButton {
  margin: 0;
  font: inherit;
  font-style: italic;
  background: none;
  color: inherit;
  border: none;
  padding: 0;
  cursor: pointer;
  outline: inherit;
  text-decoration: underline;
}
.svgData {
  height: 6em;
  width: 6em;
  color: white;
}
</style>
