<template>
    <div class="media-card">
        <div @click="$emit('clicked', item_id)" class="media-card__image"
             :style="[image ? {'background': 'url(' + image + ')'} : {'background': 'url(' + fallback_image + ')'}]">
            <ion-icon v-if="icon" :name="icon"></ion-icon>
        </div>

        <div class="media-card__footer">
            <div v-if="name && name1">
                <p class="text-truncate">
                    <router-link :to="url">{{name}}</router-link> By<br>
                    <router-link :to="url1">{{name1}}</router-link>
                </p>
            </div>

            <div v-if="name && !name1">
                <router-link :to="url">{{name}}</router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "MediaCard",
    props: {
        item_id: Number,
        image: String,
        fallback_image: String,
        icon: String,
        name: String,
        url: String,
        name1: String,
        url1: String
    }
}
</script>
