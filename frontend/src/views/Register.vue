<template>
    <div class="middle_scroll">
        <div class="container">
            <div class="row">

	              <form @submit="on_submit" class="col-md-8 align-self-center mx-auto p-5">
	                  <div class="mb-3">
	                      <h1 class="text-light">Welcome to Transfer!</h1>
	                      <h3 class="text-secondary">A valley of freedom and decentralization is waiting for you!</h3>
	                  </div>

	                  <div class="alert alert-danger" role="alert" v-if="error">
	                      There's been an error, please check you've filled all the fields or the passwords match!
	                  </div>

	                  <div class="mb-3">
	                      <label for="input_name" class="form-label text-secondary">Username:</label>
	                      <input v-model="name" name="name" type="text" class="form-control"
		                           id="input_name" aria-describedby="name_help">
	                      <div id="name_help" class="form-text">
	                          It cannot include spaces, only alphanumeric characters.
	                      </div>
	                  </div>

	                  <div class="mb-3">
	                      <label for="input_mail" class="form-label text-secondary">Email:</label>
	                      <input v-model="mail" name="mail" type="email" class="form-control"
		                           id="input_mail">
	                  </div>

	                  <div class="mb-3">
	                      <div class="row">
                            <div class="col">
		                            <label for="input_pass1" class="form-label text-secondary">Enter your password:</label>
		                            <input v-model="pass1" name="pass1" type="password" class="form-control"
		                                   id="input_pass1"/>
	                          </div>

                            <div class="col">
		                            <label for="input_pass2" class="form-label text-secondary">Confirm your password:</label>
		                            <input v-model="pass2" name="pass2" type="password" class="form-control"
		                                   id="input_pass2"/>
	                          </div>
	                      </div>
	                  </div>

	                  <button class="btn btn-success" type="submit">Sign Up</button>
	                  <div class="form-text">Already have an account?
	                      <router-link to="/login">Log In</router-link>.
	                  </div>
	              </form>

            </div>
        </div>
    </div>
</template>

<script>
import auth from "@/logic/auth"

export default {
	  name: "Register",
	  data () {
	      return {
		        name: "",
		        mail: "",
		        pass1: "",
		        pass2: "",
		        error: false
	      }
	  },
	  methods: {
	      async on_submit (e) {
		        e.preventDefault ()

		        if (this.pass1 != this.pass2)
		        {
		            this.error = true
		            return
		        }

		        try {
		            this.error = false
		            let response = await auth.register (this.name, this.mail, this.pass1)
		            this.$router.push ("/login")
		        }
		        catch (error) {
		            this.error = true
		        }
	      }
	  }
}
</script>
