import config from "./config"

import axios from "axios"

export default {
	async get_latest_songs(pages) {
		let songs = []

		for (let i = 1; i < pages + 1; i++) {
			let response = await axios.get(config.ENDPOINT + `songs/?page=${i}`)
			let retrieved_songs = response["data"]["results"]

			songs = songs.concat(retrieved_songs)
		}

		return songs
	},
	async get_latest_artists(pages) {
		let artists = []

		for (let i = 1; i < pages + 1; i++) {
			let response = await axios.get(
				config.ENDPOINT + `artists/?page=${i}`
			)
			let retrieved_artists = response["data"]["results"]

			artists = artists.concat(retrieved_artists)
		}

		return artists
	},
	async get_artist_info(artist_id) {
		let info = []

		let response = await axios.get(config.ENDPOINT + `artist/${artist_id}/`)
		info = response["data"]

		response = await axios.get(
			config.ENDPOINT + `artist/${artist_id}/albums/`
		)
		info.albums = response["data"]

		return info
	},
	async get_artist_songs(artist_id) {
		let response = await axios.get(
			config.ENDPOINT + `artist/${artist_id}/songs/`
		)
		return response["data"]
	},
	async get_album_info(album_id) {
		let response = await axios.get(config.ENDPOINT + `album/${album_id}/`)
		return response["data"]
	},
	async get_album_songs(album_id) {
		let response = await axios.get(
			config.ENDPOINT + `album/${album_id}/songs/`
		)
		return response["data"]
	},
}
