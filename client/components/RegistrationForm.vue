<template>
  <div :class="$style.content">
    <form @submit.prevent="regUser" v-if="!isButtonCliked">
      <input
        :class="$style.input"
        type="text"
        placeholder="email"
        v-model="email"
      />
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
      <button :class="$style.button">зарегистрироваться</button>
    </form>
    <div :class="$style.message" v-else>
      Вы почти завершили процесс регистрации! Вам на почту будет оптравлено
      сообщение для верефикации, после её подтверждения Вы будете успешно
      зарегестрированы
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      username: '',
      password: '',
      isButtonCliked: false,
    }
  },
  methods: {
    async regUser() {
      if (this.email !== '' && this.username !== '' && this.password !== '') {
        const user = {
          email: this.email,
          username: this.username,
          password: this.password,
        }
        await this.$store.dispatch('auth/registration', user)
        this.isButtonCliked = true
      }
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
