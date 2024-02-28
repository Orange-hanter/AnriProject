import Auth from '~/api/auth'
export const state = () => ({
  user: {},
  token: null,
})

export const actions = {
  async initToken({ state, dispatch, commit }) {
    commit('initToken')
    if (state.token && state.token !== 'undefined') {
      dispatch('refresh')
    }
  },

  async registration({ commit }, { email, username, password }) {
    const value = await Auth.registration({ email, username, password })
    commit('setUser', value)
  },

  async auth({ commit, dispatch }, { username, password }) {
    const value = await Auth.auth({ username, password })
    localStorage.setItem('accessToken', value.access)
    localStorage.setItem('refreshToken', value.refresh)
    commit('setToken', value.access)
    dispatch('refreshTokenTimeout')
    dispatch('verifyTokenTimeout')
  },

  async refresh({ commit, dispatch }) {
    const refresh = localStorage.getItem('refreshToken')
    const value = await Auth.refresh(refresh)
    if (!value.access) {
      localStorage.removeItem('accessToken')
      localStorage.removeItem('refreshToken')
      commit('deleteToken')
      location.reload()
      return
    }
    commit('setToken', value)
    localStorage.setItem('accessToken', value.access)
    dispatch('refreshTokenTimeout')
  },

  async verify({ dispatch }) {
    const refresh = localStorage.getItem('refreshToken')
    const value = await Auth.verify(refresh)
    if (value.status !== 200) {
      dispatch('refresh')
    }
    dispatch('verifyTokenTimeout')
  },

  async refreshTokenTimeout({ dispatch }) {
    setTimeout(() => dispatch('refresh'), 0.3 * 60 * 1000)
  },

  async verifyTokenTimeout({ dispatch }) {
    setTimeout(() => dispatch('verify'), 0.1 * 60 * 1000)
  },

  async deleteToken({ commit }) {
    localStorage.removeItem('accessToken')
    localStorage.removeItem('refreshToken')
    commit('deleteToken')
  },

  async activation(context, { uid, token }) {
    const value = await Auth.activation(uid, token)
    if (value.status >= 400) {
      return value.data.detail
    } else return ''
  },
}

export const mutations = {
  setUser(state, value) {
    state.user = value
  },
  setToken(state, value) {
    state.token = value
  },
  initToken(state) {
    state.token = localStorage.getItem('refreshToken') || null
  },
  deleteToken(state) {
    state.token = null
  },
}
