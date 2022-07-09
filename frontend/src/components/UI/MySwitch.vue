<template>
  <form class="switch">
    <div class="switch__outer" v-for="option in options">
      <input
        v-model="modelValue"
        @change="changeOption"
        class="switch__input visually-hidden"
        type="radio"
        name="switch"
        @check="focusOption"
        @blur="blurOption"
        :value="option.name"
        :id="option.name"
      />
      <label :for="option.name" class="switch__inner">
        {{ option.title }}
      </label>
    </div>
  </form>
</template>
<script>
export default {
  name: 'my-switch',
  props: {
    modelValue: {
      type: String,
    },
    options: {
      type: Array,
      default: () => [],
    },
  },
  methods: {
    changeOption(event) {
      this.$emit('update:modelValue', event.currentTarget.value);
    },
  },
  mounted: () => {
  },
  watch: {
    modelValue: () => {},
  },
};
</script>
<style lang="scss">
.siwtch {
  display: flex;
  flex-direction: column;
}
.switch__outer {
  display: inline-flex;
  background-color: rgba(0 0 0 / 0.2);
  padding:  5px 0;
  padding-left: 5px;
  &:first-child {
    border-radius: 12px 0 0 12px;
  }
  &:last-child {
    border-radius: 0 12px 12px 0;
    padding-right: 5px;
  }
}
.switch__inner {
  flex-shrink: 1;
  user-select: none;
  padding: 15px 30px;
  border-radius: 8px;
  &:hover {
    background-color: #20283e;
  }
}
.switch__input:checked + .switch__inner {
  background-color: #7B6EF6;
  color: white;
}
</style>
