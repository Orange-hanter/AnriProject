import Cart from '~/api/cart'
export const state = () => ({
  products: [],
})

export const actions = {
  async products({ commit }, { product, quantity }) {
    const value = await Cart.set({ product, quantity })
    commit('setProducts', value)
  },
}

export const mutations = {
  setProducts(state, value) {
    state.products = value
  },
}
