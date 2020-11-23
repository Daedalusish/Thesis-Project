<!--This is condition 1A. This condition has no controll elements, and list order is randomized in every itteration. -->
<template>
  <div id="container">
    <div class="Browse">
      <!--Loading Spinner -->
      <transition name="fade">
        <div id="loading" v-if="searching" mode="out-in">
          <div class="lds-roller">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
          </div>
        </div>
      </transition>

      <!--Instructions for condition 1-3 -->
      <div class="textBox" v-if="[1, 2, 3].includes(this.$parent.condition)">
        <!--Condition 1-3 -->
        <div class="headerText">
          <h1>Ordering Recommendations Provided</h1>
          <h1>Step {{ this.$parent.itteration }} of 5</h1>
        </div>
        <p id="help">
          Based on the movie you selected as a reference movie in the previous
          step, which is shown directly below, several sets of recommendations
          are presented. Please inspect the recommendation lists below and rate
          how the selection as a whole is ranked from top to bottom. Top ranking
          indicates that the selection has many movies you find similar. When
          done, select a movie that you would like to watch by hovering over
          one. Your selection will influence future recommendations.
        </p>

        <p />
      </div>

      <!--Instructions for condition 4-6 -->
      <div class="textBox" v-if="[4, 5, 6].includes(this.$parent.condition)">
        <!--Condition 4-6 -->
        <div class="headerText">
          <h1>Ordering Recommendations Provided</h1>
          <h1>Step {{ this.$parent.itteration }} of 5</h1>
        </div>
        <p id="help">
          Based on the movie you selected as a reference movie in the previous
          step, which is shown directly below, several sets of recommendations
          are presented. Please inspect the recommendation lists below and rate
          how the selection as a whole is ranked from top to bottom. Top ranking
          indicates that the selection has many movies you find similar. After
          rating, you may now reorder the lists to your preference. This can be
          done by dragging the handle icon "
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
          </svg>
          " or by clicking the arrows to move one position at the time. When
          done, select a movie that you would like to watch by hovering over
          one. The movie you select and your ordering of the lists will
          influence future recommendations.
        </p>

        <p />
      </div>

      <!-- Renders reference movie information -->
      <div id="metaContainer" v-if="!searching">
        <div id="textContainer">
          <h2>Your Reference Movie:</h2>
          <h3>{{ movies[0]["Metadata"].Title }}</h3>
          <p style="font-weight: bold;">{{ movies[0]["Metadata"].Release }}</p>
          <p class="metaText">{{ movies[0]["Metadata"].Overview }}</p>
          <p class="metaText">Stars: {{ movies[0]["Metadata"].Actors }}</p>
          <p class="metaText">
            Director: {{ movies[0]["Metadata"].Directors }}
          </p>
          <p class="metaText">Genres: {{ movies[0]["Metadata"].Genres }}</p>
        </div>
        <div id="imageContainer">
          <div style="width:45%; height:100%;"></div>
          <div
            id="metaHeader"
            :style="getImgStyle(movies[0]['Metadata'].Cover_Path)"
          ></div>
        </div>
      </div>

      <!--Zoom Button and list learning question-->
      <div id="metaContainer" style="justify-content: space-between;">
        <p id="infoText" style="margin-top: auto; margin-bottom:auto">
          Please report on a scale from very unsatisfied (1) to very satisfied
          (5)<br />on how you happy you are with the current list order, from
          top to bottom.
        </p>
        <table class="mainTable" align="right">
          <tr class="row">
            <td>Very<br />Unsatisfied<br />1</td>
            <td>
              <span class="noselect hidden">2</span><br /><span
                class="noselect hidden"
                >2</span
              ><br />2
            </td>
            <td>
              <span class="noselect hidden">3</span><br /><span
                class="noselect hidden"
                >3</span
              ><br />3
            </td>
            <td>
              <span class="noselect hidden">4</span><br /><span
                class="noselect hidden"
                >4</span
              ><br />4
            </td>
            <td>Very<br />Satisfied<br />5</td>
          </tr>
          <tr class="row">
            <td>
              <input
                type="radio"
                class="radio"
                value="1"
                v-model="satisfactionScore"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="2"
                v-model="satisfactionScore"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="3"
                v-model="satisfactionScore"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="4"
                v-model="satisfactionScore"
              />
            </td>
            <td>
              <input
                type="radio"
                class="radio"
                value="5"
                v-model="satisfactionScore"
              />
            </td>
          </tr>
        </table>
      </div>

      <transition name="fade">
        <div class="errorMessage" v-if="satisfactionError">
          <p>Please answer this question before you continue</p>
        </div>
      </transition>

      <button v-on:click="zoom" class="zoomButton">
        <transition name="fade" mode="out-in">
          <div v-bind:key="zoomState">
            {{ zoomState ? "Normalize" : "Zoom Out" }}
          </div>
        </transition>
      </button>

      <div>
        <h1 style="color:white">
          Here are your movie recommendations, based on...
        </h1>
      </div>

      <!--Renders without controll elements, IE conditions 1-3. Recommendations sorted into list without control elements  -->
      <div
        class="recContainer"
        v-if="[1, 2, 3].includes(this.$parent.condition)"
        v-bind:style="
          zoomState
            ? 'transform: scale(0.5); display: block; transition: all 1s;'
            : 'transform: scale(1.0); transition: all 1s;'
        "
      >
        <div
          class="list"
          v-for="(list, name) in similarities"
          v-bind:item="list"
          v-bind:key="name"
        >
          <div style="display: flex; flex-direction:column;">
            <p class="titleHeader" v-if="list[0] == 'Baseline'">
              Miscellaneous
            </p>
            <p class="titleHeader" v-if="list[0] == 'SVD'">
              Community preferences
            </p>
            <p
              class="titleHeader"
              v-if="list[0] != 'Baseline' && list[0] != 'SVD'"
            >
              {{ list[0] }}
            </p>

            <div class="listContainer">
              <div
                class="filmSet"
                v-for="(filmSet, index) in cut(list[1])"
                v-bind:item="filmSet"
                v-bind:key="index"
              >
                <div class="filmContainer">
                  <img class="test" :src="getPicUrl(filmSet.Cover_Path)" />

                  <div class="tooltip">
                    <div class="toolContainer">
                      <p class="tooltipText noselect">placeholder</p>
                      <p class="tooltipText">{{ filmSet.Title }}</p>
                      <p class="tooltipText">
                        ( {{ filmSet.Release.substring(0, 4) }} )
                      </p>
                      <p id="tooltipOverview">
                        {{ filmSet.Overview.substring(0, 90) }}...
                      </p>
                      <button
                        class="btnconf"
                        v-on:click="checkIfEnd(filmSet.MovieLensID, list[0])"
                      >
                        Watch Later
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Renders with control elements IF conditions are 4-6 -->
      <div
        class="recContainer"
        v-if="[4, 5, 6].includes(this.$parent.condition)"
        v-bind:style="
          zoomState
            ? 'transform: scale(0.5); display: block; transition: all 1s;'
            : 'transform: scale(1.0); transition: all 1s;'
        "
      >
        <draggable
        :disabled = freeze
          v-bind="dragOptions"
          v-model="similarities"
          swapThreshold="1"
          dragClass="dragging"
          direction="horizontal"
          invertSwap="false"
          class="biggerArea"
          animation="200"
          handle=".handle"
          @change="checkMove($event)"
        >
          <div
            class="list"
            v-for="(list, index, name) in similarities"
            v-bind:item="list"
            :key="name"
          >
            <!--Temporary duplicate based on placement -->
            <div class="listContainer">
              <div class="sortNavigation">
                <button class="navBtn arrowUp" v-on:click="navUp(index)">
                  <svg
                    aria-hidden="true"
                    focusable="false"
                    data-prefix="fas"
                    data-icon="chevron-up"
                    class="arrowSvg arrowUp"
                    role="img"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 448 512"
                  >
                    <path
                      fill="currentColor"
                      d="M240.971 130.524l194.343 194.343c9.373 9.373 9.373 24.569 0 33.941l-22.667 22.667c-9.357 9.357-24.522 9.375-33.901.04L224 227.495 69.255 381.516c-9.379 9.335-24.544 9.317-33.901-.04l-22.667-22.667c-9.373-9.373-9.373-24.569 0-33.941L207.03 130.525c9.372-9.373 24.568-9.373 33.941-.001z"
                    ></path>
                  </svg>
                </button>
                <svg
                  aria-hidden="true"
                  focusable="false"
                  data-prefix="fas"
                  data-icon="arrows-alt-v"
                  class="handle"
                  role="img"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 256 512"
                >
                  <path
                    fill="currentColor"
                    d="M214.059 377.941H168V134.059h46.059c21.382 0 32.09-25.851 16.971-40.971L144.971 7.029c-9.373-9.373-24.568-9.373-33.941 0L24.971 93.088c-15.119 15.119-4.411 40.971 16.971 40.971H88v243.882H41.941c-21.382 0-32.09 25.851-16.971 40.971l86.059 86.059c9.373 9.373 24.568 9.373 33.941 0l86.059-86.059c15.12-15.119 4.412-40.971-16.97-40.971z"
                  ></path>
                </svg>
                <button class="navBtn arrowDown" v-on:click="navDown(index)">
                  <svg
                    aria-hidden="true"
                    focusable="false"
                    data-prefix="fas"
                    data-icon="chevron-down"
                    class="arrowSvg arrowDown"
                    role="img"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 448 512"
                  >
                    <path
                      fill="currentColor"
                      d="M207.029 381.476L12.686 187.132c-9.373-9.373-9.373-24.569 0-33.941l22.667-22.667c9.357-9.357 24.522-9.375 33.901-.04L224 284.505l154.745-154.021c9.379-9.335 24.544-9.317 33.901.04l22.667 22.667c9.373 9.373 9.373 24.569 0 33.941L240.971 381.476c-9.373 9.372-24.569 9.372-33.942 0z"
                    ></path>
                  </svg>
                </button>
              </div>
              <!--Movie loop -->
              <div style="display: flex; flex-direction:column;">
                <p class="titleHeader" v-if="list[0] == 'Baseline'">
                  Miscellaneous
                </p>
                <!-- Quick switch so that baseline is not viewed as such to participants -->
                <p class="titleHeader" v-if="list[0] == 'SVD'">
                  Community Preferences
                </p>
                <p
                  class="titleHeader"
                  v-if="list[0] != 'Baseline' && list[0] != 'SVD'"
                >
                  {{ list[0] }}
                </p>
                <div style="display: flex; flex-direction:row;">
                  <div
                    class="filmSet"
                    v-for="(filmSet, Id) in cut(list[1])"
                    v-bind:item="filmSet"
                    v-bind:key="Id"
                  >
                    <div class="filmContainer">
                      <img class="test" :src="getPicUrl(filmSet.Cover_Path)" />

                      <div class="tooltip">
                        <div class="toolContainer">
                          <p class="tooltipText noselect">placeholder</p>
                          <p class="tooltipText">{{ filmSet.Title }}</p>
                          <p class="tooltipText">
                            ( {{ filmSet.Release.substring(0, 4) }} )
                          </p>
                          <p id="tooltipOverview">
                            {{ filmSet.Overview.substring(0, 90) }}...
                          </p>
                          <button
                            class="btnconf"
                            v-on:click="
                              checkIfEnd(filmSet.MovieLensID, list[0])
                            "
                          >
                            Watch Later
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </draggable>
      </div>
    </div>
  </div>
</template>

<script>
import PostService from "../SearchService";
import draggable from "vuedraggable";

export default {
  components: {
    draggable,
  },
  /*Local Variables */
  data() {
    return {
      freeze: true,
      id: this.$route.params.id,
      movies: [],
      similarities: [],
      errors: "",
      text: "",
      listOrder: [],
      initialOrderF: [],
      finalOrderF: [],
      moveDistanceD: 0,
      moveDistanceC: 0,
      moveDistanceA: 0,
      dragCount: 0,
      clickCount: 0,
      totalCount: 0,
      browseStart: undefined,
      searching: true,
      zoomState: false,
      zoomCounter: 0,
      satisfactionScore: undefined,
      satisfactionError: undefined,
      clickable: true,

      greekState: false,
      titleState: false,
      indexState: false,
      placement: false,
    };
  },
  computed: {
    //config for scrolling variables while dragging
    dragOptions() {
      return {
        scrollSensitivity: "200",
        forceFallback: true,
        scrollSpeed: "30",
      };
    },
  },
  watch:{
    satisfactionScore: function(){
      this.rated()
    }
  },
  /* Starts when view is initialized. Retrieves recommender lists based on movie selected. Shuffles afterwards */
  async created() {
    try {
      this.movies = await PostService.getSims(this.id);

      if (this.$parent.debugState) {
        console.log("Data collected from the database:");
        console.log(this.movies);
      }
      const temp = this.movies[0]["Similarities"];
      this.browseStart = Date.now();
      this.trimOutput();
      this.similarities = Object.keys(temp).map((key) => {
        return [String(key), temp[key]];
      });
    } catch (err) {
      console.log(err.message);
    }

    /*Sort list if randomised conditions OR first itteration. condition 1 and 4*/
    if (
      [1, 4].includes(this.$parent.condition) ||
      this.$parent.itteration == 1
    ) {
      this.similarities = this.shuffle(this.similarities);
    }

    //Sets list order to the order at the end of the previous itteration. Condition 2 and 5
    else if ([2, 5].includes(this.$parent.condition)) {
      this.similarities = this.prevOrder();
    }

    //sorts list order based on weights from previous itterations. Condition 3 and 6
    else if ([3, 6].includes(this.$parent.condition)) {
      this.applyWeights();
    }
    this.searching = false;
    this.initialOrderF = this.trimList(this.similarities);
  },

  methods: {
    rated(){
      this.freeze = false
      this.satisfactionError = false
    },

    //Logs number of drags and how far it was dragged
    zoom() {
      this.zoomState = !this.zoomState;
      this.zoomCounter++;
      console.log(this.similarities);
    },

    //Logic and logging of navbutton up
    navUp(index) {
      if(this.freeze != true){
      var currentPos = this.similarities[index];
      var abovePos = this.similarities[index - 1];
      this.similarities[index - 1] = currentPos;
      this.similarities[index] = abovePos;
      this.clickCount = this.clickCount + 1;
      this.totalCount = this.totalCount + 1;
      this.moveDistanceA = this.moveDistanceA + 1;
      this.moveDistanceC = this.moveDistanceC + 1;
      this.$forceUpdate();
      }else{
        this.satisfactionError = true;
      }
    },

    //Logic and logging of navbutton down
    navDown(index) {
      if(this.freeze != true){
        var currentPos = this.similarities[index];
        var belowPos = this.similarities[index + 1];
        this.similarities[index + 1] = currentPos;
        this.similarities[index] = belowPos;
        this.clickCount = this.clickCount + 1;
        this.totalCount = this.totalCount + 1;
        this.moveDistanceA = this.moveDistanceA + 1;
        this.moveDistanceC = this.moveDistanceC + 1;
        this.$forceUpdate();
      }
      else{
        this.satisfactionError = true;
      }
    },

    // Logs usage of drag & drop
    checkMove(evt) {
      this.dragCount = this.dragCount + 1;
      this.totalCount = this.totalCount + 1;
      this.moveDistanceD =
        this.moveDistanceD +
        parseInt(
          Math.abs(parseInt(evt.moved.oldIndex) - parseInt(evt.moved.newIndex))
        );
      this.moveDistanceA =
        this.moveDistanceA +
        parseInt(
          Math.abs(parseInt(evt.moved.oldIndex) - parseInt(evt.moved.newIndex))
        );
    },

    //formats the metadata into something more viewable
    trimOutput() {
      var source = this.movies[0]["Metadata"];
      this.movies[0]["Metadata"].Release =
        "(" + source.Release.substring(0, 4) + ")";
      var actorlist = source.Actors.split(",");
      var actorString = "";

      if (actorlist.length < 4) {
        for (var i in actorlist) {
          if (i == 0) {
            actorString = actorlist[i];
          } else {
            actorString = actorString.concat(", " + actorlist[i]);
          }
        }
      } else {
        for (var x = 0; x < 4; x++) {
          if (x == 0) {
            actorString = actorlist[x];
          } else {
            actorString = actorString.concat(", " + actorlist[x]);
          }
        }
      }
      this.movies[0]["Metadata"].Actors = actorString;
    },
    /* Sets order to previous itterations order, used by condition 2 and 5*/
    prevOrder() {
      const previousOrder = this.$parent.globalList[
        this.$parent.itteration - 2
      ];
      const tempOrder = [];

      //special handling needed for condition 2
      if (this.$parent.condition == 2 || this.$parent.condition == 5) {
        for (var p = 0; p < this.similarities.length; p++) {
          if (this.$parent.previousSelectedList == this.similarities[p][0]) {
            tempOrder.push(this.similarities[p]);
            break;
          }
        }
      }
      for (var x = 0; x < previousOrder.length; x++) {
        for (var y = 0; y < this.similarities.length; y++) {
          if (previousOrder[x] == this.similarities[y][0]) {
            if (this.similarities[y][0] !== this.$parent.previousSelectedList) {
              tempOrder.push(this.similarities[y]);
              break;
            }
          }
        }
      }
      return tempOrder;
    },

    /* Fisher-Yates shuffle of the lists for randomization */
    shuffle(arr) {
      var i, j, temp;
      for (i = arr.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }
      return arr;
    },

    //"Hey i'm going to include 10 movies in the dataset what a good idea it is probably super easy to limit output later".fix
    cut(object) {
      const treated = Object.keys(object).map((key) => {
        return [String(key), object[key]];
      });
      var halfSplit = {};
      for (var i = 0; i < 5; i++) {
        halfSplit[i] = treated[i][1];
      }
      return halfSplit;
    },

    //These two exist because vue is a real bitch with dynamic paths in the build
    getImgStyle(url) {
      const imagePath = this.getPicUrl(url);
      const anotherOne = `url(" ` + imagePath + `")`;
      return { "background-image": anotherOne };
    },
    getPicUrl(url) {
      return require("../assets/posters" + url);
    },

    /*Update database with values. postService params:  Id - Field - Value */
    async updateStuff(field, value) {
      await PostService.genericUpdate(this.$parent.sessionId, field, value);
    },

    /*Generate a list containing current order of the recs. Index = position, name = name */
    getListOrder() {
      for (var i = 0; i < this.similarities.length; i++) {
        this.listOrder.push(this.similarities[i][0]);
      }
      this.finalOrderF = this.similarities[i];
    },

    /* finds position of the list which the movie was selected from */
    getPosition(target) {
      for (var j = 0; j < this.listOrder.length; j++) {
        if (this.listOrder[j] == target) {
          return j;
        }
      }
    },

    //Apply weights based on order
    createWeights(selectedList) {
      var listObject = [];
      var temp = [];
      for (var a in this.listOrder) {
        if (a == 0) {
          temp.push(selectedList);
        }
        if (this.listOrder[a] != selectedList) {
          temp.push(this.listOrder[a]);
        }
      }
      this.listOrder = temp;

      for (var y in this.listOrder) {
        listObject[y] = {
          list: this.listOrder[y],
          value: (this.listOrder.length - y) / 10,
        };
      }
      this.$parent.weightList = listObject;

      if (this.$parent.debugState) {
        console.log("created weights");
        console.log(this.$parent.weightList);
      }
    },

    //trimming list for storage
    trimList(object) {
      var storage = [];
      for (var i in object) {
        var tempStorage = [];
        tempStorage.push(object[i][0]);
        tempStorage.push(this.cut(object[i][1]));
        storage.push(tempStorage);
      }
      return storage;
    },

    //Applies weights based on previous itterations
    updateWeights(selectedList) {
      var temp = [];
      for (var x in this.listOrder) {
        if (x == 0) {
          temp.push(selectedList);
        }
        if (this.listOrder[x] != selectedList) {
          temp.push(this.listOrder[x]);
        }
      }
      this.listOrder = temp;
        for (var b in this.listOrder) {
          for (var a in this.$parent.weightList) {
            if (this.$parent.weightList[a].list == this.listOrder[b]) {
              this.$parent.weightList[a].value = parseFloat(
                (
                  this.$parent.weightList[a].value +
                  (this.listOrder.length - b) / 10
                ).toFixed(2)
              );
              break;
            }
          }
      }
      this.$parent.weightList = this.$parent.weightList.sort((a, b) =>
        a.value < b.value ? 1 : -1
      );
    },

    //Uses the weights to sort the list
    applyWeights() {
      var sortedSim = [];
      for (var x in this.$parent.weightList) {
        for (var y in this.similarities) {
          if (this.$parent.weightList[x].list == this.similarities[y][0]) {
            sortedSim.push(this.similarities[y]);
            break;
          }
        }
      }
      this.similarities = sortedSim;
    },

    //get current time
    getTime() {
      return Math.abs((Date.now() - this.browseStart) / 1000).toFixed(2);
    },

    //Checks if satisfaction question is answered in order to promt an error or continue end of browsing operations
    checkIfEnd(movieId, selectedList) {
      if (this.clickable) {
        this.clickable = false;
        if (this.satisfactionScore != undefined) {
          this.endSession(movieId, selectedList);
        } else {
          this.satisfactionError = true;
          this.clickable = true;
          return false;
        }
      }
    },

    /*Browsing end handler. Writes activity to database, then determines what path to chose based on itteration state. */
    endSession(MovieId, selectedList) {
      this.getListOrder();
      this.$parent.previousSelectedList = selectedList;
      if ([3, 6].includes(this.$parent.condition)) {
        if (this.$parent.itteration == 1) {
          this.createWeights(selectedList);
        } else {
          this.updateWeights(selectedList);
        }
        console.log;
      }

      //Result field
      const result = {
        v_initialListMeta: this.initialOrderF,
        v_finalOrderF: this.trimList(this.similarities),
        v_listOrdering: this.listOrder,
        v_listSelectedFrom: selectedList,
        v_movieSelected: MovieId + ".json",
        v_moviePosition: this.getPosition(selectedList),
        v_clickCount: this.clickCount,
        v_dragCount: this.dragCount,
        v_totalCount: this.totalCount,
        v_moveDistanceA: this.moveDistanceA,
        v_moveDistanceC: this.moveDistanceC,
        v_moveDistanceD: this.moveDistanceD,
        v_browsingTime: parseFloat(this.getTime()),
        v_zoomPressed: this.zoomCounter,
        q_outc_satisfactionScore: parseInt(this.satisfactionScore),
      };

      if (this.$parent.debugState) {
        console.log("logged data from this session:");
        console.log(result);
      }
      const fieldName = "browseResult" + this.$parent.itteration;
      this.updateStuff(fieldName, result);

      //continuation handler
      if (this.$parent.itteration == 5) {
        this.$router.push({ path: "/Survey" });
      } else {
        this.$parent.globalList[this.$parent.itteration - 1] = this.listOrder;
        this.$parent.itteration = this.$parent.itteration + 1;
        this.$router.push({ path: "/search" });
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/*General */
.container {
  width: 100%;
  transition: 0.2s;
}
.Browse {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/*Zoom button */
.zoomButton {
  font-weight: bold;
  width: 10em;
  color: black;
  background-color: white;
  transition: 0.3s;
  margin-top: 5px;
  margin-bottom: 5px;
}
.zoomButton:hover {
  background-color: red;
}

/*Legend*/
.textBox {
  background-color: black;
  border-style: solid;
  border-width: 2px;
  border-color: white;
  padding: 10px;
  margin: 10px;
  max-width: 1200px;
}
p,
h1 {
  color: white;
  font-size: 1em;
  text-align: left;
  white-space: pre-line;
  margin: 5px;
}
#example {
  height: 1.2em;
}
.headerText {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
}
h1 {
  font-size: 2em;
  color: red;
}
i {
  color: white;
}

/*Reference Movie*/
.metaText {
  font-size: 1em;
  padding: 0px;
}
#metaContainer {
  background-color: black;
  border-style: solid;
  border-width: 2px;
  border-color: white;
  padding: 10px;
  display: flex;
  width: 95%;
  max-width: 1200px;
  margin: 10px;
}
#textContainer {
  width: 50%;
  min-width: 50%;
  max-width: 50%;
}
#imageContainer {
  width: 100%;
  min-width: 55%;
  min-height: 100%;
  display: flex;
}
h2 {
  color: red;
}
h3 {
  color: white;
  font-size: 3em;
}
.titleHeader {
  font-weight: bold;
  font-size: 1.5em;
}

/*List Style */
.recContainer {
  margin-top: 10px;
  width: 100%;
  transform-origin: top;
}
.list {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.listContainer {
  width: 100%;
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  justify-content: space-evenly;
  margin-bottom: 10px;
  align-items: center;
  max-width: 1224px;
}
.listInfoC {
  font-size: 1.3em;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: left;
}
.listInfoC * {
  white-space: nowrap;
  font-weight: bold;
  width: 60px;
  text-align: center;
}
.listInfoR {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  font-size: 1.5em;
}
/*Film style */
.filmSet {
  height: 100%;
  width: 100%;
  max-width: 20%;
  min-width: 15%;
  margin-left: 5px;
}
.film {
  min-height: 100%;
  min-width: 100%;
  display: flex;
  background-size: contain;
  background-repeat: no-repeat;
  color: black;
  transition: 0.3s;
  width: 100%;
  height: 0;
  padding-top: 150%;
}
#metaHeader {
  height: 100%;
  width: 100%;
  background-size: contain;
  background-repeat: no-repeat;
  color: black;
}

/*"Tooltip" */
.tooltip {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  color: white;
  opacity: 0;
  background-image: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0),
    rgba(0, 0, 0, 0.9),
    rgba(0, 0, 0, 1),
    rgba(0, 0, 0, 1)
  );
  transition: 0.3s;
}
.toolContainer {
  height: 100%;
  display: flex;
  flex-flow: column;
  align-items: center;
  justify-content: flex-end;
}
.filmContainer {
  position: relative;
  transition: 0.3s;
}
.filmContainer:hover .tooltip {
  opacity: 1;
}
.tooltipText {
  font-weight: bold;
  font-size: 1.3em;
  padding: 5px;
  margin: 0px;
}
.tooltipText:first-child {
  color: rgba(0, 0, 0, 0);
}
.tooltipText:nth-child(3) {
  font-size: 1em;
}
.tooltipOverview {
  max-height: 20%;
  max-width: 100%;
  font-size: 1em;
}
.noselect {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
button {
  padding: 1em;
  border-radius: 8px;
  background-color: #404040;
  font-size: 1em;
  border: none;
  color: white;
  display: inline-block;
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

/*Misc */
.biggerArea {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.dragging {
  visibility: hidden;
}
.subContainer {
  max-width: 1200px;
}
/*navigation elements */
.handle {
  margin: 5px;
  width: 2.3em;
  color: white;
  cursor: pointer;
  transition: 0.3s;
}
.handle:hover {
  transform: scale(1.1);
  color: grey;
}
.sortable-ghost .handle {
  color: red;
  opacity: 0.5;
}
.test {
  height: auto;
  max-height: 350px;
  width: 100%;
}
.sortNavigation {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.list:first-child .listContainer .sortNavigation .arrowUp {
  display: none;
}
.list:last-child .listContainer .sortNavigation .arrowDown {
  display: none;
}
.navBtn {
  position: relative;
  width: 1.5em;
  background: transparent;
  text-align: center;
  border-radius: 30px;
  cursor: pointer;
  position: relative;
  transition: 0.3s;
}
.arrowSvg {
  color: white;
  size: 2em;
  position: absolute;
  top: 50%;
  left: 50%;
  height: 50%;
  transform: translate(-50%, -50%);
  width: 2em;
  height: 2em;
  display: block;
  color: white;
  transition: 0.3s;
}
.arrowUp:hover {
  color: red;
  top: 35%;
  cursor: pointer;
}
.arrowDown:hover {
  color: red;
  top: 65%;
  cursor: pointer;
}
/* Table and input styling*/
table {
  table-layout: fixed;
  width: 35%;
  border-collapse: collapse;
}
td {
  padding-top: 5px;
  padding-bottom: 5px;
  width: 25%;
  word-break: normal;
  color: white;
}
input {
  width: 100%;
}
#commentBox {
  resize: vertical;
}
#infoText {
  font-size: 1.1em;
}
input {
  height: 2em;
  width: 100%;
  text-align: center;
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
  font-size: 2em;
}

.hidden {
  color: black;
}
#help{
  font-size: 1.1em;
}
</style>
