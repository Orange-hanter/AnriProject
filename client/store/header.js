import Auth from '~/api/auth'
export const state = () => ({
  isOpen: false,
  isAuth: false,
  user: {},
})

export const mutations = {
  changeIsOpen(state) {
    state.isOpen = !state.isOpen
  },
  changeIsAuth(state) {
    state.isAuth = !state.isAuth
  },
  setUser(state, value) {
    state.user = value
  },
}

export const actions = {
  async login({ commit }, { email, username, password }) {
    const value = await Auth.login({ email, username, password })
    console.log(value);
    commit('setUser', value)
  },
}
