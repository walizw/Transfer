<template>
    <div class="album">
        <div class="album__info">
            <div class="album__info__art">
                <img :alt="album.name" :src="album.artwork ? album.artwork : default_artwork"/>
            </div>

            <div class="album__info__meta">
                <div class="album__year">{{album.year}}</div>
                <div class="album__name">{{album.name}}</div>
                <div class="album__actions">
                    <button class="button-light save">Play</button>
                </div>
            </div>
        </div>

        <div class="album__tracks">
            <div class="tracks">
                <div class="tracks__heading">
                    <div class="tracks__heading__number">#</div>
                    <div class="tracks__heading__title">Song</div>
                </div>

                <TrackAlbumItem :song="song" v-for="song in songs"
                                :playing_song="playing_song"
                                @clicked="$emit ('clicked', song)" />
            </div>
        </div>
    </div>
</template>

<script>
import TrackAlbumItem from "./TrackAlbumItem"

import api from"../../logic/api"

export default {
    name: "AlbumInfo",
    components: {
        TrackAlbumItem
    },
    data () {
        return {
            songs: []
        }
    },
    props: {
        album: Object,
        playing_song: Object
    },
    computed: {
        default_artwork () {
            return require ("@/assets/images/album_artwork_placeholder.png")
        }
    },
    async created () {
        try
        {
            this.songs = await api.get_album_songs (this.album.id)
        } catch (err) {
            console.log (err)
        }
    }
}
</script>
