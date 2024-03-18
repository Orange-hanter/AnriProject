import Cart from '~/api/cart'
export const state = () => ({
  cart: {
    products: [],
    totalPrice: null,
  },
})

export const actions = {
  async setProducts({ dispatch }, { product, quantity }) {
    dispatch('products/checkTime', null, { root: true })
    await Cart.set({ product, quantity })
  },

  async getProducts({ commit, dispatch }) {
    dispatch('products/checkTime', null, { root: true })
    const value = await Cart.get()
    commit('setProducts', value)
  },

  async deleteProduct({ dispatch }, uuid) {
    dispatch('products/checkTime', null, { root: true })
    await Cart.delete(uuid)
    dispatch('getProducts')
  },

  async changeQuantity({ dispatch }, product, quantity) {
    dispatch('products/checkTime', null, { root: true })
    await Cart.changeQuantity(product, quantity)
  },
}

export const mutations = {
  setProducts(state, value) {
    state.cart.products = value.result
    state.cart.totalPrice = value.amount
  },
}
