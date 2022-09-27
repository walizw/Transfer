<template>
  <Header :user-logged="userLogged" />

  <div class="content">
    <NavigationLeft :user-logged="userLogged" />

    <div class="content__middle">
      <router-view/>
    </div>
  </div>
</template>

<style>
  @import "./assets/styles.css";
</style>

<script>
  import Header from "./components/Header"
  import NavigationLeft from "./components/NavigationLeft"

  import auth from "@/logic/auth"

  export default {
      name: "App",
      components: {
	  Header,
	  NavigationLeft
      },
      computed: {
	  userLogged () {
	      return auth.getUserLogged ()
	  }
      }
  }
</script>
