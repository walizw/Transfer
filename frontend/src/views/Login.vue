<template>
    <div class="container">
        <div class="row">

	          <form @submit="on_submit" class="col-md-8 align-self-center mx-auto p-5">
	              <div class="mb-3">
	                  <h1 class="text-light">Log Into Transfer!</h1>
	                  <h3 class="text-secondary">A decentralized library awaits for you!</h3>
	              </div>

	              <div class="alert alert-danger" role="alert" v-if="error">
	                  The provided credentials are wrong! Please check your username and password.
	              </div>

	              <div class="mb-3">
	                  <label for="input_name" class="form-label text-secondary">Username:</label>
	                  <input v-model="name" name="name" type="text" class="form-control"
		                       id="input_name">
	              </div>

	              <div class="mb-3">
	                  <label for="input_pass" class="form-label text-secondary">Password:</label>
	                  <input v-model="pass" name="pass" type="password" class="form-control"
		                       id="input_pass">
	              </div>

	              <button type="submit" class="btn btn-success" aria-describedby="ftext">Login</button>
	              <div id="ftext" class="form-text">Do not have an account yet?
	                  <router-link to="/register">Create one now!</router-link>
	              </div>
	          </form>
	          
        </div>
    </div>
</template>

<script>

import auth from "@/logic/auth"

export default {
	  name: "Login",
	  data () {
	      return {
		        name: "",
		        pass: "",
		        error: false
	      }
	  },
	  methods: {
	      async on_submit (e) {
		        e.preventDefault ()

		        try {
		            this.error = false
		            let response = await auth.login (this.name, this.pass)
		            auth.set_user_logged (response ["data"]["access"], response ["data"]["refresh"], this.name)

		            this.$router.go ("/")
		        }
		        catch (error) {
		            this.error = true
		        }
	      }
	  }
}
</script>
