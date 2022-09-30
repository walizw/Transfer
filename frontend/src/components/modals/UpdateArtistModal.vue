<template>
    <div class="modal fade" id="update_artist_modal" tabindex="-1" role="dialog"
         aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">

                <div class="modal-header">
                    <h5 class="modal-title">Update {{artist_name}}</h5>
                    <button class="button-dark close" type="button" data-dismiss="modal"
                            aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>

                <form @submit="update_artist">
                    <div class="modal-body">


                        <div class="form-group mb-3">
                            <label for="input_name">Name:</label>
                            <input name="name" type="text" v-model="artist_name"
                                   class="form-control" id="input_name" />
                        </div>

                        <div class="form-group mb-3">
                            <label for="area_bio">About:</label>
                            <textarea cols="30" id="area_bio" name="bio"
                                      rows="10" v-model="artist_bio"
                                      class="form-control"></textarea>
                        </div>

                        <div class="form-group mb-3">
                            <label for="input_pfp">Profile Picture</label>
                            <input name="pfp" type="file" class="form-control"
                                   @change="changed_file" ref="pfp" />
                        </div>

                        <div class="alert alert-danger" role="alert" v-if="error">
	                          There's been an error updating this artist.
	                      </div>

	                      <div class="alert alert-success" role="alert" v-if="success">
	                          Artist updated successfully (now you have to reload the page.)
	                      </div>
                    </div>

                    <div class="modal-footer">
                        <button type="submit" class="button-dark">Update</button>
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
    name: "UpdateArtistModal",
    props: {
        artist_id: Number,
        artist_name: String,
        artist_bio: String,
    },
    data () {
        return {
            artist_pfp: "",
            success: false,
            error: false
        }
    },
    methods: {
        changed_file () {
            this.artist_pfp = this.$refs.pfp.files [0]
        },
        async update_artist (e) {
            e.preventDefault ()

            this.success = false
            this.error = false

            let form_data = new FormData ()
            if (this.artist_name)
                form_data.append ("name", this.artist_name)

            if (this.artist_bio)
                form_data.append ("bio", this.artist_bio ? this.artist_bio : "")

            if (this.artist_pfp)
                form_data.append ("pfp", this.artist_pfp)

            try {
                let response = await axios.put (
                    config.ENDPOINT + "artist/" + this.artist_id + "/update/",
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
