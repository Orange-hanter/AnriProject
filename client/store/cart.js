import Cart from '~/api/cart'
export const state = () => ({
  cart: {
    products: [],
    totalPrice: 0,
  },
  isOpen: false,
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

  async deleteProduct({ dispatch, commit }, uuid) {
    dispatch('products/checkTime', null, { root: true })
    await Cart.delete(uuid)
    commit('deleteProduct', uuid)
  },

  async changeQuantity({ dispatch, commit, state }, { id, product, quantity }) {
    dispatch('products/checkTime', null, { root: true })
    await Cart.patch({ id, product, quantity })
    const productIndex = state.cart.products.findIndex((i) => i.uuid === id)
    const item = state.cart.products[productIndex]
    commit('setQuantity', { item, quantity, productIndex })
    commit('setPrice', { item, quantity, productIndex })
  },
}

export const mutations = {
  setProducts(state, value) {
    state.cart.products = value.result
    state.cart.totalPrice = value.amount
  },
  setQuantity(state, { item, quantity, productIndex }) {
    item.quantity = quantity
    state.cart.products.splice(productIndex, 1, item)
  },
  setIsOpen(state, value) {
    state.isOpen = value
  },
  deleteProduct(state, id) {
    state.cart.products = state.cart.products.filter((i) => id !== i.uuid)

    state.cart.totalPrice = 0
    for (let i = 0; i < state.cart.products.length; i++) {
      state.cart.totalPrice =
        state.cart.totalPrice + state.cart.products[i].products_price
    }
  },
  setPrice(state, { item, quantity, productIndex }) {
    item.products_price = Number(item.product.price) * quantity
    state.cart.products.splice(productIndex, 1, item)

    state.cart.totalPrice = 0
    for (let i = 0; i < state.cart.products.length; i++) {
      state.cart.totalPrice =
        state.cart.totalPrice + state.cart.products[i].products_price
    }
  },
}
