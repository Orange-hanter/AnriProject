import Products from '~/api/products'

const getTime = () => {
  const time = new Date()
  const nowTime = time.getHours() * 60 + time.getMinutes()
  return nowTime
}

export const state = () => ({
  products: [],
  product: {},
})

export const getters = {
  getTokenLifeTime(state, getters, rootState, rootGetters) {
    return rootGetters['auth/getTokenLifeTime']
  },
}

export const mutations = {
  setProducts(state, value) {
    state.products = value
  },
  setProduct(state, value) {
    state.product = value
  },
}

export const actions = {
  checkTime({ dispatch, getters }) {
    if (localStorage.getItem('time')) {
      if (getTime() - localStorage.getItem('time') > getters.getTokenLifeTime) {
        dispatch('auth/refresh', null, { root: true })
        dispatch('auth/verify', null, { root: true })
      }
    }
  },

  async getProducts({ commit, dispatch }) {
    commit('loader/setIsLoader', true, { root: true })

    dispatch('checkTime')

    const products = await Products.get()
    commit('setProducts', products)
    commit('loader/setIsLoader', false, { root: true })
  },

  async getProduct({ commit, dispatch }, id) {
    commit('loader/setIsLoader', true, { root: true })

    dispatch('checkTime')

    const product = await Products.getOne(id)
    commit('setProduct', product)
    commit('loader/setIsLoader', false, { root: true })
  },
}
