<template>
    <div class="user">
        <div class="user__notifications">
            <ion-icon name="notifications"></ion-icon>
        </div>

        <div class="user__inbox">
            <ion-icon name="cloud"></ion-icon>
        </div>

        <div class="user__info">
            <span class="user__info__img">
	              <img :alt="username" src="@/assets/images/profile_picture.jpg"
	                   class="img-responsive"/>
            </span>

            <span class="user__info__name">
	              <span class="first">Welcome, </span>
	              <span class="last">{{username}}</span>
            </span>
        </div>

        <div class="user__actions">
            <div class="dropdown">
	              <button class="dropdown-toggle" type="button" id="user_actions_dropdown"
		                           data-bs-toggle="dropdown" aria-expanded="false">
	                  <ion-icon name="chevron-down-outline"></ion-icon>
	              </button>

	              <ul class="dropdown-menu dropdown-menu-right" aria-labelledby="user_actions_dropdown">
	                  <li><a>Profile</a></li>
	                  <li><a>Settings</a></li>
	                  <li>
	                      <router-link to="/upload">Upload</router-link>
	                  </li>
	                  <li><a>Log Out</a></li>
	              </ul>
            </div>
        </div>
    </div>
</template>

<script>
import user from "@/logic/user"

export default {
    name: "UserTopbar",
    data () {
	      return {
	          username: ""
	      }
    },
    created () {
	      this.username = user.get_user_name ()
    }
}
</script>
