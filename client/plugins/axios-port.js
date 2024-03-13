import { setClient } from '~/services/apiClient'

export default ({ app, store }) => {
  app.$axios.onError((error) => {
    return error.response
  })

  app.$axios.onRequest((config) => {
    const newConfig = { ...config }
    if (store && store.state.auth.token) {
      newConfig.headers.Authorization = `anri ${store.state.auth.token}`
    }

    return newConfig
  })

  setClient(app.$axios)
}
