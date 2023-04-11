import axios from 'axios'

export const API = axios.create({
    baseURL : "127.0.0.1:8000",
    responseType : 'json',
})


const getMessages = () => {
    return API.get('/');
}

export default {
    getMessages
}