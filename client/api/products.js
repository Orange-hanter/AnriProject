import API from '~/services/apiClient'
import { Model } from './index'

class Products extends Model {
  async get() {
    const path = '/products'
    const response = await API.get(path)
    return response.data.result
  }
}
export default new Products('/products')
