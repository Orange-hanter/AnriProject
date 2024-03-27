<template>
  <div :class="$style.container">
    <div :class="$style.popup">
      <div :class="$style.overlay" @click="close"></div>
      <div :class="$style.content">
        <div :class="$style.close" @click="close">
          <img src="/images/cross.svg" alt="" />
        </div>
        <div :class="$style.body" v-if="products.length !== 0">
          <div :class="$style.title">Ваш заказ:</div>
          <div :class="$style.items">
            <div :class="$style.item" v-for="item in products" :key="item.uuid">
              <img :src="item.product.image" alt="" :class="$style.image" />
              <div>
                {{ item.product.name }}
                {{ item.product.code }}
              </div>
              <div>{{ item.product.price }}р.</div>
              <div>{{ item.quantity }}</div>
              <div>
                <span
                  @click="
                    quantity(item.uuid, item.product.uuid, item.quantity + 1)
                  "
                  >+</span
                >
                <span
                  @click="
                    quantity(item.uuid, item.product.uuid, item.quantity - 1)
                  "
                  >-</span
                >
              </div>
              <div :class="$style.delete" @click="deleteProduct(item.uuid)">
                <img src="/images/cross.svg" alt="" />
              </div>
            </div>
          </div>
          <div :class="$style.totalSum">Сумма: {{ totalPrice }}р.</div>
          <button :class="$style.button">Checkout</button>
        </div>
        <div :class="$style.body" v-else>корзина пуста</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  async mounted() {
    await this.$store.dispatch('cart/getProducts')
  },
  computed: {
    products() {
      return this.$store.state.cart.cart.products
    },
    totalPrice() {
      return this.$store.state.cart.cart.totalPrice
    },
  },
  methods: {
    close() {
      this.$store.commit('cart/setIsOpen', false)
    },

    async deleteProduct(uuid) {
      await this.$store.dispatch('cart/deleteProduct', uuid)
    },

    async quantity(cartId, productId, quantity) {
      if (quantity === 0) {
        this.deleteProduct(cartId)
      } else {
        const info = {
          id: cartId,
          product: productId,
          quantity: quantity,
        }
        await this.$store.dispatch('cart/changeQuantity', info)
      }
    },
  },
}
</script>

<style lang="scss" module>
.container {
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
          .item {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin: 0 0 1rem 0;
            .image {
              max-width: 4rem;
              max-height: 4rem;
              border-radius: 0.5rem;
            }
            .delete {
              max-width: 1rem;
              max-height: 1rem;
              border: 0.0625rem solid $black;
              border-radius: 50%;
              padding: 0.1rem;
              cursor: pointer;
              & img {
                width: 100%;
                height: 100%;
              }
            }
          }
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
