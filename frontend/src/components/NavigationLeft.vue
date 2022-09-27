<template>
  <div class="content__left">

    <nav>
      <NavigationList id="main" name="Main" :content="main_menu" />
      <NavigationList id="music" name="Music" :content="music_menu" />
    </nav>

    <section class="playlist" v-if="userLogged">
      <a href="#">
	<ion-icon name="add-circle-outline"></ion-icon>
	New Playlist
      </a>
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
	  userLogged: Object
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
