<template>
    <section class="current-track">
        <div class="current-track__actions">
            <a href="#">
	              <ion-icon name="play-skip-back"></ion-icon>
            </a>

            <a href="#" @click="$emit ('pause_current')">
	              <ion-icon :name="playing ? 'pause' : 'play'"></ion-icon>
            </a>

            <a href="#">
	              <ion-icon name="play-skip-forward"></ion-icon>
            </a>
        </div>

        <div class="current-track__progress">
            <div class="current-track__progress__start">
                {{current_playtime}}
            </div>

            <div class="current-track__progress__bar">
	              <div id="song-progress"></div>
            </div>

            <div class="current-track__progress__finish">
                {{total_playtime}}
            </div>
        </div>

        <div class="current-track__options">
            <a class="lyrics" href="#">Lyrics</a>

            <span class="controls">
	              <a class="control" href="#">
	                  <ion-icon name="reorder-three"></ion-icon>
	              </a>
	              
	              <a class="control" href="#">
	                  <ion-icon name="shuffle"></ion-icon>
	              </a>
	              
	              <a class="control" href="#">
	                  <ion-icon name="repeat"></ion-icon>
	              </a>
	              
	              <a class="control devices" href="#">
	                  <ion-icon name="phone-portrait-outline"></ion-icon>
	                  <span>Devices Available</span>
	              </a>

	              <a class="control volume" href="#">
	                  <ion-icon name="volume-high-outline"></ion-icon>
	                  <div id="song-volume"></div>
	              </a>
            </span>
        </div>
    </section>
</template>

<script>
export default {
	  name: "CurrentTrack",
	  props: {
	      playing_song: Object,
        playing: Boolean,
        current_playtime: String,
        total_playtime: String
	  }
}
</script>
