import config from "./config"

import axios from "axios"
import cookies from "js-cookie"

export default {
    get_user_name () {
	      return cookies.get ("name")
    },
    get_user_access () {
	      return cookies.get ("access")
    },
    get_user_refresh () {
	      return cookies.get ("refresh")
    }
}
