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
    commit('loader/setIsLoader', true, { root: true })
    const products = await Products.get()
    commit('setProducts', products)
    commit('loader/setIsLoader', false, { root: true })
  },
  async getProduct({ commit }, id) {
    commit('loader/setIsLoader', true, { root: true })
    const product = await Products.getOne(id)
    commit('setProduct', product)
    commit('loader/setIsLoader', false, { root: true })
  },
}
