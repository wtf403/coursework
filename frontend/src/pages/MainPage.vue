<template>
  <main class="main">
    <h1 class="main__heading">Главная</h1>
    <my-switch v-model="currentCategory" :options="categories"></my-switch>
    <video-list :videos="videos" />
  </main>
</template>

<script>
import VideoList from '@/components/VideoList';
import axios from 'axios';
export default {
  components: {
    VideoList,
  },
  data() {
    return {
      isVideosLoading: false,
      videos: [],
      currentCategory: 'all',
      categories: [
        { name: 'all', title: 'Всё' },
        { name: 'film', title: 'Фильмы' },
        { name: 'series', title: 'Сериалы' },
      ],
    };
  },
  methods: {
    async fetchVideos() {
      try {
        this.isVideosLoading = true;
        const response = await axios.get('https://jsonplaceholder.typicode.com/posts');
        this.videos = response.data;
      } catch (e) {
        alert('Ошибка загрузки видео');
      } finally {
        this.isVideosLoading = false;
      }
    },
  },
  mounted() {
    this.fetchVideos();
  },
};
</script>

<style></style>
