import config from "./config"

import axios from "axios"
import cookies from "js-cookie"

export default {
	set_user_logged(access, refresh, name) {
		cookies.set("access", access)
		cookies.set("refresh", refresh)
		cookies.set("name", name)
	},
	is_user_logged() {
		return cookies.get("access") != null
	},
	register(name, mail, password) {
		const user = {
			name: name,
			email: mail,
			password: password,
		}
		return axios.post(config.ENDPOINT + "user/create/", user)
	},
	login(username, password) {
		const user = {
			name: username,
			password: password,
		}
		return axios.post(config.ENDPOINT + "user/login/", user)
	},
}
