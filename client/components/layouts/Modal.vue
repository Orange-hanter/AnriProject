<template>
  <div :class="$style.popup">
    <div :class="$style.overlay" @click="close"></div>
    <div :class="$style.content">
      <div :class="$style.close" @click="close">
        <img src="/images/cross.svg" alt="" />
      </div>
      <div :class="$style.body">
        <slot name="body"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    close() {
      this.$store.commit('popups/changeIsAuth')
      if (!this.$store.state.popups.isOpen) {
        document.body.classList.remove('lock')
      }
    },
  },
}
</script>

<style lang="scss" module>
.popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  z-index: 10;
  .overlay {
    cursor: pointer;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(4, 4, 4, 0.4);
    backdrop-filter: blur(1.25rem);
    transition: opacity 0.3ms;
    z-index: 10;
    animation: expand 0.2s ease-in-out;
  }
  .content {
    position: fixed;
    overflow: auto;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    max-height: calc(100vh - 6.5rem);
    z-index: 10;
    background-color: $white;
    border: 0.125rem solid $black;
    border-radius: 0.3rem;
    .close {
      position: absolute;
      top: 0.5rem;
      right: 0.5rem;
      & img {
        width: 1.5rem;
        height: 1.5rem;
        cursor: pointer;
      }
    }
  }
}
</style>
