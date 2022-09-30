<template>
    <div class="modal fade" :id="`update_album${album_id}_modal`" tabindex="-1"
         role="dialog" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">

                <div class="modal-header">
                    <h5 class="modal-title">Update {{album_name}}</h5>
                    <button class="button-dark close" type="button"
                            data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>

                <form @submit="update_album">
                    <div class="modal-body">

                        <div class="form-group mb-3">
                            <label for="input_name">Name:</label>
                            <input name="name" type="text" v-model="album_name"
                                   class="form-control" id="input_name" />
                        </div>

                        <div class="form-group mb-3">
                            <label for="input_year">Year:</label>
                            <input name="year" type="text" v-model="album_year"
                                   class="form-control" id="input_year" />
                        </div>

                        <div class="form-group mb-3">
                            <label for="album_artwork">Artwork:</label>
                            <input name="artwork" type="file"
                                   @change="changed_file" ref="artwork"
                                   class="form-control" />
                        </div>

                        <div class="alert alert-danger" role="alert" v-if="error">
	                          There's been an error updating this album.
	                      </div>

	                      <div class="alert alert-success" role="alert" v-if="success">
	                          Album updated successfully (now you have to reload the page.)
	                      </div>

                    </div>

                    <div class="modal-footer">
                        <button type="submit" class="button-dark">
                            Update
                        </button>
                    </div>
                </form>

            </div>
        </div>
    </div>
</template>

<script>
import config from "@/logic/config.js"
import user from "@/logic/user.js"

import axios from "axios"

export default {
    name: "UpdateAlbumModal",
    props: {
        album_id: Number,
        album_artist: String,
        album_name: String,
        album_year: String
    },
    data () {
        return {
            album_artwork: "",
            success: false,
            error: false
        }
    },
    methods: {
        changed_file () {
            this.album_artwork = this.$refs.artwork.files [0]
        },
        async update_album (e) {
            e.preventDefault ()

            this.success = false
            this.error = false

            let form_data = new FormData ()
            if (this.album_name)
                form_data.append ("name", this.album_name)

            if (this.album_artist)
                form_data.append ("artist_id", this.album_artist)

            if (this.album_year)
                form_data.append ("year", this.album_year)

            if (this.album_artwork)
                form_data.append ("artwork", this.album_artwork)

            try {
                let response = await axios.put (
                    config.ENDPOINT + "album/" + this.album_id + "/update/",
                    form_data,
                    {
                        headers: {
                            "Content-Type": "multipart/form-data",
                            "Authorization": `Bearer ${user.get_user_access ()}`
                        }
                    }
                )

                this.success = true
            } catch (err) {
                console.log (err)
                this.error = true
            }
        }
    }
}
</script>
