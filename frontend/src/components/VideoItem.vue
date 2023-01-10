<template>
  <router-link :to="`/videos/${video.id}`" class="video" @click="selectVideo">
    <img
      class="video__image"
      :srcset="video.image_url_x2 + ' 2x'"
      :src="video.image_url"
      alt=""
    >
    <h3 class="video__title">{{video.title}}</h3>
  </router-link>
</template>

<script>
export default {
  props: {
    video: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
    };
  },
  methods: {
    selectVideo() {
    
      
    },
  },
};
</script>

<style scoped>
.video {
  display: flex;
  flex-direction: column;
  justify-content: start;
  max-width: 18em;
  padding: clamp(0.313rem, 1vw, 0.938rem);
  text-decoration: none;
  background-color: rgba(32 40 62 / 0.5);
  border-radius: 12px;
  cursor: pointer;
  backdrop-filter: blur(22px);
}


.video__title {
  display: -webkit-box;
  max-width: 100%;
  margin-bottom: auto;
  margin-bottom: 1em;
  padding: 1em 0.5em;
  padding-bottom: 0;
  overflow: hidden;
  color: white;
  font-weight: 400;
  font-size: 1em;
  text-overflow: ellipsis;
  word-wrap: break-word;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}

.video__image {
  display: block;
  object-fit: cover;
  aspect-ratio: 2 / 3;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 8px;
}
</style>
