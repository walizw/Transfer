<template>
	<div class="container">
		<div class="row">
			<form
				@submit="on_submit"
				class="col-md-10 align-self-center mx-auto p-5"
			>
				<div class="mb-3">
					<h1 class="text-light">Upload</h1>
					<h3 class="text-secondary">
						Upload a song to this local instance of Transfer!
					</h3>
				</div>

				<div class="mb-3">
					<label for="input_file" class="form-label text-secondary"
						>Song file:</label
					>
					<input
						@change="changed_file"
						name="file"
						type="file"
						ref="song"
						id="input_file"
						class="form-control"
						aria-describedby="file_text"
					/>
					<div id="file_text" class="form-text">
						Yes! You only need an audio file, we'll extract the
						metadata of this song. Don't worry, you can manually
						modify this later.
					</div>
				</div>

				<div class="alert alert-danger" role="alert" v-if="error">
					There has been an error uploading the song.
				</div>

				<div class="alert alert-success" role="alert" v-if="success">
					Song uploaded successfully!
				</div>

				<button class="btn btn-success" type="submit">Upload</button>
			</form>
		</div>
	</div>
</template>

<script>
import axios from "axios"

import config from "@/logic/config.js"
import user from "@/logic/user.js"

export default {
	name: "Upload",
	data() {
		return {
			file: "",
			error: false,
			success: false,
		}
	},
	methods: {
		changed_file() {
			this.file = this.$refs.song.files[0]
		},
		async on_submit(e) {
			e.preventDefault()

			this.success = false
			this.error = false

			let form_data = new FormData()
			form_data.append("audio_file", this.file)

			try {
				let response = await axios.post(
					config.ENDPOINT + "songs/",
					form_data,
					{
						headers: {
							"Content-Type": "multipart/form-data",
							"Authorization": `Bearer ${user.get_user_access()}`,
						},
					}
				)

				this.success = true
			} catch (error) {
				this.error = true
			}
		},
	},
}
</script>
