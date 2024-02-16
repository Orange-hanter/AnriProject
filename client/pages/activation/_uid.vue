<template>
  <div>
    <div :class="$style.info" v-if="!isError">
      <div :class="$style.text">
        <p>Поздравляем, Вы успешно зарегистрировались!</p>
        <p>Теперь вы можете авторизоваться на сайте</p>
        <button @click="openLogin">войти</button>
      </div>
    </div>
    <div v-else :class="$style.error">{{ isError }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isError: null,
    }
  },
  async mounted() {
    this.isError = await this.$store.dispatch('auth/activation', {
      uid: this.$route.params.uid,
      token: this.$route.params.token,
    })
  },
  methods: {
    openLogin() {
      this.$store.commit('popups/changeIsAuth')
      document.body.classList.add('lock')
    },
  },
}
</script>

<style lang="scss" module>
.info {
  max-width: 40rem;
  margin: 0 auto;
  padding: 7rem 1rem 0 1rem;
  font-size: 1rem;
  @media (max-width: 650px) {
    font-size: 0.9rem;
    max-width: 25rem;
  }
  .text {
    color: $white;
    margin: 0 0 1rem 0;
    padding: 1rem;
    border-radius: 0.3rem;
    background-color: $black;
    & p {
      margin: 0 0 1rem 0;
    }
    & button {
      color: $black;
      background-color: $white;
      padding: 0.5rem 2rem;
      border-radius: 0.3rem;
      font-size: 1.05rem;
    }
  }
}
.error {
  padding: 15rem;
}
</style>
