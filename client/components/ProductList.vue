<template>
  <div :class="$style.container">
    <div v-for="item in products" :key="item.id" :class="$style.content">
      <div :class="$style.image">
        <img :src="item.image" alt="" />
      </div>
      <div :class="$style.name">
        {{ item.name }}
      </div>
      <div :class="$style.price">{{ item.price }} р.</div>
    </div>
  </div>
</template>

<script>
export default {
  async mounted() {
    await this.$store.dispatch("products/getProducts")
  },
  computed: {
    products() {
      return this.$store.state.products.products
    }
  }
}
</script>
<style lang="scss" module>
.container {
  font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
  max-width: 70rem;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 1.5rem;
  @media (max-width: 1020px) {
    gap: 1rem;
    grid-template-columns: 1fr 1fr 1fr;
  }
  @media (max-width: 840px) {
    grid-template-columns: 1fr 1fr;
  }
  .content {
    margin: 0 0 4rem 0;
    @media (max-width: 840px) {
      margin: 0 0 2rem 0;
    }
    .image {
      max-width: 18rem;
      max-height: 18rem;
      margin: 0 0 1rem 0;
      @media (max-width: 840px) {
        max-width: 25rem;
        max-height: 25rem;
      }
      @media (max-width: 480px) {
        max-width: 25rem;
        max-height: 25rem;
      }
      & img {
        width: 100%;
        height: 100%;
      }
    }
    .name {
      margin: 0 0 1rem 0;
      @media (max-width: 480px) {
        font-size: 0.8rem;
        margin:0 0 0.3rem 0;
      }
    }
    .price {
      @media (max-width: 480px) {
        font-size: 0.8rem;
      }
    }
  }
}
</style>
