<template>
  <div class="about__video">
    <video playsinline autoplay muted loop src="@/../public/film-counter.mp4" id="backgroundVideo" />
  </div>
  <h1 class="about__heading">Подбери фильм или сериал под своё настроение</h1>

  <a href="#text">
    <img class="about__down" v-svg-inline height="60" src="@/assets/arrows-down.svg" alt="К контенту">
  </a>
  <my-button-outline @click="$router.push('/')" class="calltoaction">
    Перейти в каталог 
  </my-button-outline>
  <p class="about__text" id="text">
    Поиск новых и интересных фильмов и сериалов может быть трудным, но с правильными рекомендациями это может стать намного проще! Здесь вы найдете самые последние и лучшие фильмы и сериалы, чтобы поднять ваше настроение. От драм и комедий до мультфильмов и триллеров - мы предлагаем вам все и готовы помочь вам найти правильный фильм или сериал для вашего вкуса!
  </p>
  <div class="about__images">
    <img class="about__proto" src="https://burst.shopifycdn.com/photos/a-film-reel-lays-tangled-against-a-white-background.jpg?width=925&format=pjpg&exif=1&iptc=1" alt="">
    <img class="about__proto" src="https://burst.shopifycdn.com/photos/film-reel-taggled-against-a-white-background.jpg?width=925&format=pjpg&exif=1&iptc=1" alt="">
    <img class="about__proto" src="https://burst.shopifycdn.com/photos/a-film-reel-lays-flat-catching-the-sunlight.jpg?width=925&format=pjpg&exif=1&iptc=1" alt="">
  </div>
  <v-content>
    <v-card class="mx-auto" max-width="344">
      <v-img src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" height="200px" cover />
      
      <v-card-title>
        Top western road trips
      </v-card-title>
      
      <v-card-subtitle>
        1,000 miles of wonder
      </v-card-subtitle>
      
      <v-card-actions>
        <v-btn color="orange-lighten-2" variant="text">
          Explore
        </v-btn>
      
        <v-spacer />
      
        <v-btn :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'" @click="show = !show" />
      </v-card-actions>
      
      <v-expand-transition>
        <div v-show="show">
          <v-divider />
      
          <v-card-text>
            I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for
            sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add
            a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
          </v-card-text>
        </div>
      </v-expand-transition>
    </v-card>
    <div class="feedback">
      <div class="feedback__wrapper">
        <p class="feedback__subtitle">Ваша рецензия</p>
        <h2 class="feedback__title">Поделитесь своим мнением<br>о Magical Misadventures</h2>
        <form class="feedback__form" onsubmit="event.preventDefault()">
          <!-- <div class="feedback__field">
                            <label for="feedbackName" class="feedback__label">Ваше имя</label>
                            <input v-model="name" type="text" id="feedbackName" class="feedback__input" required>
                        </div> -->
          <div class="feedback__field">
            <v-text-field v-model="name"
                          :rules="nameRules"
                          label="Имя пользователя*"
                          solo
                          required
                          append-icon="mdi-account" />
          </div>
          <div class="feedback__field">
            <v-textarea clearable
                        v-model="comment"
                        required
                        solo
                        name="CommentInput"
                        label="Текст комментария*" />
          </div>
          <!-- <div class="feedback__field">
                            <label for="feedbackComment" class="feedback__label">Ваш комментарий</label>
                            <textarea v-model="comment" id="feedbackComment" style="resize: vertical" rows="6"
                                class="feedback__input" required></textarea>
                        </div> -->
          <button class="feedback__button" @click="SendComment()">Отправить</button>
        </form>
      </div>
    </div>
  </v-content>
</template>
<script>
export default {
  data() {
    return {
      show: true,
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
  // animation: b 0.2s infinite alternate;
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
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 2rem;
  margin-block: 5rem;
}

.about__phtoto {
  display: block;
  width: 100%;
}
</style>
