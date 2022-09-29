<template>
    <div class="middle-scroll">
        <div class="container">
            <div class="row">
                <div class="section-title pt-3 mr-3">Latest Songs</div>
                <div class="media-cards">

                    <div class="media-card" v-for="song in latest_songs">
                        <div class="media-card__image"
                             :style="[song.album.artwork ? {'background': 'url(' + song.album.artwork + ')'} : {'background': 'url(' + default_album_artwork + ')'}]">
                            <ion-icon name="play"></ion-icon>
                        </div>

                        <div class="media-card__footer">
                            <a>{{song.name}}</a>
                            <br>
                            <a>{{song.artist.name}}</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
import api from "@/logic/api"

export default {
    name: 'Home',
    data () {
        return {
            latest_songs: [],
            latest_artists: []
        }
    },
    computed: {
        default_album_artwork () {
            return require ("../assets/images/album_artwork_placeholder.png")
        }
    },
    async created () {
        this.latest_songs = await api.get_latest_songs (1)
    }
}
</script>
