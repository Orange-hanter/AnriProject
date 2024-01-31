import API from '~/services/apiClient'
import { Model } from './index'

class Auth extends Model {
  async login({ email, username, password }) {
    console.log("yes");
    const response = await API.post('/auth/users/', {
      email,
      username,
      password,
    })

    return response
  }
}
export default new Auth('/auth')
