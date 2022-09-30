<template>
    <div class="content__left">

        <nav :style="'height:' + nav_height + 'px;'">
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
            <div class="playing__art">
	              <img :src="default_artwork"/>
            </div>

            <div class="playing__song">
	              <a class="playing__song__name text-truncated">
                    <!-- TODO: Go to album page -->
	                  {{playing_song ? playing_song.name : "Nothing is currently playing"}}
	              </a>

	              <router-link :to="playing_song ? `/artist/${playing_song.artist.id}` : '#'">
                    <!-- TODO: Go to artist page -->
                    {{playing_song ? playing_song.artist.name : ""}}
	              </router-link>

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
	      playing_song: Object,
        nav_height: Number
    },
    computed: {
        default_artwork () {
            return require ("../assets/images/album_artwork_placeholder.png")
        }
    },
    data () {
	      return {
	          main_menu: [
		            {
		                "id": 1,
		                "name": "Browse",
		                "url": "/",
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
