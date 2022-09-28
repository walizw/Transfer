<template>
  <Header :user_logged="user_logged" />

  <div class="content">
    <NavigationLeft :user_logged="user_logged" :playing_song="playing_song" />

    <div class="content__middle">
      <router-view></router-view>
    </div>
  </div>
</template>

<style>
  @import "./assets/styles.css";
</style>

<script>
  import Header from "./components/Header"
  import NavigationLeft from "./components/NavigationLeft"

  import auth from "@/logic/auth"

  export default {
      name: "App",
      components: {
	  Header,
	  NavigationLeft
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
	  user_logged () {
	      return auth.get_user_logged ()
	  }
      }
  }
</script>
