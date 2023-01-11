<!-- eslint-disable vue/max-attributes-per-line -->
<template>
  <div>
    <h2 class="heading">
      Редактировать описание
    </h2>
    <form class="form" @submit.prevent>
      <div v-for="(i, key) in info" v-bind:key="key" class="form__line">
        <span class="form__status" />
        <label v-if="i.input == 'textarea'" class="form__multiline">
          <span>{{i.key}}</span>
          <textarea autofocus rows="5" :value="i.value" @input="updateValue" :name="key" />
        </label>
        <label v-if="i.input == 'input'" class="form__field">
          <span>{{i.key}}</span>
          <input :value="i.value"
                 @input="updateValue"
                 :inputmode="i.inputmode"
                 :step="i.step"
                 :min="i.min" :max="i.max" :name="key" :type="i.type">
        </label>
        <label v-if="i.input == 'multiselect'" class="form__multiline">
          <span>{{i.key}}</span>
          <VueMultiselect v-model="i.value"
                          :options="i.options"
                          :multiple="true"
                          :close-on-select="true"
                          placeholder="Pick some"
                          @update="updateValue"
                          :label="i.track"
                          :track-by="i.track"
                          :limit="3"
                          :name="key" />
        </label>
      </div>
      <my-button-outline @click="$emit('close')" class="form__btn">
        Отмена
      </my-button-outline>
      <my-button @click="sendData" class="form__btn">
        Отправить
      </my-button>
    </form>
  </div>
</template>
<script>
import VueMultiselect from 'vue-multiselect';
import axios from 'axios';
export default {
  components: { VueMultiselect },
  props: {
    data: Object,
    info: Object,
  },
  methods: {
    closeModal() {
      this.$emit('close'); 
    },
    updateValue(e) {
      let updatedInfo = this.info;
      updatedInfo[e.target.name].value = e.target.value;
      this.$emit('update:info', updatedInfo);
    },
    sendData() {
      const formStatus = document.querySelector('.form__status');
      axios.post('//httpbin.org/post', this.info)
        .then((response) => {
          console.log(response);
          formStatus.innerHTML = 'Данные отправлены';
          formStatus.style.color = 'limegreen';
          setTimeout(() => { this.closeModal(); }, 1000);
        })
        .catch((error) => {
          formStatus.innerHTML = 'Ошибка при отправке данных';
          formStatus.style.color = 'red';
          console.log(error);
        })
        .finally(() => {
          setTimeout(() => { document.querySelector('.form__status').innerHTML = ''; }, 1000);
        });
    },
  },
  emits: ['update:info', 'close'],
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>
<style lang="scss" scoped>
.heading {
  margin-top: 5px;
}

.form {
  display: flex;
  gap: 1rem;
  padding-top: 2rem;
}

.form__status {
  padding-bottom: 10px;
  color: orange;
  font-size: 2rem;
  text-align: center;
}

.form__line {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
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
