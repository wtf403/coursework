<template>
  <main class="register main">
    <img class="register__image" src="@/assets/register-image.png" alt="Login image">
    <h1 class="register__heading">Регистрация</h1>
    <sign-form class="register__form form" @submit.prevent>
      <my-input class="form__input" :input="$store.state.inputs.nameInput" />
      <my-input class="form__input" :input="$store.state.inputs.emailInput" />
      <my-input class="form__input" :input="$store.state.inputs.passwordInput" />
      <my-button class="form__btn" @click="registerHandler">Зарегистрироваться</my-button>
      <my-button-outline class="form__btn" @click="$router.push('/sign-in')">Уже есть аккаунт?</my-button-outline>
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
    registerHandler() {
    }
  },
};
</script>
<style lang="scss">
  .register {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: min-content 1fr;
  }
  .register__image {
    grid-row: span 2;
  }
  .register__heading {
    font-size: clamp(1.75rem, 3vw + 1rem, 4rem);
  }
  @media (max-width: 768px) {
    .register {
      grid-template-columns: 1fr;
    }
    .register__image {
      order: 2;
    }
  }
 
</style>
