const express = require('express');
const mongodb = require('mongodb');
const {MongoClient} = require('mongodb')

const router = express.Router();

//returns the document containing all movie similarity information based on movie ID.
router.get('/', async (req, res) => {
    const client = await getData();
    const search = client.db('Session').collection('condition')
    res.send(await search.find({}).toArray());
    client.close();
});

async function getData(){
    const client = await mongodb.MongoClient.connect('mongodb+srv://Writer:banan@moviedatabase-pueny.mongodb.net/test?retryWrites=true&w=majority', {useNewUrlParser: true, useUnifiedTopology: true});
    
    return client
}

module.exports = router
