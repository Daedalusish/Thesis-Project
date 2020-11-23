const express = require('express');
const mongodb = require('mongodb');
const {MongoClient} = require('mongodb')

const router = express.Router();

//Calls to thos returns searches. :query is the extension of url that constitute the text to search from. Search settings are defined in mongoDb index settings so it mostly is given a string and returns an array of all documents fitting the term.
router.get('/:query', async (req, res) => {
    const client = await searchStuff();
    const term = String(req.params.query)
    console.log("Searching")
    const search = client.db('Movies').collection('MovieData2')
    res.send(await search.find({$text:{$search: term} }).toArray());
    client.close()
});


async function searchStuff(){
    const client = await mongodb.MongoClient.connect('mongodb+srv://Writer:banan@moviedatabase-pueny.mongodb.net/test?retryWrites=true&w=majority', {useNewUrlParser: true, useUnifiedTopology: true});
    
    return client
}

module.exports = router

