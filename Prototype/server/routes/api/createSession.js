const express = require('express');
const mongodb = require('mongodb');
const {MongoClient} = require('mongodb')

const router = express.Router();

//Creates a document with init values needed in the database.
router.post('/', async (req, res) => {
    const client = await postStuff()
    const post = client.db('Session').collection('SessionInfo')
    await post.insertOne({
        sessionName : req.body.id,
        time : new Date(),
        condition : req.body.condition,
        v_attetion1: req.body.passedFirstTest
    })
    res.status(201).send();
    client.close()
});


async function postStuff(){
    const client = await mongodb.MongoClient.connect('mongodb+srv://Writer:banan@moviedatabase-pueny.mongodb.net/test?retryWrites=true&w=majority', {useNewUrlParser: true, useUnifiedTopology: true});
    
    return client
}

module.exports = router

