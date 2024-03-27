<template>
  <div :class="$style.icon" @click="open">
    <img src="/images/cart.svg" alt="" />
    <span :class="$style.count">{{
      $store.state.cart.cart.products.length
    }}</span>
  </div>
</template>

<script>
export default {
  methods: {
    open() {
      this.$store.commit('cart/setIsOpen', true)
    },
  },
}
</script>

<style lang="scss" module>
.icon {
  cursor: pointer;
  position: fixed;
  top: 7rem;
  right: 1.5rem;
  background-color: $cartIconBg;
  border-radius: 50%;
  padding: 1.5rem;
  transition: transform 0.2s ease-in-out;
  &:hover {
    transform: scale(1.1);
  }
  & img {
    width: 2rem;
    height: 2rem;
  }
  .count {
    background-color: red;
    border-radius: 1.875rem;
    bottom: -3px;
    color: #fff;
    font-family: Arial, Helvetica, sans-serif;
    height: 1.875rem;
    line-height: 1.875rem;
    position: absolute;
    right: -3px;
    text-align: center;
    width: 1.875rem;
  }
}
</style>
