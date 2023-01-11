<template>
  <div class="about__video">
    <video playsinline autoplay muted loop src="@/../public/film-counter.mp4" id="backgroundVideo" />
  </div>
  <h1 class="about__heading">Подбери фильм или сериал под своё настроение</h1>

  <a href="#text">
    <img class="about__down" v-svg-inline height="60" src="@/assets/arrows-down.svg" alt="К контенту">
  </a>
  <my-button @click="$router.push('/')" class="calltoaction">
    Подобрать фильм
  </my-button>
  <p class="about__text" id="text">
    Поиск новых и интересных фильмов и сериалов может быть трудным, но с правильными рекомендациями это может стать намного проще! Здесь вы найдете самые последние и лучшие фильмы и сериалы, чтобы поднять ваше настроение. От драм и комедий до мультфильмов и триллеров - мы предлагаем вам все и готовы помочь вам найти правильный фильм или сериал для вашего вкуса!
  </p>
  <section class="about__images">
    <a-image :preview="{ visible: false }"
             src="https://burst.shopifycdn.com/photos/a-film-reel-lays-tangled-against-a-white-background.jpg?width=373&format=pjpg&exif=1&iptc=1"
             @click="visible = true" />
    <div style="display: none;">
      <a-image-preview-group :preview="{ visible, onVisibleChange: vis => (visible = vis) }">
        <a-image src="https://burst.shopifycdn.com/photos/three-woman-watch-a-glowing-white-screen-in-a-dark-room.jpg?width=925&format=pjpg&exif=1&iptc=1" />
        <a-image src="https://burst.shopifycdn.com/photos/spilled-popcorn-on-a-red-background.jpg?width=925&format=pjpg&exif=1&iptc=1" />
        <a-image src="https://burst.shopifycdn.com/photos/a-silver-film-reel-canister-and-a-movie-clapper-board.jpg?width=925&format=pjpg&exif=1&iptc=1" />
      </a-image-preview-group>
    </div>
  </section>
  <section class="about__accardion">
    <a-collapse style="max-width: 600px; margin: 0 auto;" v-model:activeKey="activeKey" :bordered="false">
      <a-collapse-panel key="1" header="Как я могу получить рекомендации фильмов и сериалов?">
        <p>
          Для получения рекомендаций фильмов и сериалов вам нужно зарегистрироваться на нашем сайте. После регистрации вы сможете получать рекомендации на основе ваших предпочтений.
        </p>
      </a-collapse-panel>
      <a-collapse-panel key="2" header="Какие виды контента вы предлагаете?">
        <p>Пока что доступно разделение на фильмы и сериалы</p>
      </a-collapse-panel>
      <a-collapse-panel key="3" header="Какие фильмы пользуются наибольшей популярностью у пользователей?">
        <p>
          Мы предлагаем рекомендации по всем видам фильмов и сериалов, включая драмы, комедии, фантастику и даже детские фильмы. Вы можете выбрать любой вид фильма или сериала, который вам интересен.
        </p>
      </a-collapse-panel>
    </a-collapse>
  </section>
</template>
<script>
import { ref } from 'vue';
export default {
  data() {
    return {
      show: true,
      visible: ref(false),
    }; 
  },
};
</script>
<style lang="scss" scoped>
body {
  scroll-behavior: smooth;
}

.about__heading {
  color: white;
  font-weight: 700;
  font-size: clamp(1.75rem, 5vw + 0.5rem, 4.313rem);
  text-align: center;
}


.about__video {
  position: absolute;
  top: 18vh;
  right: 0;
  bottom: 15vh;
  left: 0;
  background:
    repeating-radial-gradient(#000000 0 0.0001%, #ffffff 0 0.0002%) 50% 0/2500px 2500px,
    repeating-conic-gradient(#000000 0 0.0001%, #ffffff 0 0.0002%) 60% 60%/2500px 2500px;
  background-blend-mode: difference;
  animation: b 0.2s infinite alternate;
}

.about__accardion {
  max-width: 60%;
  font-weight: bold;
  font-size: 2rem;
  margin-inline: auto;
}

@keyframes b {
  100% {
    background-position: 50% 0, 60% 50%;
  }
}

#backgroundVideo {
  width: 100%;
  object-fit: cover;
  height: 100%;
  padding: clamp(1.75rem, 5vw + 0.5rem, 4.313rem);
  border-radius: 12px;
}

.about__down {
  position: absolute;
  bottom: 5rem;
  left: 50%;
  color: white;
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

.calltoaction {
  margin-top: 100vh;
  font-size: clamp(0.75rem, 5vw + 0.5rem, 3.313rem);
}

.about__text {
  font-size: 2rem;
  text-align: center;
}


.about__images {
  max-width: 50%;
  margin: 0 auto;
}

.about__phtoto {
  display: block;
  width: 100%;
}
</style>
