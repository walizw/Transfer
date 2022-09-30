<template>
    <div class="track" v-if="song" @click="$emit ('clicked', song)"
         :id="name_id">
        <div class="track__number">{{song.track_number}}</div>
        <div v-if="playing_song && song.name === playing_song.name && song.artist_id === playing_song.artist_id"
             class="track__title text-success">
            {{song.name}}
        </div>
        <div class="track__title" @click="$emit ('clicked', song)" v-else>
            {{song.name}}
        </div>
    </div>
</template>

<script>
export default {
    name: "TrackAlbumItem",
    props: {
        song: Object,
        playing_song: Object
    },
    computed: {
        default_artwork () {
            return require ("@/assets/images/album_artwork_placeholder.png")
        },
        name_id () {
            return this.playing_song ? "album_" + this.playing_song.name.replace (/\W/g, '_') : ""
        }
    }
}
</script>
