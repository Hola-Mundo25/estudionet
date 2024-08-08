import axios from "axios"

const API = 'https://api.thecatapi.com/v1/'

export default {
    nuevos() {
    const resource = 'images'
    return {
        getOne: () => axios.get(`${API}/${resource}/search?limit=3`)

        //getOne: ({ by, value }) => axios.get(`${API}/${resource}/${by}/${value}`)
    }}
    }