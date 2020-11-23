const express = require('express');
const mongodb = require('mongodb');
const {MongoClient} = require('mongodb')

const router = express.Router();

//returns the document containing all movie similarity information based on movie ID.
router.get('/:query', async (req, res) => {
    const client = await getData();
    const term = String(req.params.query)
    const search = client.db('Movies').collection('MovieSims')
    res.send(await search.find({ID:term}).limit(2).toArray());
    client.close()
});

async function getData(){
    const client = await mongodb.MongoClient.connect('mongodb+srv://Writer:banan@moviedatabase-pueny.mongodb.net/test?retryWrites=true&w=majority', {useNewUrlParser: true, useUnifiedTopology: true});
    
    return client
}

module.exports = router
