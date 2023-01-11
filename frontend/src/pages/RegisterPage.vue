<template>
  <main class="register main">
    <img class="register__image" height="600" src="@/assets/register-image.png" alt="Login image">
    <h1 class="register__heading">
      Регистрация
    </h1>
    <form class="register__form form" @submit.prevent>
      <my-input v-model="userName" class="form__input" :input="$store.state.inputs.nameInput" />
      <my-input v-model="userEmail" class="form__input" :input="$store.state.inputs.emailInput" />
      <my-input
        v-model="userPassword"
        class="form__input"
        :input="$store.state.inputs.passwordInput"
      />
      <p class="form__error">
        {{errorMessage}}&ensp;
      </p>
      <my-button class="form__btn" @click="registerHandler">
        Зарегистрироваться
      </my-button>
      <my-button-outline
        class="form__btn"
        @click="$router.push('/sign-in')"
      >
        Уже есть аккаунт?
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
      userName: '',
      userEmail: '',
      userPassoword: '',
      errorMessage: '',
    };
  },
  methods: {
    registerHandler() {
      this.isLoading = true;
      let userNameSplitArray = this.userName.split(/(\s+)/).filter(function(e) {
        return e.trim().length > 0;
      });
      if (userNameSplitArray.length > 2) {
        this.errorMessage = 'Неверное имя';
        return;
      } else {
        let [firstName, lastName] = userNameSplitArray;
        axios({
          method: 'post',
          url: 'http://coursework.std-1724.ist.mospolytech.ru/api/user/register/',
          data: {
            first_name: firstName,
            last_name: lastName,
            email: this.userEmail || undefined,
            password: this.userPassword || undefined,
          },
        })
          .then((response) => {
            if (response.data.massage === 'success') {
              this.$store.state.isAuth = true;
              this.$router.push({ path: '/' });
            }
          })
          .catch((response) => {
            this.errorMessage = response.response.data.error || response.response.data.email[0];
          })
          .finally(() => {
            this.isLoading = false;
            window.localStorage.setItem('isAuth', this.$store.state.isAuth);
            window.localStorage.setItem('isAuth', this.$store.state.userId);
          });
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.register {
  display: grid;
  grid-template-rows: min-content 1fr;
  grid-template-columns: 1fr 1.2fr;
}

.register__image {
  grid-row: span 2;
  user-select: none;
}

.register__heading {
  font-size: clamp(1.75rem, 3vw + 1rem, 4rem);
}

.form__btn {
  color: white;
}

.form__error {
  color: #eb4444;
  font-weight: bold;
  font-size: 1.5em;
  line-height: 1;
  text-align: center;
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
