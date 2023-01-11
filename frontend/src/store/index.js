import { createStore } from 'vuex';

export default createStore({
  state: {
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
    comments: [],
    setCommentsLoading: false,
  },
  getters: {
    allComments(state) {
      return state.comments;
    },
  },
  mutations: {
    setCommentsLoading(state, bool) {
      state.commentsLoading = bool;
    },
    setComments(state, comments) {
      state.comments = comments;
    },

  },
  actions: {
    async fetchComments(ctx) {
      ctx.commit('setCommentsLoading', true);
      const res = await fetch('https://jsonplaceholder.typicode.com/comments?_limit=5');
      const comments = await res.json();
      ctx.commit('setComments', comments);
      ctx.commit('setCommentsLoading', false);
    },
  },
  modules: {},
});
