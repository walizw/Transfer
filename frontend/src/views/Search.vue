<template>
	<div class="container">
		<div class="row">
			<div class="section-title pt-3 mr-3">
				Results for {{ $route.params.query }}
			</div>

			<div class="tracks">
				<div class="section-title">Tracks</div>
				<TrackListItem
					:song="song_results ? song_results[index - 1] : {}"
					:number="index"
					@play_song="play_song"
					@add_to_queue="add_to_queue"
					:playing_song="playing_song"
					v-for="index in 10"
					:key="index"
					include_artist
				/>
			</div>

			<div class="media_cards">
				<div class="section-title">Artists</div>
			</div>
		</div>
	</div>
</template>

<script>
import api from "@/logic/api"

import TrackListItem from "../components/utils/TrackListItem.vue"

export default {
	// eslint-disable-next-line vue/multi-word-component-names
	name: "Search",
	emits: ["play_song", "add_to_queue"],
	components: {
		TrackListItem,
	},
	props: {
		playing_song: Object,
	},
	data() {
		return {
			song_results: [],
		}
	},
	watch: {
		"$route.params.query"(query) {
			this.get_results()
		},
	},
	methods: {
		async get_results() {
			this.song_results = await api.search(this.$route.params.query)
			this.song_results = this.song_results.results
		},
		play_song(song) {
			this.$emit("play_song", song)
		},
		add_to_queue(song) {
			this.$emit("add_to_queue", song)
		},
	},
	async created() {
		this.get_results()
	},
}
</script>
