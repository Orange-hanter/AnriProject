<template>
  <div>
    <Header />
    <RegModal v-if="$store.state.header.isAuth" />
    <Nuxt />
  </div>
</template>

<script>
import Header from '~/components/layouts/Header.vue'
import RegModal from '~/components/RegModal.vue'
export default {
  components: {
    Header,
    RegModal,
  },
}
</script>
