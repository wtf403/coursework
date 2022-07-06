<template>
  <section v-if="videos.length > 0">
    <h3>Список видео</h3>
    <div name="user-list">
      <video-item
        v-for="video in videos"
        :video="video"
        :key="video.id"
      />
    </div>
    <my-switch v-model="currentPage" :options="pages"/>
  </section>
  <h2 v-else style="color: red">
    Ничего нет!
  </h2>
</template>

<script>
import VideoItem from './VideoItem.vue';
import MySwitch from './UI/MySwitch.vue';
export default {
  components: { VideoItem, MySwitch },
  props: {
    videos: {
      type: Array,
    }
  },
  data() {
    return {
      currentPage: '1',
      pages: [
        { name: '1', title: '1' },
        { name: '2', title: '2' },
        { name: '3', title: '3' },
      ],
    }
  }
}
</script>

<style>

</style>
