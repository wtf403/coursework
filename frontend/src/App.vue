<template>
  <header class="header">
    <a href="/">
      <img
        class="header__logo"
        src="@/assets/logo-icon.svg"
        alt="Logotype"
        @click="$router.push('/')"
      >
    </a>
    <nav class="header__navigation">
      <router-link class="header__link" to="/">Главная</router-link>
      <router-link class="header__link" to="/about">О проекте</router-link>
      <router-link
        v-if="!$store.state.isAuth && $route.name != 'sign-in'"
        class="header__link"
        to="/sign-in"
      >
        <img :src="require('@/assets/logout-icon.svg')" alt="Войти">
        <span>Вход</span>
      </router-link>
      <router-link
        v-if="!$store.state.isAuth && $route.name != 'sign-up'"
        class="header__link"
        to="/sign-up"
      >
        <img :src="require('@/assets/logout-icon.svg')" alt="Регистарция">
        <span>Регистрация</span>
      </router-link>
      <router-link v-if="$store.state.isAuth" class="header__link" to="/sign-in" @click="logout">
        <img :src="require('@/assets/logout-icon.svg')" alt="Выйти">
        <span>Выйти</span>
      </router-link>
    </nav>
  </header>

  <router-view class="main" />

  <footer class="footer">
    <a class="footer__link" href="https://github.com/wtf403/coursework">
      <img class="footer__logo" src="@/assets/logo-icon.svg" alt="Logotype">
      Ссылка на GitLab
    </a>
    <p class="footer__text">
      Курсвовой проект студента группы 211-321 Киселева Максима Романовича
    </p>
    <p class="footer__text">
      Московский политехничесий университет, 2023
    </p>
  </footer>
  <div class="backgroud-video">
    <video playsinline autoplay muted loop src="/background.mp4" id="backgroundVideo" />
  </div>
</template>

<script>

export default {
  data() {
    return {};
  },
  created() {
    this.$store.state.isAuth = window.localStorage.getItem('isAuth') === 'true';
    this.$store.state.userId = window.localStorage.getItem('userId');
  },
  mounted() {
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    mediaQuery.addEventListener('change', checkBackgroundVideoPlay);
    function checkBackgroundVideoPlay() {
      if (mediaQuery.matches) {
        document.querySelector('#backgroundVideo').pause();
      } else {
        document.querySelector('#backgroundVideo').play();
      }
    }
    checkBackgroundVideoPlay();
  },
  methods: {
    logout() {
      this.$store.state.isAuth = false;
      window.localStorage.setItem('isAuth', false);
    },
  },
};
</script>
<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

#app {
  --accent-color: #7b6ef6;
  --background-color: #121829;
  --darken-blur: rgba(18 24 41 / 0.2);
  display: grid;
  grid-template-rows: min-content 1fr min-content;
  gap: 2rem;
  width: 100%;
  max-width: 1440px;
  margin: 0 auto;
  padding: 0 clamp(1.25rem, 10vw - 1.25rem, 7.5rem);
  color: white;
  font-size: clamp(0.5rem, 1vw + 0.5rem, 1.125rem);
  font-family: 'Roboto', sans-serif;
  background-color: var(--background-color);
}

.header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 100vm;
  padding: 20px 0;
  background-color: var(--darken-blur);
  box-shadow: 0 0 0 100vmax var(--darken-blur);
  clip-path: inset(0 -100vmax);
}

.header__navigation {
  display: flex;
  gap: clamp(0.313rem, 1vw, 0.938rem);
}

.header__link {
  display: inline-grid;
  grid-template-columns: max-content 1fr;
  align-items: center;
  gap: 5px;
  color: inherit;
  text-decoration: none;
  cursor: pointer;
}

.footer {
  padding-top: auto;
  padding-bottom: 1rem;
  text-align: center;
}

.footer__link {
  display: inline-grid;
  grid-template-columns: max-content 1fr;
  align-items: center;
  gap: 5px;
  color: inherit;
}

.footer__logo {
  display: inline;
}

.backgroud-video {
  position: absolute;
  inset: 0;
  z-index: -1;
  isolation: isolate;

  & > video {
    position: fixed;
    inset: 0;
    z-index: -2;
    width: 100%;
    height: 100vh;
    object-fit: cover;
  }

  &::after {
    position: fixed;
    z-index: -1;
    width: 100%;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.42);
    content: '';
    object-fit: cover;
  }
}

/* CSS RESET */

/* Box sizing rules */

*,
*::before,
*::after {
  box-sizing: border-box;
}

/* Remove default margin */

body,
h1,
h2,
h3,
h4,
p,
figure,
blockquote,
dl,
dd {
  margin: 0;
}

/* Remove list styles on ul, ol elements with a list role, which suggests default styling will be removed */

ul[role='list'],
ol[role='list'] {
  list-style: none;
}

/* Set core root defaults */

html:focus-within {
  scroll-behavior: smooth;
}

/* Set core body defaults */

body {
  min-height: 100vh;
  text-rendering: optimizespeed;
  line-height: 1.5;
}

/* A elements that don't have a class get default styles */

a:not([class]) {
  text-decoration-skip-ink: auto;
}

/* Make images easier to work with */

img,
picture {
  display: block;
  max-width: 100%;
}

/* Inherit fonts for inputs and buttons */

input,
button,
textarea,
select {
  font: inherit;
}

/* Remove all animations, transitions and smooth scroll for people that prefer not to see them */

@media (prefers-reduced-motion: reduce) {
  html:focus-within {
    scroll-behavior: auto;
  }

  *,
  *::before,
  *::after {
    transition-duration: 0.01ms !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
  }
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  white-space: nowrap;
  border: 0;
  clip: rect(0 0 0 0);
  clip-path: inset(100%);
}

@media print {
  .header {
    display: none;
  }

  *,
  *::before,
  *::after {
    box-sizing: border-box;
    color: #000000 !important;
    color: black !important;
    font-size: 10pt !important;
    text-shadow: none !important;
    background: #ffffff !important;

    /* Black prints faster */
    box-shadow: none !important;
  }

  #app {
    position: relative;
    height: max-content;
    margin: 1cm !important;
  }

  .backgroud-video {
    display: none;
  }

  .footer {
    margin-top: auto;
    transform: translateX(-1cm);
  }
}
</style>
