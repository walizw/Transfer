<template>
  <div class="content__left">

    <nav>
      <NavigationList id="main" name="Main" :content="main_menu" />
      <NavigationList id="music" name="Music" :content="music_menu" />
    </nav>

    <section class="playlist" v-if="user_logged">
      <a href="#">
	<ion-icon name="add-circle-outline"></ion-icon>
	New Playlist
      </a>
    </section>

    <section class="playing">
      <div class="playing__art" style="width: 50px; height: 50px; background-color: #181818; color: #fff; font-size: 250%; text-align: center;">
	<ion-icon name="musical-notes"></ion-icon>
      </div>

      <div class="playing__song">
	<a class="playing__song__name">
	  {{playing_song.name}}
	</a>

	<a class="playing__song_artist" href="">
	  <!-- TODO: Get artist -->
	</a>

	<div class="playing__add" v-if="user_logged">
	  <!-- TODO: Add -->
	</div>
      </div>
    </section>

  </div>
</template>

<script>
  import NavigationList from "./navigation/NavigationList"

  export default {
      name: "NavigationLeft",
      components: {
	  NavigationList
      },
      props: {
	  user_logged: Object,
	  playing_song: Object
      },
      data () {
	  return {
	      main_menu: [
		  {
		      "id": 0,
		      "name": "Browse",
		      "url": "/browse",
		      "icon": "compass"
		  },
		  {
		      "id": 1,
		      "name": "Activity",
		      "url": "/activity",
		      "icon": "people"
		  },
		  {
		      "id": 2,
		      "name": "Radio",
		      "url": "/radio",
		      "icon": "radio"
		  }
	      ],
	      music_menu: [
		  {
		      "id": 0,
		      "name": "Songs",
		      "url": "/explore/songs",
		      "icon": "musical-notes"
		  },
		  {
		      "id": 1,
		      "name": "Albums",
		      "url": "/explore/albums",
		      "icon": "albums"
		  },
		  {
		      "id": 2,
		      "name": "Artists",
		      "url": "/explore/artists",
		      "icon": "person"
		  }
	      ]
	  }
      }
    }
</script>
