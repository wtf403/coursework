<template>
  <main class="login main">
    <img class="login__image" src="@/assets/login-image.png" alt="Login image">
    <h1 class="login__heading">
      Вход
    </h1>
    <form class="login__form form" @submit.prevent>
      <my-input v-model="userEmail" class="form__input" :input="$store.state.inputs.emailInput" />
      <my-input
        v-model="userPassword"
        class="form__input"
        :input="$store.state.inputs.passwordInput"
      />
      <p class="form__error">
        {{errorMessage}}&ensp;
      </p>
      <my-button class="form__btn" @click="logginHandler">
        Войти
      </my-button>
      <my-button-outline
        class="form__btn"
        @click="$router.push('/sign-up')"
      >
        Зарегистрироваться
      </my-button-outline>
    </form>
  </main>
</template>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      isLoading: false,
      userEmail: '',
      userPassword: '',
      errorMessage: '',
    };
  },
  methods: {
    logginHandler() {
      this.isLoading = true;
      axios({
        method: 'post',
        url: 'http://coursework.std-1724.ist.mospolytech.ru/api/user/login/',
        data: {
          email: this.userEmail || undefined,
          password: this.userPassword || undefined,
        },
      })
        .then((response) => {
          this.errorMessage = '';
          this.$store.state.isAuth = true;
          this.$store.state.userId = response.data.id;
          this.$router.push('/');
        })
        .catch((response) => {
          this.errorMessage = response.response.data.error;
        }).finally(() => {
          this.isLoading = false;
          window.localStorage.setItem('isAuth', this.$store.state.isAuth);
        });
    },
  },
};
</script>
<style lang="scss">
.login {
  display: grid;
  grid-template-rows: min-content 1fr;
  grid-template-columns: 1fr 1fr;
}

.login__image {
  grid-row: span 2;
  user-select: none;
}

.login__heading {
  font-size: clamp(1.75rem, 3vw + 1rem, 4rem);
}

.form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.form__input,
.form__btn {
  width: 100%;
  color: white;

  &:first-of-type {
    margin-top: 1em;
  }
}

.form__error {
  color: #eb4444;
  font-weight: bold;
  font-size: 1.5em;
  line-height: 1;
  text-align: center;
}

@media (max-width: 768px) {
  .login {
    grid-template-columns: 1fr;
  }

  .login__image {
    order: 2;
  }
}
</style>
