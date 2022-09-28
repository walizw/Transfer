import config from "./config"

import axios from "axios"
import cookies from "js-cookie"

export default {
    set_user_logged (access, refresh) {
	cookies.set ("access", access)
	cookies.set ("refresh", refresh)
    },
    get_user_logged () {
	return cookies.get ("access")
    },
    register (name, mail, password1, password2) {
    },
    login (username, password) {
	const user = {
	    "name": username,
	    "password": password
	}
	return axios.post (config.ENDPOINT + "user/login/", user)
    },
}
