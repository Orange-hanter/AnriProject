import API from '~/services/apiClient'
import { Model } from './index'

class Products extends Model {
  async get() {
    const response = await API.get("/products/")
    return response.data.result
  }

  async getOne(id) {
    const response = await API.get(`/products/${id}/`)
    return response.data
  }
}
export default new Products('/products')
