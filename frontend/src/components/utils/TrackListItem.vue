<template>
    <div class="track" v-if="song" :id="name_id">
        <div class="track__art" @click="$emit ('clicked', song)">
        </div>

        <div class="track__number">{{number}}</div>

        <div class="track__title">
            <i v-if="playing_song && song.name === playing_song.name && song.artist_id === playing_song.artist_id"
                 @click="play_song"
                 class="text-success">
                {{song.name}}
            </i>
            <a @click="play_song" v-else>
                {{song.name}}
            </a>
        </div>
    </div>
</template>

<script>
export default {
    name: "TrackListItem",
    props: {
        song: Object,
        number: Number, // Song number
        playing_song: Object
    },
    methods: {
        play_song () {
            this.song.album = this.song.album [0]
            this.$emit ("clicked", this.song)
        }
    },
    computed: {
        default_artwork () {
            return require ("@/assets/images/album_artwork_placeholder.png")
        },
        name_id () {
            return this.playing_song ? this.playing_song.name.replace (/\W/g, '_') : ""
        }
    }
}
</script>
