<template>
  <button class="btn btn--outline">
    <slot />
  </button>
</template>
<script>

export default {
  name: 'MyButtonOutline', 
};
</script>
<style lang="scss" scoped>
.btn--outline{
  background-color: rgba(0 0 0 / 0.2);
  border: 2px #7b6ef6 solid;
  cursor: pointer;
}
</style>
