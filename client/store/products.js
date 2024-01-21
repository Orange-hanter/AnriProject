import Products from '~/api/products'
export const state = () => ({
  products: [],
  product: {},
})

export const mutations = {
  setProducts(state, value) {
    state.products = value
  },
  setProduct(state, value) {
    state.product = value
  },
}

export const actions = {
  async getProducts({ commit }) {
    const products = await Products.get()
    commit('setProducts', products)
  },
  async getProduct({ commit }, id) {
    const product = await Products.getOne(id)
    commit('setProduct', product)
  },
}
