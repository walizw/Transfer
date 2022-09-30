import config from "./config"

import axios from "axios"

export default {
    async get_latest_songs (pages) {
        let songs = []

        for (let i = 1; i < pages + 1; i++)
        {
            let response = await axios.get (config.ENDPOINT + `songs/?page=${i}`)
            let retrieved_songs = response ["data"]["results"]

            for (let j = 0; j < retrieved_songs.length; j++)
            {
                let artist_id = retrieved_songs [j].artist_id
                let artist_response = await axios.get (config.ENDPOINT + `artist/${artist_id}/`)
                retrieved_songs [j].artist = artist_response.data

                let album_id = retrieved_songs [j].album_id
                let album_response = await axios.get (config.ENDPOINT + `album/${album_id}/`)
                retrieved_songs [j].album = album_response.data
                songs.push (retrieved_songs [j])
            }
        }

        return songs
    },
    async get_latest_artists (pages) {
        let artists = []

        for (let i = 1; i < pages + 1; i++) {
            let response = await axios.get (config.ENDPOINT + `artists/?page=${i}`)
            let retrieved_artists = response ["data"]["results"]

            artists = artists.concat (retrieved_artists)
        }

        return artists
    },
    async get_artist_info (artist_id) {
        let info = []

        let response = await axios.get (config.ENDPOINT + `artist/${artist_id}/`)
        info = response ["data"]

        response = await axios.get (config.ENDPOINT + `artist/${artist_id}/albums/`)
        // TODO: Check if response ["next"] to get all the albums of the artist
        info.albums = response ["data"]

        return info
    },
    async get_artist_songs (artist_id) {
        // TODO: Get all pages
        let response = await axios.get (config.ENDPOINT + `artist/${artist_id}/songs/`)
        return response ["data"]
    },
    async get_album_songs (album_id) {
        // TODO: Get all pages
        let response = await axios.get (config.ENDPOINT + `album/${album_id}/songs/`)
        return response ["data"]
    }
}
