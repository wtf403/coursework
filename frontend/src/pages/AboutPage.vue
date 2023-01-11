<template>
  <img class="hero-image__inner" src="@/../public/kino-background.png" alt="">
  <h1>Подберите фильм или сериал по вкусу</h1>
</template>
<script>

export default {
};
</script>
<style lang="scss" scoped>
$wrapper: 1440px;


.hero-image__inner {
  position: absolute;
  top: 80px;
  right: 0;
  left: 0;
  z-index: 1;
  width: 100vw;
  height: min(100vh - 80px, 100vw / 2);
}
</style>
