<template>
  <div :class="$style.container">
    <div :class="$style.back">
      <nuxt-link to="/" :class="$style.catalog">← все товары</nuxt-link>
      <nuxt-link to="/" :class="$style.cross">
        <img src="/images/cross.svg" alt="" />
      </nuxt-link>
    </div>
    <div :class="$style.content">
      <div :class="$style.image">
        <img :src="product.image" alt="" />
      </div>
      <div :class="$style.info">
        <div :class="$style.name">{{ product.name }}</div>
        <div :class="$style.code">Артикул: {{ product.code }}</div>
        <div :class="$style.code">
          количество на складе: {{ product.quantity_in_stock }}
        </div>
        <div :class="$style.price">{{ product.price }} р.</div>
        <button :class="$style.button" @click="addToCart">
          {{ btnText }}
        </button>
        <div :class="$style.description">{{ product.description }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      btnText: 'добавить в корзину',
    }
  },
  async mounted() {
    await this.$store.dispatch(
      'products/getProduct',
      this.$route.params.product
    )
    if (!('uuid' in this.product)) {
      this.$router.push('/error')
    }

    const productIndex = this.$store.state.cart.cart.products.findIndex(
      (i) => i.product.uuid === this.product.uuid
    )
    const item = this.$store.state.cart.cart.products[productIndex]
    if (item) {
      this.btnText = 'перейти в корзину'
    }
  },
  computed: {
    product() {
      return this.$store.state.products.product
    },
    cart() {
      return this.$store.state.cart.cart
    },
  },
  beforeDestroy() {
    this.$store.commit('products/setProduct', {})
  },

  methods: {
    async addToCart() {
      const productIndex = this.$store.state.cart.cart.products.findIndex(
        (i) => i.product.uuid === this.product.uuid
      )
      const item = this.$store.state.cart.cart.products[productIndex]
      if (item) {
        this.$store.commit('cart/setIsOpen', true)
      } else {
        this.btnText = 'перейти в корзину'
        const value = {
          product: this.product.uuid,
          quantity: 1,
        }
        await this.$store.dispatch('cart/setProducts', value)
        await this.$store.dispatch('cart/getProducts')
      }
    },
  },
}
</script>

<style lang="scss" module>
.container {
  padding: 10rem 2rem;
  max-width: 85rem;
  margin: 0 auto;
  @media (max-width: 830px) {
    padding: 5rem 1rem;
  }
  .back {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0 0 1rem 0;
    @media (max-width: 980px) {
      margin: 0 0 2rem 0;
    }
    .catalog {
      text-decoration: none;
      color: $black;
    }
    .cross {
      cursor: pointer;
      max-width: 2rem;
      max-height: 2rem;
      & img {
        width: 100%;
        height: 100%;
      }
    }
  }
  .content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    max-width: 75rem;
    margin: 0 auto;
    @media (max-width: 980px) {
      display: block;
      max-width: 35rem;
    }
    .image {
      max-width: 35rem;
      max-height: 35rem;
      margin: 0 3rem 0 0;
      @media (max-width: 980px) {
        width: 100%;
        margin: 0 0 2rem 0;
      }
      & img {
        width: 100%;
        height: 100%;
      }
    }
    .info {
      .name {
        font-size: 1.5rem;
        margin: 0 0 1rem 0;
      }
      .code {
        color: $grey;
        margin: 0 0 2rem 0;
      }
      .price {
        font-size: 1.2rem;
        font-weight: 500;
        margin: 0 0 2rem 0;
      }
      .button {
        cursor: pointer;
        color: $white;
        background-color: $black;
        border: none;
        padding: 1rem 2rem;
        border-radius: 0.3rem;
        font-weight: 600;
        margin: 0 0 3rem 0;
      }
      .description {
        margin: 0 0 1rem 0;
      }
    }
  }
}
</style>
