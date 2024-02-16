<template>
  <section>
    <div>
      <h1>Error 404 Page not found</h1>
      <nuxt-link to="/" :class="$style.link">Назад</nuxt-link>
    </div>
  </section>
</template>

<style lang="scss" module>
section {
  max-width: 25rem;
  margin: 0 auto;
  padding: 10rem 1rem 0 1rem;
  & div {
    padding: 1rem;
    border: 0.125rem solid $red;
    border-radius: 0.3rem;
  }

  & h1 {
    color: $red;
    font-size: 2rem;
    margin: 0 0 2rem 0;
  }
  .link {
    color: $white;
    background-color: $blueBtn;
    padding: 0.5rem 1rem;
    border-radius: 0.3rem;
  }
}
</style>
