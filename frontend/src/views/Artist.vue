<template>
    <div class="is-verified">

        <div class="middle_scroll__header">
            <div class="middle_scroll__info">
                <div class="profile__img">
                    <img :src="artist_info.pfp ? artist_info.pfp : default_pfp" :alt="artist_info.name" />
                </div>

                <div class="artist__info__meta">
                    <div class="middle_scroll__info__type">Artist</div>
                    <div class="middle_scroll__info__name">{{artist_info.name}}</div>
                    <div class="middle_scroll__info__actions">
                        <button class="button-dark">
                            <ion-icon name="play"></ion-icon>
                            Play
                        </button>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import api from "../logic/api"

export default {
    name: "Artist",
    data () {
        return {
            artist_info: []
        }
    },
    computed: {
        default_pfp () {
            return require ("../assets/images/profile_picture.jpg")
        }
    },
    async created () {
        this.artist_info = await api.get_artist_info (this.$route.params.id)
        console.log (this.artist_info)
    }
}
</script>
