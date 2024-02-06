<template>
  <div>
    <Header />
    <RegModal v-if="$store.state.popups.isAuth" />
    <Loader v-if="$store.state.loader.isLoader" />
    <Nuxt />
  </div>
</template>

<script>
import Header from '~/components/layouts/Header.vue'
import RegModal from '~/components/RegModal.vue'
import Loader from '~/components/common/Loader.vue'
export default {
  components: {
    Header,
    RegModal,
    Loader,
  },
  mounted() {
    this.$store.dispatch('auth/initToken')
  },
}
</script>
