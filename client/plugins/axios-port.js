import { setClient } from '~/services/apiClient'

export default ({ app }) => {
  app.$axios.onError((error) => {
    return error.response
  })
  setClient(app.$axios)
}
