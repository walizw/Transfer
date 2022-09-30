<template>
    <div class="track" v-if="song">
        <div class="track__art" @click="$emit ('clicked', song)">
            <img :alt="song.name" :src="song.artwork ? song.artwork : default_artwork"/>
        </div>

        <div class="track__number">{{number}}</div>

        <div v-if="playing_song && song.name === playing_song.name && song.artist_id === playing_song.artist_id"
             class="track__title text-success" @click="$emit ('clicked', song)">
            {{song.name}}
        </div>
        <div class="track__title" v-else>
            {{song.name}}
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
    computed: {
        default_artwork () {
            return require ("@/assets/images/album_artwork_placeholder.png")
        }
    }
}
</script>
