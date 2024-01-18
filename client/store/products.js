import Products from '~/api/products'
export const state = () => ({
  products: [],
})

export const mutations = {
  setProducts(state, value) {
    state.products = value
  },
}

export const actions = {
  async getProducts({ commit }) {
    const products = await Products.get()
    commit('setProducts', products)
  },
}
