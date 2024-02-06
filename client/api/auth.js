import API from '~/services/apiClient'
import { Model } from './index'

class Auth extends Model {
  async registration({ email, username, password }) {
    const response = await API.post('/auth/users/', {
      email,
      username,
      password,
    })
    return response.data
  }

  async auth({ username, password }) {
    const response = await API.post('/auth/jwt/create/', {
      username,
      password,
    })

    return response.data
  }

  async refresh(token) {
    const response = await API.post('/auth/jwt/refresh/', {
      refresh: token,
    })
    return response.data
  }

  async verify(token) {
    const response = await API.post('/auth/jwt/verify/', {
      token,
    })
    return response.data
  }
}
export default new Auth('/auth')
