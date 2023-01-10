<template>
  <button class="btn" type="submit">
    <slot />
  </button>
</template>
<script>
export default {
  name: 'MyButton', 
};
</script>
<style lang="scss">
.btn {
  padding: 12px 20px;
  color: inherit;
  text-align: center;
  background-color: var(--accent-color);
  border: 2px solid transparent;
  border-radius: 12px;
  cursor: pointer;
}
</style>
