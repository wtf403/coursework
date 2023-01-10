import { createStore } from 'vuex';

export default createStore({
  state: {
    isAuth: false,
    userId: 0,
    inputs: {
      nameInput: {
        inputType: 'text',
        iconPath: require('@/assets/user-icon.svg'),
        placeholderText: 'Введите имя и фамилию',
      },
      emailInput: {
        inputType: 'email',
        iconPath: require('@/assets/email-icon.svg'),
        placeholderText: 'Введите почту',
      },
      passwordInput: {
        inputType: 'password',
        iconPath: require('@/assets/key-icon.svg'),
        placeholderText: 'Введите пароль',
      },
      searchInput: {
        inputType: 'text',
        iconPath: require('@/assets/search-icon.svg'),
        placeholderText: 'Введите название',
      },
    },
  },
  getters: {},
  mutations: {},
  actions: {},
  modules: {},
});
