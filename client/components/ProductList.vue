<template>
  <div :class="$style.container">
    <Product
      v-for="item in products"
      :key="item.id"
      :item="item"
      :class="$style.content"
    />
  </div>
</template>

<script>
export default {
  async mounted() {
    await this.$store.dispatch('products/getProducts')
  },
  computed: {
    products() {
      return this.$store.state.products.products
    },
  },
}
</script>
<style lang="scss" module>
.container {
  font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
  max-width: 70rem;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  justify-content: center;
  gap: 1.5rem;
  padding: 10rem 1rem 0 1rem;
  @media (max-width: 1020px) {
    gap: 1rem;
    grid-template-columns: 1fr 1fr 1fr;
  }
  @media (max-width: 840px) {
    grid-template-columns: 1fr 1fr;
  }
}
</style>
