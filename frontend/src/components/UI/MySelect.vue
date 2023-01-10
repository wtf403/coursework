<!-- eslint-disable vue/no-mutating-props -->
<!-- eslint-disable vue/no-deprecated-slot-attribute -->
<template>
  <selectmenu v-if="HTMLSelectMenuElementSupported()" v-model="modelValue" class="selectmenu" @change="changeOption">
    <my-button-outline slot="button" class="select__button" behavior="button">
      <span behavior="selected-value">
        Фильтрация
      </span>
      <img v-svg-inline height="20" src="@/assets/sort-icon.svg" alt="Сортировка">
    </my-button-outline>
    <ul slot="listbox" popup class="select__popup" behavior="listbox">
      <option
        v-for="option in options"
        :key="option.value"
        class="select__option"
        :value="option.value"
      >
        {{option.name}}
      </option>
    </ul>
  </selectmenu>
  <div class="select" v-else>
    <select @change="changeOption" class="select__button">
      <option
        v-for="option in options"
        :key="option.value"
        class="select__option"
        :value="option.value"
      >
        {{option.name}}
      </option>
    </select>
  </div>
</template>
<script>
export default {
  name: 'MySelect',
  props: {
    modelValue: {
      type: String,
    },
    options: {
      type: Array,
      default: () => [],
    },
  },
  watch: {
    // eslint-disable-next-line vue/no-arrow-functions-in-watch
    modelValue: () => {},
  },
  methods: {
    changeOption(event) {
      this.$emit('update:modelValue', event.currentTarget.value);
    },
    HTMLSelectMenuElementSupported() {
      return 'HTMLSelectMenuElement' in window;
    },
  },
};
</script>
<style lang="scss">
.select {
  display: flex;
  background-color: rgba(0 0 0 / 0.2);
  border: 2px #7b6ef6 solid;
  border-radius: 12px;
}

.select__popup {
  position: absolute;
  padding: 0;
  background-color: rgba(0 0 0 / 0.8);
  border-radius: 12px;
}

.select__button {
  position: relative;
  display: inline-flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  min-width: 220px;
  padding: 12px 20px;
  color: white;
  text-align: center;
  background-color: transparent;
  border: 0;
  border-right: 20px solid transparent;
  border-radius: 12px;
}

.select__option {
  padding: 0.5rem 1rem;
  color: white;
  outline: none;

  &:checked {
    background-color: #7b6ef6;

    &:hover {
      background-color: #7b6ef6;
    }
  }

  &:hover {
    background-color: #20283e;
  }

  &:first-child {
    border-radius: 12px 12px 0 0;
  }

  &:last-child {
    border-radius: 0 0 12px 12px;
  }
}
</style>
