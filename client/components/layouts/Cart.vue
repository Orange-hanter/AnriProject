<template>
  <div :class="$style.container">
    <div
      :class="$style.icon"
      @click="openCart"
      v-if="$store.state.cart.products.length !== 0"
    >
      <img src="/images/cart.svg" alt="" />
      <span :class="$style.count">{{ $store.state.cart.products.length }}</span>
    </div>

    <div :class="$style.popup" v-if="isOpen">
      <div :class="$style.overlay" @click="isOpen = false"></div>
      <div :class="$style.content">
        <div :class="$style.close" @click="isOpen = false">
          <img src="/images/cross.svg" alt="" />
        </div>
        <div :class="$style.body">
          <div :class="$style.title">Ваш заказ:</div>
          <div :class="$style.items">
            dcdcdcdcdcdcdcdccddccdcdcddcdcdcddcdcdcdcdcdcdcdccddccdcdcddcdcdcd
            dcdcdcdcdcdcdcdccddccdcdcddcdcdcddcdcdcdcdcdcdcdccddccdcdcddcdcdcd
            dcdcdcdcdcdcdcdccddccdcdcddcdcdcdcdcdcdcdcdcdcdccddccdcdcddcdcdcd
            dcdcdcdcdcdcdcdccddccdcdcddcdcdcd
            dcdcdcdcdcdcdcdccddccdcdcddcdcdcddcdcdcdcdcdcdcdccddccdcdcddcdcdcd
            dcdcdcdcdcdcdcdccddccdcdcddcdcdcddcdcdcdcdcdcdcdccddccdcdcddcdcdcd
            dcdcdcdcdcdcdcdccddccdcdcddcdcdcddcdcdcdcdcdcdcdccddccdcdcddcdcdcd
            dcdcdcdcdcdcdcdccddccdcdcddcdcdcddcdcdcdcdcdcdcdccddccdcdcddcdcdcd
            dcdcdcdcdcdcdcdccddccdcdcddcdcdcddcdcdcdcdcdcdcdccddccdcdcddcdcdcd
            dcdcdcdcdcdcdcdccddccdcdcddcdcdcddcdcdcdcdcdcdcdccddccdcdcddcdcdcd
            dcdcdcdcdcdcdcdccddccdcdcddcdcdcddcdcdcdcdcdcdcdccddccdcdcddcdcdcd
            dcdcdcdcdcdcdcdccddccdcdcddcdcdcddcdcdcdcdcdcdcdccddccdcdcddcdcdcd
            dcdcdcdcdcdcdcdccddccdcdcddcdcdcddcdcdcdcdcdcdcdccddccdcdcddcdcdcd
            dcdcdcdcdcdcdcdccddccdcdcddcdcdcddcdcdcdcdcdcdcdccddccdcdcddcdcdcd
          </div>
          <div :class="$style.totalSum">Сумма:</div>
          <button :class="$style.button">Checkout</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false,
    }
  },
  methods: {
    openCart() {
      this.isOpen = true
    },
  },
}
</script>

<style lang="scss" module>
.container {
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
  .popup {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    z-index: 10;
    .overlay {
      cursor: pointer;
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.8);
      z-index: 15;
    }
    .content {
      .close {
        position: absolute;
        top: 1rem;
        right: 1rem;
        z-index: 15;
        & img {
          width: 2rem;
          height: 2rem;
          cursor: pointer;
          filter: brightness(0) invert(1);
        }
      }
      .body {
        position: fixed;
        overflow: auto;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        max-height: calc(100vh - 6.5rem);
        background-color: $white;
        padding: 4rem 8rem;
        z-index: 15;

        .title {
          font-size: 1.2rem;
          margin: 0 0 2rem 0;
        }
        .items {
          border-top: 0.0625rem solid $black;
          border-bottom: 0.0625rem solid $black;
          padding: 1rem 0;
          margin: 0 0 2rem 0;
        }
        .totalSum {
          margin: 0 0 2rem 0;
          text-align: right;
        }
        .button {
          width: 100%;
          background-color: $black;
          padding: 1rem;
          text-align: center;
          color: $white;
          font-size: 1.1rem;
          font-weight: 700;
        }
      }
    }
  }
}
</style>
