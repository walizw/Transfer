<template>
  <form class="search" @submit="onSubmit">
    <input type="text" placeholder="Search" v-model="query" name="query"/>
  </form>
</template>

<script>
    export default {
	name: "Search",
	data () {
	    return {
		query: ""
	    }
	},
	methods: {
	    onSubmit (e) {
		e.preventDefault ()

		alert (`TODO: Buscar ${this.query}`)
	    }
	}
    }
</script>
