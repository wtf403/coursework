<template>
  <h1 class="about__heading">Подберите фильм или сериал по вкусу</h1> 
  <div class="about__video">
    <video playsinline autoplay muted loop src="@/../public/film-counter.mp4" id="backgroundVideo" />
  </div>

  <img class="about__down" v-svg-inline height="60" src="@/assets/arrows-down.svg" alt="К контенту">
  <p class="about__text">
    Поиск новых и интересных фильмов и сериалов может быть трудным, но с правильными рекомендациями это может стать намного проще! Здесь вы найдете самые последние и лучшие фильмы и сериалы, чтобы поднять ваше настроение. От драм и комедий до мультфильмов и триллеров - мы предлагаем вам все и готовы помочь вам найти правильный фильм или сериал для вашего вкуса!
  </p>
  <div class="about__images">
    <img class="about__proto" src="" alt="">
    <img class="about__proto" src="" alt="">
    <img class="about__proto" src="" alt="">
  </div>
</template>
<script>

export default {
};
</script>
<style lang="scss" scoped>
.about__heading {
  margin-top: 2rem;
  color: white;
  font-weight: 700;
  font-size: 2.5em;
  text-align: center;
}

.about__video {
  position: absolute;
  top: 20vh;
  right: 0;
  left: 0;
  background:
    repeating-radial-gradient(#000000 0 0.0001%, #ffffff 0 0.0002%) 50% 0/2500px 2500px,
    repeating-conic-gradient(#000000 0 0.0001%, #ffffff 0 0.0002%) 60% 60%/2500px 2500px;
  background-blend-mode: difference;
  // animation: b 0.2s infinite alternate;
}

@keyframes b {
  100% {
    background-position: 50% 0, 60% 50%;
  }
}

#backgroundVideo {
  width: 100%;
  padding: 5rem;
}

.about__down {
  position: absolute;
  bottom: 5rem;
  left: 50%;
  transform: translateX(-50%);
  animation: arrows 1s infinite alternate;
}

@keyframes arrows {
  0% {
    transform: translateX(-50%) translateY(0);
  }

  50% {
    transform: translateX(-50%) translateY(10px);
  }

  100% {
    transform: translateX(-50%) translateY(0);
  }
}

.about__text {
  margin-top: 100vh;
  font-size: 2rem;
  text-align: center;
}
</style>
