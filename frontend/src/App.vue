<template>
  <Header :is_user_logged="is_user_logged" />

  <div class="content">
    <NavigationLeft :is_user_logged="is_user_logged" :playing_song="playing_song" />

    <div class="content__middle">
      <router-view></router-view>
    </div>
  </div>

  <CurrentTrack :playing_song="playing_song" />
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
	      playing_song: {
		  "name": "Not playing anything",
		  "album_id": 0,
		  "artist_id": 0,
		  "audio_file": 0
	      }
	  }
      },
      computed: {
	  is_user_logged () {
	      return auth.is_user_logged ()
	  }
      }
  }
</script>
