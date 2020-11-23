<template>
  <div id="container">
    <div class="Survey" v-if="surveyState != false">
      <div class="textBox">
        <h1>Final Questionnaire</h1>
        <p>
          As a final step, please fill out the questionnaire below. "*" denotes
          required fields
        </p>
      </div>

      <div class="selectField">
        <h2>1. To what degree do you agree with the following statements? *</h2>
        <transition name="fade">
          <div class="errorMessage" v-if="errors.rows == true">
            <p>Please answer every question to continue.</p>
          </div>
        </transition>

        <table class="mainTable">
          <tr>
            <td></td>
            <td>Completely<br />Disagree(1)</td>
            <td>(2)</td>
            <td>(3)</td>
            <td>(4)</td>
            <td>Completely<br />Agree(5)</td>
          </tr>

          <!--System experience Questions -->
          <tr class="row" v-for="data in system_related" v-bind:key="data.id">
            <td class="textField">{{ data.text }}</td>
            <td>
              <input type="radio"
                class="radio"
                value="1"
                v-model="data.value"/>
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="2"
                v-model="data.value"/>
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="3"
                v-model="data.value"/>
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="4"
                v-model="data.value"/>
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="5"
                v-model="data.value"/>
            </td>
          </tr>

          <!--Process experience Questions -->
          <tr class="row" v-for="data in process_related" v-bind:key="data.id">
            <td class="textField">{{ data.text }}</td>
            <td>
              <input
                type="radio"
                class="radio"
                value="1"
                v-model="data.value"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="2"
                v-model="data.value"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="3"
                v-model="data.value"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="4"
                v-model="data.value"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="5"
                v-model="data.value"
              />
            </td>
          </tr>
          
          <!--Attention Check -->
          <tr class="row" v-for="data in attention_check" v-bind:key="data.id">
            <td class="textField">{{ data.text }}</td>
            <td>
              <input
                type="radio"
                class="radio"
                value="1"
                v-model="data.value"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="2"
                v-model="data.value"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="3"
                v-model="data.value"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="4"
                v-model="data.value"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="5"
                v-model="data.value"
              />
            </td>
          </tr>

          <!--Outcome experience Questions -->
          <tr class="row" v-for="data in outcome_related" v-bind:key="data.id">
            <td class="textField">{{ data.text }}</td>
            <td>
              <input
                type="radio"
                class="radio"
                value="1"
                v-model="data.value"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="2"
                v-model="data.value"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="3"
                v-model="data.value"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="4"
                v-model="data.value"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="5"
                v-model="data.value"
              />
            </td>
          </tr>
        </table>

        <p></p>

        <!-- Selection inputs -->
        <div class="selectField">
          <h2>
            2. Which of the following statements best describes your use of
            online movie services (e.g, Netflix, IMDB, etc.)? *
          </h2>
          <transition name="fade">
            <div class="errorMessage" v-if="errors.usage == true">
              <p>Please answer the question to continue.</p>
            </div>
          </transition>
          <div class="selecter">
            <label>
              <select
                class="menu"
                v-model="surveyQuestions.q_dem_onlineUsage"
                placeholder="Chose..."
              >
                <option value="1">Daily</option>
                <option value="2">Once a week</option>
                <option value="2">Once a month</option>
                <option value="3">Every three months</option>
                <option value="4">Hardly use them</option>
              </select>
            </label>
          </div>
        </div>

        <div class="selectField">
          <h2>3. On average, on how many days per week do you watch a movie? *</h2>
          <transition name="fade">
            <div class="errorMessage" v-if="errors.movies == true">
              <p>Please answer the question to continue.</p>
            </div>
          </transition>
          <div class="selecter">
            <label>
              <select
                class="menu"
                v-model="surveyQuestions.q_dem_movieUsage"
                placeholder="Chose..."
              >
                <option value="0">0</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
              </select>
            </label>
          </div>
        </div>

        <div class="selectField">
          <h2>4. Your age: *</h2>
          <transition name="fade">
            <div class="errorMessage" v-if="errors.age == true">
              <p>Please answer the question to continue.</p>
            </div>
          </transition>
          <input
            type="number"
            id="ageBox"
            v-model="surveyQuestions.q_dem_age"
            placeholder="..."
            style="font-size: 1.3em; text-align: left;"
          />
        </div>

        <div class="selectField">
          <h2>5. Your gender: *</h2>
          <transition name="fade">
            <div class="errorMessage" v-if="errors.gender == true">
              <p>Please answer the question</p>
            </div>
          </transition>
          <div class="selecter">
            <label>
              <select v-model="surveyQuestions.q_dem_gender">
                <option>Male</option>
                <option>Female</option>
                <option>Other</option>
              </select>
            </label>
          </div>
        </div>

        <div class="selectField">
          <h2>6. General comments: </h2>
          <transition name="fade">
            <div class="errorMessage" v-if="errors.q_comment == true">
              <p>Please answer the question</p>
            </div>
          </transition>
          <textarea
            id="commentBox"
            v-model="surveyQuestions.comment"
            style="width: 99%; height:100px; font-size: 1.3em;"
            placeholder="..."
          ></textarea>
        </div>
      </div>

      <!-- Input and main errors -->
      <div class="selectField">
        <transition name="fade">
          <div class="errorMessage" v-if="surveyState == true">
            <p>Some required fields are missing. Please see errors above.</p>
          </div>
        </transition>
        <button @click="clickedButton">Complete</button>
        <button @click="checkValue" v-if="this.$parent.debug">
          checkValue
        </button>
      </div>
    </div>

    <!-- Finished screen -->
    <div class="textBox" v-if="surveyState == false">
      <h2>
        Survey is complete. Thank you for your participation. Please, copy and
        paste the code below to Amazon Mechanical Turk in order to obtain your
        payment for this HIT!
      </h2>
      <h1>{{ this.$parent.sessionId }}</h1>
    </div>
  </div>
</template>

<script>
import PostService from "../SearchService";
export default {
  name: "Survey",
  data() {
    return {
      //General variables
      surveyState: undefined,
      startTime: undefined,
      clickable: true,

      //Error specific variables
      errors: {
        rows: undefined,
        usage: undefined,
        movies: undefined,
        age: undefined,
        gender: undefined,
        comment: undefined,
      },
      //General data variables from some inputs and other logged features
      surveyQuestions: {
        q_dem_onlineUsage: undefined,
        q_dem_movieUsage: undefined,
        q_dem_age: undefined,
        q_dem_gender: undefined,
        q_comment: undefined,
        v_surveyTime: undefined,
        v_totalTime: undefined,
        v_attention2: undefined,
        questions: undefined,
      },

      //SuS questions
      system_related: [
        {
          id: 1,
          text: "I think that I would like to use this system frequently.",
          value: undefined,
          tag: "q_sys_freqUse",
        },
        {
          id: 2,
          text: "I found the system unnecessarily complex.",
          value: undefined,
          tag: "q_sys_complex",
        },
        {
          id: 3,
          text: "I thought the system was easy to use.",
          value: undefined,
          tag: "q_sys_easeUse",
        },
        {
          id: 4,
          text: "I think that I would need the support of a technical person to be able to use this system.",
          value: undefined,
          tag: "q_sys_techNeed",
        },
        {
          id: 5,
          text: "I found the various functions in this system well integrated.",
          value: undefined,
          tag: "q_sys_funcInteg",
        },
        {
          id: 6,
          text: "I thought there was too much inconsistency in this system",
          value: undefined,
          tag: "q_sys_inconsist",
        },
        {
          id: 7,
          text: "I would imagine that most people would learn to use this system very quickly.",
          value: undefined,
          tag: "q_sys_learnUse",
        },
        {
          id: 8,
          text: "I found the system very cumbersome to use.",
          value: undefined,
          tag: "q_sys_cumbUse",
        },
        {
          id: 9,
          text: "I felt very confident using the system.",
          value: undefined,
          tag: "q_sys_confUse",
        },
        {
          id: 10,
          text: "I needed to learn a lot of things before I could get going with this system.",
          value: undefined,
          tag: "q_sys_learnToUse",
        },
      ],

      //General survey questions for all conditions
        process_related: [
        {
          id: 11,
          text: "Searching for similar movies took a lot of time.",
          value: undefined,
          tag: "q_proc_searchSim",
        },
        {
          id: 12,
          text: "Deciding between a large number of options was difficult.",
          value: undefined,
          tag: "q_proc_decidDiff",
        },

        {
          id: 13,
          text: "The recommendations improved over time.",
          value: undefined,
          tag: "q_proc_recImprove",
        },
        {
          id: 14,
          text: "I felt in control of the recommendations.",
          value: undefined,
          tag: "q_proc_control",
        },
        {
          id: 15,
          text: "The sorting functions were useful.",
          value: undefined,
          tag: "q_proc_sorting",
        },
      ],
      attention_check: [
        {
          id: 16,
          text: "Fill in on the scale the answer to 'one plus two'.",
          value: undefined,
          tag: "c_attention2",
        }
      ],
      // Questions for only the last set of conditions
      outcome_related: [
        {
          id: 17,
          text: "The movies presented to me were diverse.",
          value: undefined,
          tag: "q_outc_diversity",
        },
        {
          id: 18,
          text: "I was able to discover new movies.",
          value: undefined,
          tag: "q_outc_novelty",
        },
        {
          id: 19,
          text: "I was pleasantly suprised by the recommendations.",
          value: undefined,
          tag: "q_outc_serendipity",
        },
        {
          id: 20,
          text:"All of the presented movies were similar to my reference movies.",
          value: undefined,
          tag: "q_outc_relevance",
        },
      ],
    };
  },
  //logs time at component creation
  created() {
    this.startTime = Date.now();
  },

  methods: {
    //Updates database generic function
    async updateStuff(field, value) {
      //Id - Field -Value
      await PostService.genericUpdate(this.$parent.sessionId, field, value);
    },

    //formats data for storage in database.
    endSession() {
      this.surveyState = false;
      this.generateReport();
      this.surveyQuestions.v_surveyTime = parseFloat(Math.abs((Date.now() - this.startTime) / 1000).toFixed(2));
      this.surveyQuestions.v_totalTime = parseFloat(Math.abs((Date.now() - this.$parent.timeStart) / 1000).toFixed(2));
      this.surveyQuestions.q_dem_age = parseInt(this.surveyQuestions.q_dem_age);
      this.surveyQuestions.q_dem_movieUsage = parseInt(this.surveyQuestions.q_dem_movieUsage);
      this.surveyQuestions.q_dem_onlineUsage = parseInt(this.surveyQuestions.q_dem_onlineUsage
      );

      if (this.$parent.debugState) {
        console.log("Results of survey and other finishing variables");
        console.log(this.surveyQuestions);
      }
      this.updateStuff("surveyResults", this.surveyQuestions);
    },

    //Button handling
    clickedButton() {
      this.clickable = false;
      if (this.validate()) {
        this.endSession();
      }
      else{
        this.clickable = true
      }
    },
    //Checks if all questions are answered. Formats variables based on where questions are missing to activate location based error messages
    validate() {
      var rowError = undefined;
      var rerun = true;
      //Likert Questionaire groups
      for (var i in this.system_related) {
        if (this.system_related[i].value == undefined) {
          rowError = true;
          break;
        }
      }

      for (var j in this.process_related) {
        if (this.process_related[j].value == undefined) {
          rowError = true;
          break;
        }
      }

      for (var k in this.outcome_related) {
        if (this.outcome_related[k].value == undefined) {
          rowError = true;
          break;
        }
      }

      if (rowError == true) {
        this.errors.rows = true;
        rerun = false;
      } else {
        this.errors.rows = undefined;
      }
            console.log("pass 2" + rerun)
      //Demograhpic question check
      if (this.surveyQuestions.q_dem_onlineUsage == undefined) {
        this.errors.usage = true;
        rerun = false;
      } else {
        this.errors.usage = undefined;
      }

      if (this.surveyQuestions.q_dem_movieUsage == undefined) {
        this.errors.movies = true;
        rerun = false;
      } else {
        this.errors.movies = undefined;
      }

      if (this.surveyQuestions.q_dem_age == undefined) {
        this.errors.age = true;
        rerun = false;
      } else {
        this.errors.age = undefined;
      }

      if (this.surveyQuestions.q_dem_gender == undefined) {
        this.errors.gender = true;
        rerun = false;
      } else {
        this.errors.gender = undefined;
      }
      console.log("pass 3" + rerun)
      if (rerun == false) {
        this.surveyState = true;
      }
      return rerun;
    },

    //format questions for database entry
    generateReport() {
      var response = {};
      for (var x in this.system_related) {
        response[this.system_related[x].tag] = parseInt(this.system_related[x].value);
      }
      for (var y in this.process_related) {
        response[this.process_related[y].tag] = parseInt(this.process_related[y].value);
      }
      for (var z in this.outcome_related) {
        response[this.outcome_related[z].tag] = parseInt(this.outcome_related[z].value);
      }

      if (this.attention_check[0].value == 3) {
            this.surveyQuestions.v_attention2 = true;
      } else {
            this.surveyQuestions.v_attention2 = false;
      }
      this.surveyQuestions.questions = response;
    },
  },
};
</script>

<style scoped>
/*General styling */
#container {
  display: flex;
  justify-content: center;
}
.Survey {
  max-width: 1300px;
}
.textBox {
  background-color: black;
  border-style: solid;
  border-width: 2px;
  border-color: white;
  padding: 10px;
}
p,
h1 {
  color: white;
  font-size: 1.25em;
  text-align: left;
  white-space: pre-line;
  text-align: center;
}
h1 {
  font-size: 3em;
  color: red;
}
button {
  padding: 1em;
  margin: 1em;
  border-radius: 4px;
  background-color: red;
  font-size: 1.5em;
  border: none;
  color: white;
  cursor: pointer;
  width: 20%;
}
button:hover {
  background-color: #f2848f;
  transition: 0.3s;
}
h2 {
  color: white;
}
/* Table and input styling*/
.selectField {
  background-color: black;
  color: white;
  border-top: 2px solid red;
}
table {
  border-collapse: collapse;
}
tr {
  border-bottom: 1px solid white;
}
tr:nth-child(even) {
  background-color: #292827;
}
td {
  padding-top: 5px;
  padding-bottom: 5px;
  width: 10%;
  word-break: normal;
}
td:first-child {
  width: 30%;
}
.textField {
  word-break: normal;
  text-align: start;
  padding-left: 5px;
}
select {
  width: 100%;
  font-size: 1.3em;
}
input {
  width: 100%;
}
#commentBox {
  resize: vertical;
}
input {
  height: 2em;
  width: 100%;
  text-align: center;
}
select {
  height: 2em;
  width: 100%;
}
input[type="radio"]:after {
  right: 5px;
  width: 1.6em;
  height: 1.6em;
  border-radius: 15px;
  position: relative;
  background-color: #d1d3d1;
  content: "";
  display: inline-block;
  visibility: visible;
  border: 2px solid white;
  -moz-appearance: none !important;
}
input[type="radio"]:checked:after {
  width: 1.6em;
  height: 1.6em;
  border-radius: 15px;
  position: relative;
  background-color: #f7200c;
  content: "";
  display: inline-block;
  visibility: visible;
  border: 2px solid white;
  -moz-appearance: none !important;
}

/*Compability CSS since radio buttons really are a struggle */
.radio {
  height: 1.5em;
  visibility: hidden;
  -moz-appearance: none; /*Firefox Compatability check */
}
/*Edge Support */
@supports (-ms-ime-align: auto) {
  .radio {
    visibility: visible;
  }
}
/*Internet Explorer 10 and 11 radio button finishes */
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
  .radio {
    visibility: visible !important;
  }
}
/*Error styling */
.errorMessage {
  background-color: #fcdfe2;
  border-style: solid;
  border-width: 2px;
  border-color: #f2848f;
  box-sizing: inherit;
  margin-bottom: 15px;
}
.errorMessage p {
  color: #f2848f;
  display: inline-block;
}
button {
  padding: 1em;
  margin: 1em;
  border-radius: 4px;
  background-color: red;
  font-size: 1.5em;
  border: none;
  color: white;
  cursor: pointer;
  width: 20%;
}

button:hover {
  background-color: #f2848f;
  transition: 0.3s;
}
h2 {
  color: white;
}
</style>
