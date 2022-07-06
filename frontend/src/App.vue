<template>
  <header class="header">
    <img
      class="header__logo"
      @click="$router.push('/')"
      src="@/assets/logo-icon.svg"
      alt="Logotype"
    />
    <nav class="header__navigation">
      <router-link class="header__link" to="/">Главная</router-link>
      <router-link class="header__link" to="/about">О проекте</router-link>
      <router-link
        class="header__link"
        v-if="!($store.state.isAuth) && $route.name != 'sign-in'"
        to="/sign-in"
      >
        <img :src="require('@/assets/logout-icon.svg')" alt="Войти" />
        <span>Вход</span>
      </router-link>
      <router-link
        class="header__link"
        v-if="!($store.state.isAuth) && $route.name != 'sign-up'"
        to="/sign-up"
      >
        <img :src="require('@/assets/logout-icon.svg')" alt="Регистарция" />
        <span>Регистрация</span>
      </router-link>
      <router-link
        class="header__link"
        v-if="$store.state.isAuth"
        @click="logout"
        to="/about"
      >
        <img :src="require('@/assets/logout-icon.svg')" alt="Выйти" />
        <span>Выйти</span>
      </router-link>
    </nav>
  </header>

  <router-view />

  <footer class="footer">
    <a class="footer__link" href="https://gitlab.com/maaaaath/courcework">
      <img class="footer__logo" src="@/assets/logo-icon.svg" alt="Logotype" />
      Ссылка на GitLab
    </a>
    <p class="footer__text">Курсвовой проект студента группы 211-321 Киселева Максима Романовича</p>
    <p class="footer__text">Московский политехничесий университет, 2022</p>
  </footer>
</template>

<script>
import store from '@/store';

export default {
  data() {
    return {};
  },
  methods: {
    logout() {
      store.state.isAuth = false;
    }
  },
};
</script>

<style lang="scss">
#app {
  --accent-color: #7b6ef6;
  --background-color: #121829;
  background-color: var(--background-color);
  color: #c3c8d4;
  font-family: Roboto;
  font-size: clamp(0.75rem, 1vw + 0.5rem, 1.125rem);
  display: grid;
  grid-template-rows: min-content 1fr min-content;
  gap: 2rem;
  max-width: 1440px;
  width: 100%;
  margin: 0 auto;
  padding: 0 120px;
}
@media (max-width: 768px) {
  #app {
    padding: 0 20px;
  }
}
.header {
  display: flex;
  justify-content: space-between;
  padding: 20px 0;
}

.header__navigation {
  display: flex;
  gap: 30px;
}

.header__link {
  text-decoration: none;
  color: inherit;
  display: inline-grid;
  gap: 5px;
  grid-template-columns: max-content 1fr;
  align-items: center;
}

.footer {
  padding-top: auto;
  text-align: center;
  padding-bottom: 1rem;
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

.main {
  margin: 0 auto;
  max-width: 1440px;
  width: 100%;
}

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
  text-rendering: optimizeSpeed;
  line-height: 1.5;
}

/* A elements that don't have a class get default styles */
a:not([class]) {
  text-decoration-skip-ink: auto;
}

/* Make images easier to work with */
img,
picture {
  max-width: 100%;
  display: block;
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
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  border: 0;
  padding: 0;
  white-space: nowrap;
  clip-path: inset(100%);
  clip: rect(0 0 0 0);
  overflow: hidden;
}
</style>
