<template>
	<div class="container">
		<div class="row">
			<div class="section-title mt-3 col">Queue</div>
			<div class="col">
				<p
					@click="$emit('clear_queue')"
					class="text-end text-light mt-3"
				>
					Clear queue
				</p>
			</div>
		</div>
		<!-- TODO: Drag this to reorganize the queue -->
		<div v-if="playing_queue.length > 0" class="overview__artist tracks">
			<div v-for="i in playing_queue.length" :key="i">
				<TrackListItem
					:number="i"
					:song="playing_queue[i]"
					:playing_song="playing_song"
				/>
			</div>
		</div>
		<h1 class="text-light" v-else>Your Queue is empty</h1>
	</div>
</template>

<script>
import TrackListItem from "@/components/utils/TrackListItem"

export default {
	name: "Queue",
	components: {
		TrackListItem,
	},
	emits: ["clear_queue"],
	props: {
		playing_queue: Object,
		playing_song: Object,
	},
}
</script>
