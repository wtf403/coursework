<template>
  <button class="btn" type="submit">
    <slot></slot>
  </button>
</template>
<script>
export default {
    name: 'my-button', 
};
</script>
<style lang="scss">
    .btn {
        color: inherit;
        border-radius: 12px;
        background-color: var(--accent-color);
        border: 2px solid transparent;
        padding: 12px 20px;
        text-align: center;
    }
</style>
