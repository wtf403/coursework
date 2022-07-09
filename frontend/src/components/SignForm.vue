<template>
  <form class="form">
    <slot></slot>
  </form>
</template>
<script>
export default {};
</script>
<style lang="scss">
.form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.form > label,
.form > button {
  width: 100%;
  &:first-of-type {
    margin-top: 1em;
  }
}
</style>
