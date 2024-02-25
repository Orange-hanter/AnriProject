<template>
  <div :class="$style.content" @click="open">
    <div :class="$style.image">
      <img :src="item.image" alt="" />
    </div>
    <div :class="$style.name">
      {{ item.name }}
    </div>
    <div :class="$style.price">{{ item.price }} р.</div>
  </div>
</template>
<script>
export default {
  props: {
    item: Object,
  },
  methods: {
    open() {
    this.$store.commit("products/setProduct", this.item)
      this.$router.push({
        name: 'product',
        params: { product: this.item.uuid },
      })
    },
  },
}
</script>
<style lang="scss" module>
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
      margin: 0 0 0.3rem 0;
    }
  }
  .price {
    @media (max-width: 480px) {
      font-size: 0.8rem;
    }
  }
}
</style>
