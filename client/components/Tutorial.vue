<template>
  <div @click="showProducts">
    click
    <div v-for="item in products" :key="item.id">
      <div>{{ item.name }}</div>
      <div>{{ item.description }}</div>
      <img :src="item.image" alt="" />
      <div>{{ item.code }}</div>
      <div>{{ item.price }}</div>
    </div>
  </div>
</template>

<script>
import Products from "~/api/products"
export default {
  async mounted() {
    this.products = await Products.get()

  },
data() {
  return {
    products: []
  }
},
  methods: {
    showProducts() {
      console.log(this.products)
    },
  },
}
</script>
