<template>
  <div>
    <Header />
    <CartIcon v-if="$store.state.cart.cart.products.length > 0" />
    <Cart v-if="$store.state.cart.isOpen" />
    <RegModal v-if="$store.state.popups.isAuth" />
    <Loader v-if="$store.state.loader.isLoader" />
    <Nuxt />
  </div>
</template>

<script>
import Header from '~/components/layouts/Header.vue'
import RegModal from '~/components/RegModal.vue'
import Loader from '~/components/common/Loader.vue'
import Cart from '~/components/layouts/Cart.vue'
import CartIcon from '~/components/layouts/CartIcon.vue'
export default {
  components: {
    Header,
    RegModal,
    Loader,
    Cart,
    CartIcon,
  },
  async mounted() {
    this.$store.dispatch('auth/initToken')

    if (this.$store.state.auth.token !== null) {
      await this.$store.dispatch('cart/getProducts')
    }
  },
}
</script>
