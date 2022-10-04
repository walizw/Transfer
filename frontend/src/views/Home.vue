<template>
	<div class="container">
		<div class="row">
			<div class="section-title pt-3 mr-3">Latest Songs</div>
			<div class="media-cards">
				<MediaCard
					v-for="song in latest_songs"
					:item_id="song.id"
					:image="song.album ? song.album.artwork : default_artwork"
					:fallback_image="default_album_artwork"
					icon="play"
					:name="song.name"
					url="#"
					:name1="song.artist.name"
					:url1="'/artist/' + song.artist.id"
					@play_song="play_song"
				/>
			</div>

			<div class="section-title pt-3 mr-3">Latest Artists</div>
			<div class="media-cards">
				<MediaCard
					v-for="artist in latest_artists"
					:item_id="artist.id"
					:image="artist.pfp"
					:fallback_image="default_artist_pfp"
					:name="artist.name"
					:url="'/artist/' + artist.id"
				/>
			</div>
		</div>
	</div>
</template>

<script>
import api from "@/logic/api"
import MediaCard from "@/components/utils/MediaCard"

export default {
	name: "Home",
	components: {
		MediaCard,
	},
	methods: {
		play_song(sng_id) {
			let song_to_play = this.latest_songs.find((x) => x.id == sng_id)
			this.$emit("play_song", song_to_play)
		},
	},
	data() {
		return {
			latest_songs: [],
			latest_artists: [],
		}
	},
	computed: {
		default_album_artwork() {
			return require("../assets/images/album_artwork_placeholder.png")
		},
		default_artist_pfp() {
			return require("../assets/images/profile_picture.jpg")
		},
	},
	async created() {
		this.latest_songs = await api.get_latest_songs(1)
		this.latest_artists = await api.get_latest_artists(1)
	},
}
</script>
