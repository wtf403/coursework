<template>
  <section v-if="videos.length > 0">
    <h3>Список видео</h3>
  </section>
  <h2 v-else style="color: red;">
    Ничего нет!
  </h2>
</template>

<script>
export default {
  props: {
    videos: {
      type: Array,
    },
  },
  data() {
    return {
    };
  },
};
</script>

