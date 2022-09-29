<template>
    <div class="content__left">

        <nav>
            <NavigationList id="main" name="Main" :content="main_menu" />
            <NavigationList id="music" name="Music" :content="music_menu" />
        </nav>

        <section class="playlist" v-if="is_user_logged">
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
                    <!-- TODO: Go to album page -->
	                  {{playing_song ? playing_song.name : "Nothing is currently playing"}}
	              </a>

	              <a class="playing__song_artist" href="#">
                    <!-- TODO: Go to artist page -->
                    {{playing_song ? playing_song.artist.name : ""}}
	              </a>

	              <div class="playing__add" v-if="is_user_logged">
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
	      is_user_logged: Boolean,
	      playing_song: Object
    },
    data () {
	      return {
	          main_menu: [
                {
                    "id": 0,
                    "name": "Home",
                    "url": "/",
                    "icon": "home"
                },
		            {
		                "id": 1,
		                "name": "Browse",
		                "url": "/browse",
		                "icon": "compass"
		            },
		            {
		                "id": 2,
		                "name": "Activity",
		                "url": "/activity",
		                "icon": "people"
		            },
		            {
		                "id": 3,
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
