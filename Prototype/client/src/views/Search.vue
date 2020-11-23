<!--This component handles all searches for movies -->
<template>
  <div class="Search">
    <!--Legend container-->
    <div class="container">
      <div class="textBox">
        <h1>Reference Item Selection</h1>
        <h2>Step {{ this.$parent.itteration }} of 5</h2>
        <p class="info">
          Please search for and select a movie that you have watched and enjoyed
          at some point. In the following step, we show you other movies that
          might be interesting for you.
        </p>
        <p />
        <p class="info">You may not select the same movie several times.</p>
        <p class="info">
          Note that our survey system only contains a limited number of movies;
          especially newer movies might be missing. If the movie you would like
          to select is not available, please try another one.
        </p>
      </div>
    </div>

    <!--Search input container -->
    <div class="container">
      <div class="searchBox">
        <div class="searchField">
          <input
            type="text"
            id="inputField"
            v-model="text"
            v-on:keyup="keymonitor"
            autocomplete="off"
            placeholder="Search for reference movie.."
          />
          <button class="searchBtn" v-on:click="searchMovies">
            <svg
              aria-hidden="true"
              focusable="false"
              data-prefix="fas"
              data-icon="search"
              class="searchIcon"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 512 512"
            >
              <path
                fill="currentColor"
                d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z"
              ></path>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!--Load animation -->
    <transition name="fade">
      <div id="loading" v-if="searching">
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

    <!--Result Container -->
    <div>
      <transition name="fade" mode="out-in">
        <div class="wrap" v-if="prevError">
          <div class="errorMsg">
            <h1>You cannot select the same movie twice. Please try another.</h1>
          </div>
        </div>
      </transition>

      <transition name="fade" mode="out-in">
        <!--Displays message if request returned no result or server failure-->
        <div class="wrap" v-if="resultState == false || serverError == true">
          <div class="errorMsg" v-if="resultState == false" key="noResult">
            <h1>No results found for "{{ previousText }}".</h1>
            <p>Check spelling or try another movie.</p>
          </div>
          <div class="errorMsg" v-if="serverError == true" key="error">
            <h1>
              Problem processing the request, connection to server refused.
            </h1>
          </div>
        </div>

        <!--Displays movies found when searching -->
        <div v-if="resultState" class="movieContainer" key="result">
          <div
            class="movie"
            v-for="(movie, index) in movies"
            v-bind:item="movie"
            v-bind:index="index"
            v-bind:key="movie._id"
            v-bind:id="movies.Id"
          >
            <div class="poster" :style="getImgStyle(movie.Cover_Path)">
              <div class="tooltip">
                <div class="toolContainer">
                  <p class="tooltipText noselect">placeholder</p>
                  <!--If it works it's not dumb -->
                  <p class="tooltipText">{{ movie.Title }}</p>
                  <p class="tooltipText">{{ movie.Release }}</p>
                  <p id="tooltipOverview">{{ movie.Overview }}</p>
                  <button class="btnconf" v-on:click.once="checkList(movie.Id)">
                    <i class="fas fa-check"></i>Choose as<br />reference movie
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import PostService from "../SearchService";
export default {
  name: "Search",
  data() {
    return {
      //Local Variables
      movies: [],
      errors: "",
      text: "",
      resultState: undefined,
      previousText: undefined,
      searching: false,
      serverError: false,
      prevError: false,
      clickable: true,
    };
  },

  methods: {
    //Allows users to use their enter button with same functionality as search button. Check in place to disable double-click
    keymonitor: function(event) {
      if (event.key == "Enter" && this.text != this.previousText) {
        this.searchMovies();
      }
    },

    //Call to API with query. Also handles the state of DOM elements such as loading icon. Check in place to disable double-click
    async searchMovies() {
      if(this.clickable){
        this.clickable = false
        this.prevError = false;
        if (this.text !== "" && this.text != this.previousText) {
          this.searching = true;

          try {
            this.movies = await PostService.searchMovie(this.text);
            this.resultsFound();
            this.previousText = this.text;
            this.searching = false;
          } catch (err) {
            this.serverError = true;
            this.searching = false;
            console.log(err);
          }
        }
        this.clickable = true
      }
    },

    //Decides if results are found and are to be treated, or do display empty result warning
    resultsFound() {
      if (this.movies.length == 0) {
        this.previousText = this.text;
        this.resultState = false;
      } else {
        if (this.$parent.debugState) {
          console.log("Found data");
          console.log(this.movies);
        }
        this.resultState = true;
        this.trimOutput();
      }
    },

    //Trims some movie metadata strings to make them fit the movie tooltip
    trimOutput() {
      for (var i in this.movies) {
        this.movies[i].Release =
          "(" + this.movies[i].Release.substring(0, 4) + ")";
        this.movies[i].Overview =
          this.movies[i].Overview.substring(0, 100) + "...";
      }
    },

    //Sets image style
    getImgStyle(url) {
      const imagePath = this.getPicUrl(url);
      const anotherOne = `url(" ` + imagePath + `")`;
      return { "background-image": anotherOne };
    },

    //Needed in order to force vue to recognize dynamic links existance at build.
    getPicUrl(url) {
      return require("../assets/posters" + url);
    },

    //Creates path for next view based on query and condition
    concatPath(id) {
      return "/Browse/" + id;
    },

    //Check if movie has been selected earlier.
    checkList(id) {
      if (this.$parent.previousSelection.includes(id)) {
        this.prevError = true;
      } else {
        this.$parent.previousSelection.push(id);
        this.nextScreen(id);
      }
    },

    //Handles end of view based on button press. Logs session information to database and reroutes to appropriate condition based on global variable
    nextScreen(id) {
      this.updateStuff("v_refMovie_" + this.$parent.itteration, id);
      if(this.$parent.itteration == 1 && [4,5,6].includes(this.$parent.condition))
      {
        this.$parent.tempIDStore = id;
        this.$router.push({ path: "/Instruction" });
      }
      else{
      this.$router.push({ path: this.concatPath(id) });
      }
    },

    //Update database with values. postService params:  Id - Field - Value
    async updateStuff(field, value) {
      await PostService.genericUpdate(this.$parent.sessionId, field, value);
    },
  },
};
</script>

<style scoped>
/*Legend Style*/
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.textBox {
  background-color: black;
  border: 1px solid white;
  padding: 10px;
  max-width: 1200px;
  display: block;
}
p,
h1 {
  color: white;
  padding: 5px;
  text-align: left;
  white-space: pre-line;
  text-align: center;
}
h1 {
  font-size: 2em;
  color: red;
}
h2 {
  font-size: 1.5em;
  color: white;
}
.info{
  font-size: 1.1em;
  padding-right: 50px;
  padding-left: 50px;
}
/*Search bar */
.searchBox {
  margin: 2em;
  max-width: 80%;
  display: block;
}
.searchField {
  width: 100%;
  display: flex;
}
#inputField {
  width: 15em;
  max-width: 80%;
  border: 1px solid white;
  background-color: black;
  border-right: none;
  padding: 10px;
  height: 20px;
  border-radius: 5px 0 0 5px;
  outline: none;
  color: white;
  font-size: 1.5em;
}
.searchBtn {
  width: 60px;
  height: 42px;
  border: 1px solid white;
  background: white;
  text-align: center;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
  position: relative;
  transition: 0.3s;
}
.searchBtn:hover {
  background-color: red;
  border: 1px solid red;
}
.searchIcon {
  position: absolute;
  top: 50%;
  left: 50%;
  height: 50%;
  transform: translate(-50%, -50%);
  width: 2em;
  height: 2em;
  display: block;
  color: black;
}

/*Error Styling */
.errorMsg {
  background-color: black;
  border: 1px solid white;
  max-width: 1200px;
}
.wrap {
  display: flex;
  align-items: center;
  justify-content: center;
}

/*Movie styling */
.movieContainer {
  display: grid;
  grid-gap: 1em;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
}
.movie {
  height: 100%;
  width: auto;
  box-sizing: border-box;
  margin: 1em;
}
.poster {
  height: 450px;
  width: 300px;
  display: inline-block;
  background-size: cover;
  transition: 0.2s;
}
.toolContainer {
  height: 100%;
  display: flex;
  flex-flow: column;
  align-items: center;
  justify-content: flex-end;
}
.tooltip {
  height: 100%;
  width: 100%;
  color: white;
  opacity: 0;
  background-image: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0),
    rgba(0, 0, 0, 0.9),
    rgba(0, 0, 0, 1),
    rgba(0, 0, 0, 1)
  );
  display: inline-block;
  transition: 0.3s;
}
.noselect {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.tooltipText {
  font-weight: bold;
  font-size: 1.3em;
  padding: 0px;
  margin: 0px;
}
.tooltipText:first-child {
  flex-grow: 3;
  padding: 5px;
  color: rgba(0, 0, 0, 0);
}
#tooltipOverview {
  max-height: 20%;
  max-width: 100%;
  font-size: 1em;
}
.btnconf {
  padding: 1rem 1.5rem;
  transition: 0.3s;
  border-radius: 3px;
  background-color: #404040;
  font-size: 1.4em;
  border: none;
  color: white;
  margin: 1em;
}
.poster:hover .tooltip {
  opacity: 1;
}
.poster:hover {
  transform: scale(1.06);
}
.btnconf:hover {
  background-color: darkgray;
  cursor: pointer;
}
/*IE targeting css hack to preserve some DOM order as grid is not supported*/
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
  .movieContainer {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
  }
}
</style>
