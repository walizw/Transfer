<template>
  <div class="dropdown">
    <button
      class="text-light bg-dark dropdown dropdown-toggle"
      type="button"
      :id="`dropdown_song_${song.id}`"
      data-bs-toggle="dropdown"
      aria-expanded="false"
    >
      <ion-icon name="reorder-three"></ion-icon>
    </button>

    <ul
      class="dropdown-menu dropdown-menu-dark"
      :aria-labelledby="`dropdown_song_${song.id}`"
    >
      <li>
        <a @click="$emit('play_song', song)" class="dropdown-item">Play</a>
      </li>

      <li>
        <a @click="$emit('add_to_queue', song)" class="dropdown-item"
          >Add to Queue</a
        >
      </li>
    </ul>
  </div>
</template>

<script>
export default {
	name: "SongContext",
	emits: ["play_song", "add_to_queue"],
	props: {
		song: Object,
	},
}
</script>
