<template>
  <div class="video">
    <div class="video__image" />
    <div class="video__title" />
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
    selectVideo() {},
  },
};
</script>

<style lang="scss" scoped>
.video {
  display: flex;
  flex-direction: column;
  justify-content: end;
  max-width: 18em;
  padding: clamp(0.313rem, 1vw, 0.938rem);
  background-color: rgba(32 40 62 / 0.5);
  border-radius: 12px;
  cursor: pointer;
  backdrop-filter: blur(22px);
}

.video__title {
  margin-top: 15px;
  margin-bottom: 5px;
  padding: 1em 0.5em;
  font-weight: 400;
  font-size: 1em;
  line-height: 1.5;
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
}

.video__image {
  position: relative;
  display: block;
  width: 100%;
  border-radius: 8px;
  clip-path: inset(0);
  object-fit: cover;
  aspect-ratio: 2 / 3;

  &::after {
    position: absolute;
    display: block;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    border-radius: 12px;
    transform: translateX(-100%);
    animation: loading 1.5s infinite;
    content: '';
  }

  @keyframes loading {
    100% {
      transform: translateX(100%);
    }
  }
}
</style>
