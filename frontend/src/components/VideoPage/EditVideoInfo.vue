<!-- eslint-disable vue/max-attributes-per-line -->
<template>
  <h2 class="heading">
    Редактировать описание
  </h2>
  <form action="" class="form" @submit.prevent>
    <label class="form__multiline">
      <span>Описание</span>
      <textarea autofocus rows="5" :value="data.description" name="description" />
    </label>
    <label class="form__field">
      <span>Продолжительность:</span>
      <input class="text" :value="data.duration" type="time" step="1">
    </label>
    <label class="form__field">    
      <span>Страна:</span>
      <input class="text" list="countries"  :value="data.country" type="text">
      <datalist id="countries">
        <option value="Китай" />
        <option value="Россия" />
        <option value="США" />
        <option value="Индия" />
      </datalist>
    </label>
    <label class="form__field">    
      <span>Дата выхода:</span>
      <input class="text" :value="data.release" type="date">
    </label>
    <label class="form__field">
      <span>Бюджет:</span>
      <input class="text" inputmode="numeric" :value="data.budget" type="text">
    </label>
    <label class="form__field">
      <span>Сборы:</span>
      <input class="text" inputmode="numeric" :value="data.fees" type="text">
    </label>
    <label class="form__field">
      <span>Возрастное ограничение:</span>
      <input class="text" :value="data.age_restriction" type="text">
    </label>
    <div class="form__multiline">
      <span>Режисёры:</span>
      <VueMultiselect v-model="selectedDirectors" :options="directors" :multiple="true"
                      :close-on-select="true" placeholder="Pick some" label="name" track-by="name" />
    </div>
    <div class="form__multiline">
      <span>Актеры:</span>
      <VueMultiselect v-model="selectedActors" :options="actors" :multiple="true"
                      :close-on-select="true" placeholder="Pick some" label="name" track-by="name" />
    </div>
    <div class="form__multiline">
      <span>Жанры:</span>
      <VueMultiselect v-model="selectedGenres" :options="genres" :multiple="true" :close-on-select="true"
                      placeholder="Pick some" label="title" track-by="title" />
    </div>

    <my-button-outline @click="closeModel" class="form__btn">
      Отмена
    </my-button-outline>
    <my-button class="form__btn">
      Отправить
    </my-button>
  </form>
</template>
<script>
import VueMultiselect from 'vue-multiselect';
export default {
  components: { VueMultiselect },
  props: {
    data: Object,
  },
  data() {
    return {
      actors: this.data.actors,
      selectedActors: null,
      directors: this.data.directors,
      selectedDirectors: null,
      genres: this.data.genres,
      selectedGenres: null,
    };
  },
  methods: {
    closeModel() {
      this.$emit('close');
    },
  },
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>
<style lang="scss" scoped>
.heading {
  margin-top: 5px;
}

.form {
  display: flex;
}

.form__multiline {
  display: flex;
  flex-direction: column;
  max-width: 100%;
  margin-bottom: 20px;

  & > textarea {
    resize: vertical;
  }
}

.form__field {
  display: inline-flex;
  justify-content: space-between;
  font-size: clamp(1rem, 0.4vw + 0.9rem, 1.25rem);
}

.form__btn {
  color: white;
  font-weight: 700;
}
</style>
