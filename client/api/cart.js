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

  async get() {
    const response = await API.get('/carts/')
    return response.data
  }

  async delete(uuid) {
    const response = await API.delete(`/carts/${uuid}/`)
    return response
  }

  async changeQuantity(product, quantity) {
    const response = await API.patch(`/carts/${product}/`, quantity)
    return response
  }
}
export default new Cart('/carts')
