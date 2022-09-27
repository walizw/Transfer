<template>
  <header>

    <div class="page-flows">
      <span class="flow">
	<ion-icon name="chevron-back-outline"></ion-icon>
		  <!-- @click="$router.back ()"></ion-icon> -->
      </span>

      <span class="flow">
	<ion-icon name="chevron-forward-outline"></ion-icon>
		  <!-- @click="$router.forward ()"></ion-icon> -->
      </span>
    </div>

    <Search />
    <UserTopbar v-if="userLogged" />

  </header>
</template>

<script>
  import Search from "./header/Search"
  import UserTopbar from "./header/UserTopbar"

  export default {
      name: "Header",
      components: {
	  Search,
	  UserTopbar
      },
      props: {
	  userLogged: Object
      }
  }
</script>
