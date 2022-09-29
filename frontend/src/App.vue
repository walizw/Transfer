<template>
    <Header :is_user_logged="is_user_logged" />

    <div class="content">
        <NavigationLeft :is_user_logged="is_user_logged" :playing_song="playing_song" />

        <div class="content__middle">
            <router-view @play_song="play_song"></router-view>
        </div>
    </div>

    <CurrentTrack :playing_song="playing_song" :playing="playing"
                  :current_playtime="current_playtime"
                  :total_playtime="total_playtime" />
    <audio hidden id="song_audio">
        <source v-if="playing_song" :src="playing_song.audio_file" type="audio/mpeg" />
    </audio>
</template>

<style>
@import "@/assets/styles.css";
</style>

<script>
import Header from "./components/Header"
import NavigationLeft from "./components/NavigationLeft"
import CurrentTrack from "./components/footer/CurrentTrack"

import auth from "@/logic/auth"

export default {
    name: "App",
    components: {
	      Header,
	      NavigationLeft,
	      CurrentTrack
    },
    data () {
	      return {
            playing: false,
	          playing_song: null,
            current_playtime: "0:00",
            total_playtime: "0:00",
	      }
    },
    computed: {
	      is_user_logged () {
	          return auth.is_user_logged ()
	      }
    },
    methods: {
        resize_viewports () {
            let total_height = $(window).height ()

            let header_height = $("header").outerHeight ()
            let footer_height = $(".current-track").outerHeight ()
            let playlist_height = $(".playlist").outerHeight ()
            let now_playing = $(".playing").outerHeight ()

            let nav_height = total_height - (header_height + footer_height + playlist_height + now_playing)
            let middle_height = total_height - (header_height + footer_height)

            $("nav").css ("height", nav_height)
            $(".middle_scroll").css ("height", middle_height)
        },
        play_song (song) {
            this.playing_song = song

            let song_audio = document.getElementById ("song_audio")

            try {
                song_audio.load ()
                song_audio.play ()

                this.playing = true

                let self = this
                song_audio.oncanplay = (e) => {
                    let total_seconds = Math.floor (song_audio.duration % 60)
                    let total_minutes = Math.floor (song_audio.duration / 60)

                    self.total_playtime = `${total_minutes}:${total_seconds < 10 ? '0' + total_seconds : total_seconds}`
                }

                song_audio.ontimeupdate = (e) => {
                    self.current_playtime = ""

                    let seconds = Math.floor (song_audio.currentTime)
                    let minutes = Math.floor (seconds / 60)

                    self.current_playtime += `${minutes}:`

                    if (seconds % 60 < 10)
                        self.current_playtime += `0${seconds % 60}`
                    else
                        self.current_playtime += `${seconds  % 60}`
                }
            }
            catch (err) {
                this.playing = false
                console.log (err)
            }
        }
    },
    created () {
        let self = this
        $(window).on ("resize", self.resize_viewports)
        $(window).ready (self.resize_viewports)
    }
}
</script>
