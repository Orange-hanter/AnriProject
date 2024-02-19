import API from '~/services/apiClient'
import { Model } from './index'

class Cart extends Model {
  async set({ product, quantity }) {
    const response = await API.post('/carts/', {
      product,
      quantity,
    })

    return response.data
  }
}
export default new Cart('/carts')
