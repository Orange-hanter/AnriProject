export const state = () => ({
  isLoader: false,
})

export const mutations = {
  setIsLoader(state, value) {
    state.isLoader = value
  },
}
