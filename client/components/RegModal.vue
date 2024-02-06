<template>
  <div>
    <Modal>
      <template #body>
        <div :class="$style.content">
          <div :class="$style.title">Авторизуйтесь на сайте</div>
          <button :class="$style.button" @click="login">
            Зарегистрироваться
          </button>
          <button :class="$style.button" @click="auth">Войти</button>
        </div>
      </template>
    </Modal>
    <RegistrationFormVue v-if="isLogin" />
    <SignInForm v-if="isAuth" />
  </div>
</template>

<script>
import Modal from './layouts/Modal.vue'
import RegistrationFormVue from './RegistrationForm.vue'
import SignInForm from './SignInForm.vue'
export default {
  data() {
    return {
      isAuth: false,
      isLogin: false,
    }
  },
  components: {
    Modal,
    RegistrationFormVue,
    SignInForm,
  },
  methods: {
    auth() {
      this.isAuth = !this.isAuth
    },
    login() {
      this.isLogin = !this.isLogin
    },
  },
}
</script>

<style lang="scss" module>
.content {
  padding: 4rem;
  .title {
    font-size: 1.2rem;
    margin: 0 0 2rem 0;
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
