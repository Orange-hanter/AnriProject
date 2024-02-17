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
    commit('setToken', value.access)
    localStorage.setItem('accessToken', value.access)
    localStorage.setItem('refreshToken', value.refresh)
    dispatch('refreshTokenTimeout')
  },

  async refresh({ commit, dispatch }) {
    const access = localStorage.getItem('accessToken')
    const data = await Auth.verify(access)
    commit('setToken', data)

    const refresh = localStorage.getItem('refreshToken')
    const value = await Auth.refresh(refresh)
    commit('setToken', value.access)
    localStorage.setItem('accessToken', value.access)
    localStorage.setItem('refreshToken', value.refresh)
    dispatch('refreshTokenTimeout')
  },

  async verify({ commit }) {
    const access = localStorage.getItem('accessToken')
    const value = await Auth.verify(access)
    commit('setToken', value)
    // localStorage.setItem('refreshToken', value.refresh)
    //dispatch('refreshTokenTimeout')
  },

  async refreshTokenTimeout({ dispatch }) {
    setTimeout(() => dispatch('refresh'), 0.25 * 60 * 1000)
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
}
