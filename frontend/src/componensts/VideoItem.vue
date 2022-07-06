<template>
  <div class="video">
    <div>
      <h3>Видео {{ video.id }}</h3>
      <div><strong>Название:</strong> {{ video.title }}</div>
    </div>
    <div class="post__btns">
      <my-button
        @click="$router.push(`/videos/${video.id}`)"
      >
        Открыть
      </my-button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    video: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style scoped>
.video {
  padding: 15px;
  background-color: aliceblue;
}
</style>
