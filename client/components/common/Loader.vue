<template>
  <div :class="$style.container">
    <div :class="$style.loader"></div>
  </div>
</template>

<style lang="scss" module>
.container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  z-index: 10;
  .loader {
    position: fixed;
    overflow: auto;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    max-height: calc(100vh - 6rem);
    z-index: 10;

    width: 6rem;
    height: 6rem;
    border: 0.31125rem solid $black;
    border-radius: 50%;
    display: inline-block;
    position: relative;
    box-sizing: border-box;
    animation: rotation 2s linear infinite;

    &::after {
      content: '';
      box-sizing: border-box;
      position: absolute;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%);
      width: 5rem;
      height: 5rem;
      border-radius: 50%;
      border: 0.31125rem solid;
      border-color: yellow transparent;
    }
  }
}

@keyframes rotation {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
