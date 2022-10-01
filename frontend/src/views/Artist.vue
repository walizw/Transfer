<template>
  <UpdateArtistModal
    :artist_id="artist_info.id"
    :artist_name="artist_info.name"
    :artist_bio="artist_info.bio"
  />

  <div class="is-verified">
    <div class="middle_scroll__header">
      <div class="middle_scroll__info">
        <div class="profile__img" @click="show_update_artist">
          <img
            :src="artist_info.pfp ? artist_info.pfp : default_pfp"
            :alt="artist_info.name"
          />
        </div>

        <div class="artist__info__meta">
          <div class="middle_scroll__info__type">Artist</div>
          <div class="middle_scroll__info__name">
            {{ artist_info.name }}
          </div>
          <div class="middle_scroll__info__actions">
            <button class="button-dark">
              <ion-icon name="play"></ion-icon>
              Play
            </button>
          </div>
        </div>
      </div>

      <div class="navigation">
        <ul class="nav nav-tabs" id="artistTab" role="tablist">
          <li class="nav-item" role="presentation">
            <a
              class="nav-link active"
              id="overview-tab-btn"
              data-bs-toggle="tab"
              data-bs-target="#overview-tab"
              type="button"
              role="tab"
              aria-controls="overview"
              aria-selected="true"
            >
              Overview
            </a>
          </li>

          <li class="nav-item" role="presentation">
            <a
              class="nav-link"
              id="related-tab-btn"
              data-bs-toggle="tab"
              data-bs-target="#related-tab"
              type="button"
              role="tab"
              aria-controls="related"
              aria-selected="false"
            >
              Related Artists
            </a>
          </li>
        </ul>
      </div>
    </div>

    <div class="middle_scroll__content">
      <div id="artistTabContent" class="tab-content">
        <div
          class="tab-pane fade show active"
          id="overview-tab"
          role="tabpanel"
          aria-labelledby="overview-tab-btn"
        >
          <div class="overview__artist">
            <div class="section-title">Latest</div>
            <div class="tracks">
              <TrackListItem
                :song="artist_songs ? artist_songs[index - 1] : {}"
                :number="index"
                @play_song="play_song"
                @add_to_queue="add_to_queue"
                :playing_song="playing_song"
                v-for="index in 5"
                :key="index"
              />
            </div>
          </div>

          <div class="overview__albums">
            <div class="overview__albums__head">
              <span class="section-title">Albums</span>

              <span class="view-type">
                <ion-icon name="list" class="list active"></ion-icon>
              </span>
            </div>

            <AlbumInfo
              :album="album"
              v-for="album in artist_albums"
              :playing_song="playing_song"
              @play_song="play_song"
              @add_to_queue="add_to_queue"
            />
          </div>
        </div>

        <div
          id="related-tab"
          class="tab-pane fade"
          role="tabpanel"
          aria-labelledby="related-tab-btn"
        >
          <h1>Related goes here</h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../logic/api"

import TrackListItem from "../components/utils/TrackListItem"
import AlbumInfo from "../components/utils/AlbumInfo"

import UpdateArtistModal from "../components/modals/UpdateArtistModal.vue"

export default {
	name: "Artist",
	emits: ["play_song", "add_to_queue"],
	components: {
		TrackListItem,
		AlbumInfo,
		UpdateArtistModal,
	},
	emits: ["play_song", "add_to_queue"],
	props: {
		playing_song: Object,
	},
	data() {
		return {
			artist_info: [],
			artist_songs: [],
			artist_albums: [],
		}
	},
	computed: {
		default_pfp() {
			return require("../assets/images/profile_picture.jpg")
		},
	},
	methods: {
		play_song(song) {
			let final_song = song
			song.artist = this.artist_info
			this.$emit("play_song", final_song)
		},
		add_to_queue(song) {
			let final_song = song
			song.artist = this.artist_info
			this.$emit("add_to_queue", final_song)
		},
		show_update_artist() {
			$("#update_artist_modal").modal("show")
		},
	},
	async created() {
		let self = this

		this.artist_info = JSON.parse(
			JSON.stringify(await api.get_artist_info(this.$route.params.id))
		)
		this.artist_songs = JSON.parse(
			JSON.stringify(await api.get_artist_songs(this.$route.params.id))
		)
		this.artist_songs.forEach((x) => {
			x.album = self.artist_info.albums.filter((e) => {
				return e.id == x.album_id
			})
		})
		this.artist_albums = await this.artist_info.albums
	},
}
</script>
