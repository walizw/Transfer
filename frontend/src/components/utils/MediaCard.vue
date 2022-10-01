<template>
  <div class="media-card">
    <div
      @click="$emit('play_song', item_id)"
      class="media-card__image"
      :style="[
        image
          ? { background: 'url(' + image + ')' }
          : { background: 'url(' + fallback_image + ')' },
      ]"
    >
      <ion-icon v-if="icon" :name="icon"></ion-icon>
    </div>

    <div class="media-card__footer">
      <div class="container">
        <div class="row">
          <div class="col-10">
            <div v-if="name && name1">
              <p class="text-truncate">
                <router-link :to="url">
                  {{ name }}
                </router-link>
                <br />
                By
                <router-link :to="url1">
                  {{ name1 }}
                </router-link>
              </p>
            </div>

            <div class="col-2">
              <!-- TODO: Song Context here -->
            </div>
          </div>
        </div>
      </div>

      <div v-if="name && !name1">
        <router-link :to="url">{{ name }}</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import SongContext from "./SongContext"

export default {
	name: "MediaCard",
	components: {
		SongContext,
	},
	props: {
		item_id: Number,
		image: String,
		fallback_image: String,
		icon: String,
		name: String,
		url: String,
		name1: String,
		url1: String,
	},
}
</script>
