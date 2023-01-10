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
  padding: clamp(0.5rem, 0.5vw + 0.4rem, 0.75rem) clamp(1rem, 0.4vw + 0.9rem, 1.25rem);
  color: inherit;
  text-align: center;
  background-color: var(--accent-color);
  border: 2px solid transparent;
  border-radius: 12px;
  cursor: pointer;
}
</style>
