<template>
	<section class="current-track">
		<div class="current-track__actions">
			<a @click="$emit('skip_previous')">
				<ion-icon name="play-skip-back"></ion-icon>
			</a>

			<a @click="$emit('pause_current')">
				<ion-icon :name="playing ? 'pause' : 'play'"></ion-icon>
			</a>

			<a @click="$emit('skip_next')">
				<ion-icon name="play-skip-forward"></ion-icon>
			</a>
		</div>

		<div class="current-track__progress">
			<div class="current-track__progress__start">
				{{ current_playtime }}
			</div>

			<div class="current-track__progress__bar">
				<div id="song-progress"></div>
			</div>

			<div class="current-track__progress__finish">
				{{ total_playtime }}
			</div>
		</div>

		<div class="current-track__options">
			<router-link class="lyrics" to="/lyrics">Lyrics</router-link>

			<span class="controls">
				<router-link to="/queue">
					<ion-icon name="reorder-three"></ion-icon>
				</router-link>

				<a class="control" href="#">
					<ion-icon name="shuffle"></ion-icon>
				</a>

				<a class="control" href="#">
					<ion-icon name="repeat"></ion-icon>
				</a>

				<a class="control devices" href="#">
					<ion-icon name="phone-portrait-outline"></ion-icon>
					<span>Devices Available</span>
				</a>

				<a class="control volume" href="#">
					<ion-icon name="volume-high-outline"></ion-icon>
					<div id="song-volume"></div>
				</a>
			</span>
		</div>
	</section>
</template>

<script>
export default {
	name: "CurrentTrack",
	emits: ["pause_current", "skip_next", "skip_previous"],
	props: {
		playing_song: Object,
		playing: Boolean,
		current_playtime: String,
		total_playtime: String,
	},
}
</script>
