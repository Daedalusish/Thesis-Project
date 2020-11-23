const express = require('express');
const mongodb = require('mongodb');
const {MongoClient} = require('mongodb')

const router = express.Router();

//Handles all updates for the database. Field is a string that denotes name. Value can be anything from an array containing several fields and names allready determined, or singular value.
router.post('/', async (req, res) => {
    const client = await postStuff()
    const post = client.db('Session').collection('SessionInfo')

    const fieldName = req.body.field
    const value = req.body.value
    const id = req.body.id

    await post.updateOne({
        "sessionName" : id}, 
        {$set: {[fieldName] : value}}, 
        upsert=false,multi = true)
    res.status(201).send();
    client.close();
});


async function postStuff(){
    const client = await mongodb.MongoClient.connect('mongodb+srv://Writer:banan@moviedatabase-pueny.mongodb.net/test?retryWrites=true&w=majority', {useNewUrlParser: true, useUnifiedTopology: true});
    
    return client
}

module.exports = router

