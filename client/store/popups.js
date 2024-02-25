export const state = () => ({
  isOpen: false,
  isAuth: false,
})

export const mutations = {
  changeIsOpen(state) {
    state.isOpen = !state.isOpen
  },
  changeIsAuth(state) {
    state.isAuth = !state.isAuth
  },
}
