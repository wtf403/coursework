<template>
  <section v-if="$store.state.isAuth" class="comments">
    <div class="comments__heading">
      <h2 class="comments__title">
        Комментарии
      </h2>
      <span class="comments__count">Всего ({{comments.length ?? 0}})</span>
    </div>
    <form class="comments__form" action="" @submit.prevent>
      <input type="hidden" name="user">
      <textarea v-model="inputText" rows="4" class="comments__input" placeholder="Ваш комментарий" />
      <div class="comments__btns">
        <my-button-outline type="reset">
          Отмена
        </my-button-outline>
        <my-button @click="addComment">
          Отправить
        </my-button>
      </div>
    </form>
    <section class="comments__section" v-if="$store.state.isAuth">
      <div v-for="comment in comments" v-bind:key="comment.userId" class="comments__block">
        <h3 class="comment__username">User #{{comment.userId}}</h3>
        <pre class="comment__text">{{comment.text}}</pre>
      </div>
    </section>
  </section>
</template>
<script>

export default {
  data() {
    return {
      inputText: '',
      comments: [ {
        userId: 921,
        text: 'Example comment',
      }, 
      ],
    };
  },
  methods: {
    addComment() {
      this.comments.push({
        userId: this.$store.state.userId,
        text: this.inputText,
      });
    },
  },
};
</script>
<style lang="scss" scoped>
.comments {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 6rem;
}

.comments__heading {
  display: flex;
  justify-content: space-between;
}

.comments__count {
  display: inline-flex;
  gap: 1ch;
  font-size: 1.2em;
}

.comments__input {
  padding: 1em;
  color: white;
  background-color: transparent;
  border: 2px solid white;
  border-radius: 6px;
  resize: none;

  &::placeholder {
    color: lightslategrey;
  }
}

.comments__form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.comments__btns {
  display: flex;
  gap: 1rem;
  margin-left: auto;
}


.comments__section {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 2rem;
}

.comments__block {
  padding: 1rem 2rem;
  background-color: rgba(0, 0, 0, 0.4);
  border-radius: 12px;
}

.comment__text {
  white-space: pre-wrap;
  word-wrap: break-word;
  margin-block: 0;
}
</style>
