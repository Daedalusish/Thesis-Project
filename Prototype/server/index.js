const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')

//Start script with NPM RUN DEV

const app = express();
/*This is the main API files. currently hosts on port 5000. Mostly uses libraries. Each url is stored in singular files and this stores the routes to them. */
app.use(bodyParser.json({ limit: "50mb" }));
app.use(cors());

const search = require('./routes/api/search');
app.use('/api/search', search)

const getSim = require('./routes/api/getSim');
app.use('/api/getSim', getSim)

const createSession = require('./routes/api/createSession');
app.use('/api/createSession', createSession)

const genericUpdate = require('./routes/api/genericUpdate');
app.use('/api/genericUpdate', genericUpdate)

const getCondition = require('./routes/api/getCondition.js');
app.use('/api/getCondition', getCondition)

if(process.env.NODE_ENV === 'production') {
    app.use(express.static(__dirname + '/public/'))
    app.get(/.*/, (req,res) => res.sendFile(__dirname + '/public/index.html'))
}

const port = process.env.PORT || 5000;

app.listen(port, () => console.log('Api now online at port ' + port));