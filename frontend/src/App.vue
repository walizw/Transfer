<template>
  <Header />
  <router-view/>
</template>

<style>
  @import "./assets/styles.css";
</style>

<script>
    import Header from "./components/Header"

  export default {
      name: "App",
      components: {
	  Header
      }
  }
</script>
