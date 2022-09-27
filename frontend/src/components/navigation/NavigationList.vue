<template>
  <div class="navigation__list">
    <div class="navigation__list__header" type="button"
	    data-bs-toggle="collapse" :data-bs-target="'#' + id"
	    aria-expanded="true" :aria-controls="id">
      {{name}}
    </div>

    <div class="collapse show" :id="id">
      <div v-for="elm in content">
	<router-link :to="elm.url" class="navigation__list__item">
	  <ion-icon :name="elm.icon" class="ion-icon"></ion-icon>
	  {{elm.name}}
	</router-link>
      </div>
    </div>

  </div>
</template>

<script>
    export default {
	name: "NavigationList",
	props: {
	    id: String,
	    name: String,
	    content: Array
	}
    }
</script>
