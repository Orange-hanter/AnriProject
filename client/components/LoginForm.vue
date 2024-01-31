<template>
  <div>
    <Form>
      <template #form>
        <div :class="$style.content">
          <form @submit.prevent="loginUser">
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
        </div>
      </template>
    </Form>
  </div>
</template>

<script>
import Form from './layouts/Form.vue'
export default {
  data() {
    return {
      email: '',
      username: '',
      password: '',
    }
  },
  components: {
    Form,
  },
  methods: {
    async loginUser() {
      const user = {
        email: this.email,
        username: this.username,
        password: this.password,
      }
      await this.$store.dispatch('header/login', user)
    },
  },
}
</script>

<style lang="scss" module>
.content {
  padding: 4rem;
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
