<template>
	<Header :is_user_logged="is_user_logged" />

	<div class="content">
		<NavigationLeft
			:is_user_logged="is_user_logged"
			:playing_song="playing_song"
		/>

		<div class="content__middle">
			<div class="middle_scroll">
				<router-view
					@play_song="play_song"
					@add_to_queue="add_to_queue"
					@clear_queue="clear_queue"
					:playing_song="playing_song"
					:playing_queue="playing_queue"
				></router-view>
			</div>
		</div>
	</div>

	<CurrentTrack
		:playing_song="playing_song"
		:playing="playing"
		:current_playtime="current_playtime"
		:total_playtime="total_playtime"
		@pause_current="pause_song"
		@skip_next="skip_next"
		@skip_previous="skip_previous"
	/>

	<audio hidden id="song_audio">
		<source
			v-if="playing_song"
			:src="playing_song.audio_file"
			type="audio/mpeg"
		/>
	</audio>
</template>

<style>
@import "@/assets/styles.css";
</style>

<script>
import Header from "./components/Header"
import NavigationLeft from "./components/NavigationLeft"
import CurrentTrack from "./components/footer/CurrentTrack"
import auth from "@/logic/auth"
export default {
	name: "App",
	components: {
		Header,
		NavigationLeft,
		CurrentTrack,
	},
	data() {
		return {
			playing: false,
			playing_song: null,
			playing_queue: [],
			playing_id: 0, // playing_queue [playing_id], basically

			// viewport
			current_playtime: "0:00",
			total_playtime: "0:00",
			header_height: 0,
			footer_height: 0,
			playlist_height: 0,
			now_playing_height: 0,
			total_height: 0,
			nav_height: 0,
			middle_height: 0,
		}
	},
	computed: {
		is_user_logged() {
			return auth.is_user_logged()
		},
	},
	watch: {
		playing_id() {
			if (this.playing_id < 0)
				this.playing_id =
					this.playing_queue.length > 0
						? this.playing_queue.length - 1
						: 0
			else if (this.playing_id >= this.playing_queue.length)
				this.playing_id = 0

			if (this.playing_queue[this.playing_id])
				this.playing_song = this.playing_queue[this.playing_id]
			else this.playing_song = null
		},
		playing_song() {
			if (this.playing_song === null) {
				let song_audio = document.getElementById("song_audio")
				song_audio.pause()
				return
			}
			this.play_song(this.playing_song, false)
		},
		total_height() {
			this.nav_height =
				window.innerHeight -
				(this.header_height +
					this.footer_height +
					this.playlist_height +
					this.now_playing_height)
			this.middle_height =
				window.innerHeight - (this.header_height + this.footer_height)
			if ($(window).width() <= 768) {
				$(".collapse").removeClass("show")
				$("nav").css("height", "auto")
				$(".artist").css("height", "auto")
				$(".middle_scroll").css("height", this.middle_height)
			} else {
				$("nav").css("height", this.nav_height)
				$(".middle_scroll").css("height", this.middle_height)
				$(".collapse").addClass("show")
			}
		},
	},
	methods: {
		resize_viewports() {
			this.header_height = $("header").outerHeight()
			this.footer_height = $(".current-track").outerHeight()
			this.playlist_height = $(".playlist").outerHeight()
			this.now_playing_height = $(".playing").outerHeight()
			this.total_height = $(window).height()
		},
		pause_song() {
			if (!this.playing_song) return
			this.playing = !this.playing
			let song_audio = document.getElementById("song_audio")
			if (this.playing) song_audio.play()
			else if (!this.playing) song_audio.pause()
		},
		clear_queue() {
			this.playing_id = 0
			this.playing = false
			this.playing_song = null
			this.playing_queue = []
			this.total_playtime = "0:00"
			this.current_playtime = "0:00"
		},
		add_to_queue(song) {
			this.playing_queue.push(song)

			if (!this.playing_song) {
				this.playing_id = 0
				this.play_song(this.playing_queue[this.playing_id], false)
			}
		},
		remove_from_queue(song) {
			this.playing_queue = this.playing_queue.filter((x) => {
				x.id != song.id
			})
		},
		skip_next() {
			this.playing_id++
		},
		skip_previous() {
			this.playing_id--
		},
		play_song(song, add = true) {
			this.playing_song = song

			if (add) this.add_to_queue(song)

			let song_audio = document.getElementById("song_audio")
			try {
				song_audio.load()
				song_audio.play()
				this.playing = true
				let self = this
				song_audio.oncanplay = (e) => {
					let slider = document.getElementById("song-progress")
					slider.noUiSlider.destroy()
					noUiSlider.create(slider, {
						start: [0],
						range: {
							min: [0],
							max: [Math.floor(song_audio.duration)],
						},
					})
					slider.noUiSlider.on("start", () => {
						song_audio.pause()
					})
					slider.noUiSlider.on("slide", (v) => {
						song_audio.currentTime = parseInt(v[0])
					})
					slider.noUiSlider.on("end", (v) => {
						song_audio.play()
					})
					let total_seconds = Math.floor(song_audio.duration % 60)
					let total_minutes = Math.floor(song_audio.duration / 60)
					self.total_playtime = `${total_minutes}:${
						total_seconds < 10 ? "0" + total_seconds : total_seconds
					}`
				}
				song_audio.onpause = (e) => {
					self.playing = false
				}
				song_audio.onplay = (e) => {
					self.playing = true
				}
				song_audio.onended = (e) => {
					self.playing = false
					self.playing_id++
				}
				song_audio.ontimeupdate = (e) => {
					document
						.getElementById("song-progress")
						.noUiSlider.set(song_audio.currentTime)
					self.current_playtime = ""
					let seconds = Math.floor(song_audio.currentTime)
					let minutes = Math.floor(seconds / 60)
					self.current_playtime += `${minutes}:`
					if (seconds % 60 < 10)
						self.current_playtime += `0${seconds % 60}`
					else self.current_playtime += `${seconds % 60}`
				}
			} catch (err) {
				this.playing = false
				console.log(err)
			}
		},
	},
	created() {
		let self = this
		window.onresize = this.resize_viewports
		$(document).ready(() => {
			var slider = document.getElementById("song-progress")
			noUiSlider.create(slider, {
				start: [0],
				range: {
					min: [0],
					max: [0],
				},
			})
			self.resize_viewports()
		})
	},
}
</script>
