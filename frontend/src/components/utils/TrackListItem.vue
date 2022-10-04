<template>
  <div class="track" v-if="song" :id="name_id">
    <div class="track__art" @click="$emit('play_song', song_to_play)"></div>

    <div class="track__number">{{ number }}</div>

    <div class="track__title">
      <i
        v-if="
          playing_song &&
          song.name === playing_song.name &&
          song.artist_id === playing_song.artist_id
        "
        @click="$emit('play_song', song_to_play)"
        class="text-success"
      >
        {{ song.name }}
      </i>
      <a @click="$emit('play_song', song_to_play)" v-else>
        {{ song.name }}
      </a>
    </div>

    <div class="track__plays">
      <SongContext
        @play_song="$emit('play_song', song_to_play)"
        @add_to_queue="$emit('add_to_queue', song_to_play)"
        :song="song"
      />
    </div>
  </div>
</template>

<script>
import SongContext from "./SongContext"

export default {
	name: "TrackListItem",
	components: {
		SongContext,
	},
	emits: ["play_song", "add_to_queue"],
	props: {
		song: Object,
		number: Number, // Song number
		playing_song: Object,
	},
	computed: {
		default_artwork() {
			return require("@/assets/images/album_artwork_placeholder.png")
		},
		name_id() {
			return this.playing_song
				? this.playing_song.name.replace(/\W/g, "_")
				: ""
		},
		song_to_play() {
			return this.song
		},
	},
}
</script>
