<template>
  <main class="not-found">
    <div class="not-found__info">
      <h1 class="not-found__heading">404. Страница не&nbsp;найдена</h1>
      <p class="not-found__text">Возможно, она была перемещена, или вы просто неверно указали адрес страницы.</p>
      <my-button class="not-fount__btn">На главную</my-button>
    </div>
    <video autoplay loop muted class="not-found__video" src="@/assets/not-found.mp4"></video>
  </main>
</template>
<script>

export default {
  
}
</script>
<style lang="scss">
.not-found {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 3em;
}

.not-found__info {
  display: flex;
  flex-direction: column;
  gap: 1em;
}

.not-fount__btn {
  width: fit-content
}

.not-found__video {
  width: 100%;
}
@media (max-width: 768px) {
  .not-found {
    grid-template-columns: 1fr;
    max-width: 80%;
    margin: 0 auto;
  }
  .not-found__video {
    order: -1;
  }
}

</style>
