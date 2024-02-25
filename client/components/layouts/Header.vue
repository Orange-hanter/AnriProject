<template>
  <div :class="$style.container">
    <div :class="$style.content">
      <div :class="$style.column">
        <nuxt-link to="/" :class="$style.logo"> Menidyon </nuxt-link>
      </div>
      <div :class="$style.column">
        <div
          :class="[$style.burger, isOpen ? $style.open : '']"
          @click="openBurger"
        >
          <span></span>
        </div>
        <div :class="[$style.list, isOpen ? $style.open : '']">
          <nuxt-link to="/" :class="[$style.link, $style.effect]">
            <span @click="closeBurger">Каталог</span>
          </nuxt-link>
          <a :class="[$style.link, $style.effect]">
            <span @click="closeBurger">О нас</span>
          </a>
          <a :class="[$style.link, $style.effect]"
            ><span @click="closeBurger">Доставка</span></a
          >
          <a :class="[$style.link, $style.effect]"
            ><span @click="closeBurger">Контакты</span></a
          >
          <a :class="[$style.link, $style.effect]"
            ><span>+123 678 901 23</span></a
          >
          <a :class="[$style.link, $style.button]" @click="openLogin">войти</a>
          <a :class="$style.link">
            <img src="~/assets/images/login.svg" alt="" />
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    isOpen() {
      return this.$store.state.popups.isOpen
    },
  },
  methods: {
    openBurger() {
      this.$store.commit('popups/changeIsOpen')
      document.body.classList.toggle('lock')
    },
    openLogin() {
      this.$store.commit('popups/changeIsAuth')
      document.body.classList.add('lock')
    },
    closeBurger() {
      this.$store.commit('popups/changeIsOpen')
      document.body.classList.remove('lock')
    },
  },
}
</script>

<style lang="scss" module>
.container {
  position: fixed;
  width: 100%;
  padding: 2rem 0;
  background-color: $white;
  @media (max-width: 830px) {
    padding: 1rem 0;
    background-color: $black;
  }
  .content {
    padding: 0 3rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    @media (max-width: 950px) {
      padding: 0 1rem;
    }
    .column {
      .logo {
        font-size: 2rem;
        color: $black;
        @media (max-width: 830px) {
          position: relative;
          z-index: 10;
          color: $white;
        }
      }
      .list {
        display: flex;
        align-items: center;
        @media (max-width: 830px) {
          position: fixed;
          overflow: auto;
          width: 100%;
          height: 100%;
          top: 4rem;
          left: -100%;
          background-color: $white;
          padding: 3rem 0 0 0;
          transition: all 0.5s ease 0s;
          flex-direction: column;
          gap: 2rem;
        }
        .link {
          margin: 0 0 0 2rem;
          font-size: 1.2rem;
          color: $black;
          cursor: pointer;
          & img {
            width: 1.5rem;
            height: 1.5rem;
          }
          @media (max-width: 1000px) {
            margin: 0 0 0 1rem;
          }
          @media (max-width: 830px) {
            margin: 0 0 1.5rem 0;
            font-size: 1.5rem;
          }
        }
        .button {
          color: $white;
          background-color: $black;
          padding: 0.5rem;
          border-radius: 0.3rem;
        }
        .effect {
          position: relative;
          &:after {
            content: '';
            position: absolute;
            left: 0;
            bottom: 20%;
            opacity: 0;
            width: 100%;
            height: 0.0625rem;
            border-bottom: 0.15rem solid $black;
            -webkit-box-shadow: inset 0rem -0.0625rem 0rem 0rem $black;
            -moz-box-shadow: inset 0rem -0.0625rem 0rem 0rem $black;
            box-shadow: inset 0rem -0.0625rem 0rem 0rem $black;
            -webkit-transition: all 0.3s ease;
            transition: all 0.3s ease;
          }
          &:hover:after {
            opacity: 1;
            bottom: -0.2rem;
          }
        }
      }
      .list.open {
        left: 0;
      }
      .burger {
        display: none;
        @media (max-width: 830px) {
          display: block;
          position: absolute;
          cursor: pointer;
          top: 1.5625rem;
          right: 1rem;
          width: 1.875rem;
          height: 1.0625rem;
          z-index: 10;
          &::before {
            content: '';
            background-color: $white;
            position: absolute;
            width: 100%;
            height: 0.125rem;
            right: 0;
            transition: all 0.3s ease 0s;
            top: 0;
          }
          &::after {
            content: '';
            background-color: $white;
            position: absolute;
            width: 100%;
            height: 0.125rem;
            right: 0;
            transition: all 0.3s ease 0s;
            bottom: 0;
          }
          & span {
            background-color: $white;
            position: absolute;
            width: 100%;
            height: 0.125rem;
            right: 0;
            top: 0.4375rem;
            transition: all 0.3s ease 0s;
          }
        }
      }
      .burger.open {
        &::before {
          transform: rotate(45deg);
          top: 0.4375rem;
          background-color: $white;
        }
        &::after {
          transform: rotate(-45deg);
          bottom: 0.5rem;
          background-color: $white;
        }
        & span {
          background-color: $white;
          transform: scale(0);
        }
      }
    }
  }
}
</style>
