<template>
  <div :class="$style.container">
    <div :class="$style.back">
      <nuxt-link to="/" :class="$style.catalog">← все товары</nuxt-link>
      <nuxt-link to="/" :class="$style.cross">
        <img src="../../assets/images/cross.jpg" alt="" />
      </nuxt-link>
    </div>
    <div :class="$style.content">
      <div :class="$style.image">
        <img :src="product.image" alt="" />
      </div>
      <div :class="$style.info">
        <div :class="$style.name">{{ product.name }}</div>
        <div :class="$style.code">Артикул: {{ product.code }}</div>
        <div :class="$style.price">{{ product.price }} р.</div>
        <button :class="$style.button">Добавить в корзину</button>
        <div :class="$style.description">{{ product.description }}</div>
        <div>{{ product.uuid }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  async mounted() {
    if (!('uuid' in this.product)) {
      await this.$store.dispatch(
        'products/getProduct',
        this.$route.params.product
      )
    }
  },
  computed: {
    product() {
      return this.$store.state.products.product
    },
  },
  beforeDestroy() {
    this.$store.commit('products/setProduct', {})
  },
}
</script>

<style lang="scss" module>
.container {
  padding: 2rem 1rem 0 1rem;
  max-width: 85rem;
  margin: 0 auto;
  @media (max-width: 500px) {
    padding: 1rem 0 0 0;
  }
  .back {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0 0 5rem 0;
    @media (max-width: 980px) {
      margin: 0 0 2rem 0;
    }
    .catalog {
      text-decoration: none;
      color: #000;
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
    font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
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
        color: grey;
        margin: 0 0 2rem 0;
      }
      .price {
        font-size: 1.2rem;
        font-weight: 500;
        margin: 0 0 2rem 0;
      }
      .button {
        cursor: pointer;
        color: #fff;
        background-color: #000;
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
