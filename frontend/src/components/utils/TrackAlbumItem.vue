<template>
  <div class="track" v-if="song" :id="name_id">
    <div class="track__number">{{ song.track_number }}</div>
    <div
      v-if="
        playing_song &&
        song.name === playing_song.name &&
        song.artist_id === playing_song.artist_id
      "
      class="track__title text-success"
    >
      {{ song.name }}
    </div>
    <div class="track__title" @click="$emit('play_song', song)" v-else>
      {{ song.name }}
    </div>

    <div class="track__plays">
      <SongContext
        @play_song="$emit('play_song', song)"
        @add_to_queue="$emit('add_to_queue', song)"
        :song="song"
      />
    </div>
  </div>
</template>

<script>
import SongContext from "./SongContext"

export default {
	name: "TrackAlbumItem",
	components: {
		SongContext,
	},
	props: {
		song: Object,
		playing_song: Object,
	},
	emits: ["play_song", "add_to_queue"],
	computed: {
		default_artwork() {
			return require("@/assets/images/album_artwork_placeholder.png")
		},
		name_id() {
			return this.playing_song
				? "album_" + this.playing_song.name.replace(/\W/g, "_")
				: ""
		},
	},
}
</script>
