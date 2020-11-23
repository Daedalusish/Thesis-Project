/* eslint-disable no-async-promise-executor */
import axios from 'axios';

// DEV
//const url ='http://localhost:5000/api'
//PROD
const url = 'api'

class PostService {
    static searchMovie(query) {
        return new Promise(async(resolve, reject) => {
            try{
                const res = await axios.get(url.concat('/search/',query))
                const data = res.data;

                resolve(
                    data.map(results => ({
                        ...results
                    }))
                );
            } catch(err) {
                reject(err)
            }
        })
    }
    static getSims(query) {
        return new Promise(async(resolve, reject) => {
            try{
                const res = await axios.get(url.concat('/getSim/',query))
                const data = res.data;
                resolve(
                    data.map(results => ({
                        ...results
                    }))
                ); 
            } catch(err) {
                reject(err)
            }
        })
    }
    static getCondition() {
        return new Promise(async(resolve, reject) => {
            try{
                const res = await axios.get(url.concat('/getCondition/'))
                const data = res.data;
                resolve(
                    data.map(results => ({
                        ...results
                    }))
                ); 
            } catch(err) {
                reject(err)
            }
        })
    }
    static createSession(id,condition,passedFirstTest) {
        return axios.post(url.concat('/createSession/'), {
            id, condition, passedFirstTest
       });
    }
    static genericUpdate(id,field,value) {
        return axios.post(url.concat('/genericUpdate/'), {
            id, value, field
        })
    }
}
export default PostService