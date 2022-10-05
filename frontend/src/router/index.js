import { createRouter, createWebHistory } from "vue-router"

import Home from "../views/Home"
import Login from "../views/Login"
import Register from "../views/Register"
import Upload from "../views/Upload"
import Artist from "../views/Artist"
import Lyrics from "../views/Lyrics"
import Queue from "../views/Queue"
import Search from "../views/Search"
import Empty from "../views/Empty"

import auth from "../logic/auth"

const routes = [
	{
		path: "/",
		name: "Home",
		component: Home,
	},
	{
		path: "/login",
		name: "Login",
		component: Login,
	},
	{
		path: "/register",
		name: "Register",
		component: Register,
	},
	{
		path: "/upload",
		name: "Upload",
		component: Upload,
	},
	{
		path: "/artist/:id",
		name: "Artist",
		component: Artist,
	},
	{
		path: "/lyrics",
		name: "Lyrics",
		component: Lyrics,
	},
	{
		path: "/queue",
		name: "Queue",
		component: Queue,
	},
	{
		path: "/search/:query",
		name: "Search",
		component: Search,
	},
	{
		path: "/activity",
		name: "Activity",
		component: Empty,
	},
	{
		path: "/radio",
		name: "Radio",
		component: Empty,
	},
	{
		path: "/explore/songs",
		name: "Songs",
		component: Empty,
	},
	{
		path: "/explore/albums",
		name: "Albums",
		component: Empty,
	},
	{
		path: "/explore/artists",
		name: "Artists",
		component: Empty,
	},
]

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
})

router.beforeEach(async (to) => {
	const public_pages = ["/login", "/register"]
	const auth_required = !public_pages.includes(to.path)
	const authenticated = auth.is_user_logged()

	if (auth_required && !authenticated) {
		return "/login"
	}

	if (!auth_required && authenticated) return "/"
})

export default router
