<template>
    <Header :is_user_logged="is_user_logged" />

    <div class="content">
        <NavigationLeft :is_user_logged="is_user_logged" :playing_song="playing_song" :nav_height="nav_height" />

        <div class="content__middle">
            <div class="middle_scroll"
                 :style="'height:' + middle_height + 'px;'">
                <router-view @play_song="play_song"></router-view>
            </div>
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
            header_height: 0,
            footer_height: 0,
            playlist_height: 0,
            now_playing_height: 0,
            total_height: 0,
            nav_height: 0,
            middle_height: 0
	      }
    },
    computed: {
	      is_user_logged () {
	          return auth.is_user_logged ()
	      }
    },
    watch: {
        total_height () {
            this.nav_height = window.innerHeight - (this.header_height +
                                         this.footer_height +
                                         this.playlist_height +
                                         this.now_playing_height)

            this.middle_height =  window.innerHeight - (this.header_height +
                                                        this.footer_height)
        }
    },
    methods: {
        resize_viewports () {
            this.header_height = $("header").outerHeight ()
            this.footer_height = $(".current-track").outerHeight ()
            this.playlist_height = $(".playlist").outerHeight ()
            this.now_playing_height = $(".playing").outerHeight ()

            this.total_height = window.innerHeight
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
        $(document).ready (self.resize_viewports)
    }
}
</script>
