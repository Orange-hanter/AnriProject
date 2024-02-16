<template>
  <Modal>
    <template #body>
      <div :class="$style.content" v-if="content === 'choice'">
        <div :class="$style.title">Авторизуйтесь на сайте</div>
        <button :class="$style.button" @click="changeContent('reg')">
          Зарегистрироваться
        </button>
        <button :class="$style.button" @click="changeContent('auth')">
          Войти
        </button>
      </div>

      <div :class="$style.content" v-else-if="content === 'reg'">
        <div :class="$style.back" @click="changeContent('choice')">
          вернуться назад
        </div>
        <RegistrationForm />
      </div>

      <div :class="$style.content" v-else-if="content === 'auth'">
        <div :class="$style.back" @click="changeContent('choice')">
          вернуться назад
        </div>
        <SignInForm />
      </div>
    </template>
  </Modal>
</template>

<script>
import RegistrationForm from './RegistrationForm.vue'
import SignInForm from './SignInForm.vue'
import Modal from './layouts/Modal.vue'
export default {
  data() {
    return {
      content: 'choice',
    }
  },
  components: {
    RegistrationForm,
    SignInForm,
    Modal,
  },
  methods: {
    changeContent(value) {
      this.content = value
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
  .back {
    margin: 0 0 1rem 0;
    cursor: pointer;
  }
}
</style>
