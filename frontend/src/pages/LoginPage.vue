<template>
  <main class="login main">
    <img class="login__image" src="@/assets/login-image.png" alt="Login image">
    <h1 class="login__heading">Вход</h1>
    <sign-form class="login__form form" @submit.prevent>
      <my-input class="form__input" :input="$store.state.inputs.emailInput" />
      <my-input class="form__input" :input="$store.state.inputs.passwordInput" />
      <my-button class="form__btn" @click="logginHandler">Войти</my-button>
      <my-button-outline class="form__btn" @click="$router.push('/sign-up')">Зарегистрироваться</my-button-outline>
    </sign-form>
  </main>
</template>
<script>
import SignForm from '@/componensts/SignForm'
export default {
  components: {
    SignForm
  },
  data() {
    return {};
  },
  methods: {
    logginHandler() {
  
    }
  },
};
</script>
<style lang="scss">
  .login {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: min-content 1fr;
  }
  .login__image {
    grid-row: span 2;
  }
  .login__heading {
    font-size: clamp(1.75rem, 3vw + 1rem, 4rem);
  }
  .form {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .form__input, .form__btn {
    width: 100%;
    &:first-of-type {
      margin-top: 1em;
    }
  }
  @media (max-width: 768px) {
    .login{
      grid-template-columns: 1fr;
    
    }
    .login__image{
      order: 2;
    }
  }
 
</style>
