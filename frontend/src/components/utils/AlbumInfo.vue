<template>
	<UpdateAlbumModal
		:album_id="album.id"
		:album_name="album.name"
		:album_year="album.year"
		:album_artist="album.artist_id"
	/>
	<div class="album" :id="album_id">
		<div class="album__info">
			<div class="album__info__art" @click="show_update_album">
				<img
					:alt="album.name"
					:src="album.artwork ? album.artwork : default_artwork"
				/>
			</div>

			<div class="album__info__meta">
				<div class="album__year">{{ album.year }}</div>
				<div class="album__name">{{ album.name }}</div>
				<div class="album__actions">
					<button
						@click="add_album_to_queue"
						class="button-light save"
					>
						Play
					</button>
				</div>
			</div>
		</div>

		<div class="album__tracks">
			<div class="tracks">
				<div class="tracks__heading">
					<div class="tracks__heading__number">#</div>
					<div class="tracks__heading__title">Song</div>
				</div>

				<TrackAlbumItem
					:song="song"
					v-for="song in songs"
					:playing_song="playing_song"
					@play_song="play_song"
					@add_to_queue="add_to_queue"
				/>
			</div>
		</div>
	</div>
</template>

<script>
import TrackAlbumItem from "./TrackAlbumItem"
import UpdateAlbumModal from "../modals/UpdateAlbumModal"

import api from "../../logic/api"

export default {
	name: "AlbumInfo",
	components: {
		TrackAlbumItem,
		UpdateAlbumModal,
	},
	emits: ["play_song", "add_to_queue"],
	data() {
		return {
			songs: [],
		}
	},
	props: {
		album: Object,
		playing_song: Object,
	},
	methods: {
		show_update_album() {
			$(`#update_album${this.album.id}_modal`).modal("show")
		},
		play_song(song) {
			this.$emit("play_song", song)
		},
		add_to_queue(song) {
			this.$emit("add_to_queue", song)
		},
		add_album_to_queue() {
			for (let i = 0; i < this.songs.length; i++) {
				let final_song = this.songs[i]
				this.$emit("add_to_queue", final_song)
			}
		},
	},
	computed: {
		default_artwork() {
			return require("@/assets/images/album_artwork_placeholder.png")
		},
		album_id() {
			let name = this.album.name
			return name.split(" ").join("_")
		},
	},
	async created() {
		try {
			this.songs = await api.get_album_songs(this.album.id)
		} catch (err) {
			console.log(err)
		}
	},
}
</script>
