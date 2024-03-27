<template>
  <div :class="$style.content">
    <form @submit.prevent="authUser" v-if="!isLogin">
      <input
        :class="$style.input"
        type="text"
        placeholder="логин"
        v-model="username"
      />
      <input
        :class="$style.input"
        type="password"
        placeholder="пароль"
        v-model="password"
      />
      <button :class="$style.button">Войти</button>
    </form>
    <div :class="$style.message" v-else>Вы успешно авторизованы</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      isLogin: false,
    }
  },
  methods: {
    async authUser() {
      const user = {
        username: this.username,
        password: this.password,
      }
      await this.$store.dispatch('auth/auth', user)
      await this.$store.dispatch('cart/getProducts')
      this.isLogin = true
    },
  },
}
</script>

<style lang="scss" module>
.content {
  .input {
    display: block;

    padding: 0.5rem;
    margin: 0 0 1rem 0;
    background-color: $black;
    color: $white;
    border-radius: 0.3rem;
  }
  .button {
    display: block;
    width: 100%;
    padding: 0.5rem;
    margin: 0 0 1rem 0;
    background-color: $black;
    color: $white;
    border-radius: 0.3rem;
  }
}
</style>
