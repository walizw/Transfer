<template>
  <div class="container">
    <div class="row" v-if="playing_song">
      <div class="col">
        <div
          style="
            margin: 0;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-125%, -50%);
          "
        >
          <img :alt="playing_song.name" :src="playing_song.album.artwork" />
          <h1 class="section-title text-center">
            <br />{{ playing_song.name }}
          </h1>

          <router-link :to="`/artist/${playing_song.artist.id}`">
            <h6 class="text-center">{{ playing_song.artist.name }}</h6>
          </router-link>
        </div>
      </div>

      <div class="col">
        <div class="section-title">Lyrics</div>

        <div style="overflow-y: scroll; height: 100%">
          <div :key="line" v-for="line in lyrics">
            <h1 class="text-light">{{ line }}</h1>
          </div>
        </div>
      </div>
    </div>
    <div class="row" v-else>
      <div class="container">
        <div class="row">
          <div class="col">
            <div
              style="
                margin: 0;
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
              "
            >
              <h1 class="text-light">Nothing is currently playing</h1>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
	name: "Lyrics",
	props: {
		playing_song: Object,
	},
	computed: {
		lyrics() {
			return this.playing_song.lyrics.split("\n")
		},
	},
}
</script>
