<template>
  <button class="btn btn--outline">
    <slot></slot>
  </button>
</template>
<script>

export default {
 name: 'my-button-outline' 
}
</script>
<style lang="scss" scoped>
    .btn--outline{
        background-color: rgba(0 0 0 / 0.2);
        border: 2px #7B6EF6 solid;
    }
</style>
