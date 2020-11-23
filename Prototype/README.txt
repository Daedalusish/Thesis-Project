Hierarchy Guide: The following describes the structure of the code folders and where different codes lie. Any folder not included in this 
guide are folders utilized by the vue client developer and has little use in a code review, though are needed for running and building.

-\Root
|
-\client ---Contains all the code for the client side. This needs to be built in order to be utilized outside of vue client development.
|   |
|   |-\vue.config.js	---build settings and links the API to the build
|   |
|   |-\public		---Public in this instance contains the files that the compiler/builder will build into. Contains the rudimentory html shell and "tab" icon
|   |
|   |-\src		---Contains all the front end assets and code
|       |
|       |-\App.vue		--Root client level component. Every other "view" is rendered in this. Contains the global scope of settings, methods and data.
|       |
|       |-\main.js		--Initializer for the vue code. Doesn't contain much
|       |
|       |-\SearchService.js	--Main code that communicates with the API and handles client side queries to the server side API.
|       |
|       |-\assets 		---Contains movie posters and fonts
|       |
|       |-\router 		---Contains the settings for the router which is the code that handles single page dynamic routing between components
|       |
|       |-\views 		---Contains the different components/pages
|           |
|           |-\Welcome.vue	---Welcome page that contains instruction for the survey
|           |
|           |-\Search.vue 	---The page where the user can search for movies and select a reference movies
|           |
|           |-\Browse.vue	---The page where the user browses for component
|           |
|           |-\Survey.vue	---The exit survey.       
|
-\server  \\Main host folder in production and contains both the server side API handling and public folder for the build. Note, also contains index.js which is the server API
|   |
|   |-\public \\This folder contains the build, the compiled client code for hosting.
|   |
|   |-\routes
|   |    |
|   |    |-\api
    |		|
    |           |-\routes \\Here lies the javascript files that descibes the different API operations that can be performed on the database.
   

install guide (For hosting and viewing the application in development mode
You can technically do this in any IDE, and even without an IDE. This guide just centers around using Visual Studio Code.
%root% stands for the main folder that contains the server, client etc etc.

1. Have nodejs and npm install. This can be retrieved from https://nodejs.org/en/download/
if npm was just installed, you will need to restart the computer in order for the path to be updated. 
Verify installation with npm -v to check if path has been updated. Every other dependency is allready packaged.

2. install vue. This is done with %root% "npm install vue"

3. In order to run the application, you will need to open two terminals.
	3-Server - at %root%, "npm run dev". This will start the api at localhost:5000
	3-Client - at %root%\client, "npm run serve". This will host a development version of the application at localhost:8080

The application will now run and function as intended!

extra: 
In order to create a build for production, run "npm run build" in %root%\client. Then push the %root%\server folder into production.
Different hosting sites may use different setups and require some tweaking. The current setup is configured to be hosted at Heroku