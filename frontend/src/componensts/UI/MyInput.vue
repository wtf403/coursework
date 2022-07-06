<template>
  <label class="label">
    <span class="visually-hidden">{{ input.inputType }} field</span>
    <img class="label__image" :src="input.iconPath" alt="Icon" />
    <input
      class="label__input"
      ref="input"
      :value="modelValue"
      @input="updateInput"
      :type="input.inputType"
      :placeholder="input.placeholderText"
    />
    <img
      class="label__hide"
      ref="eyeImage"
      v-if="input.inputType == 'password'"
      :src="require('@/assets/eye-icon.svg')"
      alt="Toggle password visibility"
      @click="togglePasswordVisibility"
    />
  </label>
</template>

<script>
export default {
  name: 'my-input',
  props: {
    modelValue: [String, Number],
    input: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      passwordInputVisible: false,
    };
  },
  methods: {
    updateInput(event) {
      this.$emit('update:modelValue', event.target.value);
      if (this.$props.input.inputType == 'password') {
        this.$refs.input.type = 'password';
        this.$refs.eyeImage.src = require('@/assets/eye-icon.svg');
      }
    },
    togglePasswordVisibility() {
      this.passwordInputVisible = !this.passwordInputVisible;
      if (this.passwordInputVisible) {
        this.$refs.input.type = 'text';
        this.$refs.eyeImage.src = require('@/assets/eye-slash-icon.svg');
      } else {
        this.$refs.input.type = 'password';
        this.$refs.eyeImage.src = require('@/assets/eye-icon.svg');
      }
    },
  },
};
</script>

<style lang="scss" scoped>
@use 'sass:color';
.label {
  display: grid;
  grid-template-columns: max-content 1fr max-content;
  align-items: center;
  border: 1px solid #323b54;
  border-radius: 12px;
  padding: 15px 20px;
  min-height: 50px;
  position: relative;
  isolation: isolate;
}
.label__input {
  background: transparent;
  position: absolute;
  width: 100%;
  inset: 5px;
  border-radius: 12px;
  border: 0;
  padding-inline: 55px;
  inset: 0;
  color: inherit;
  border: 1px solid transparent;
  &:focus {
    outline: 0;
    border: 1px solid #8f99b6;
    border-radius: 12px;
  }
  &::placeholder {
    color: color.change(#8f99b6, $alpha: 0.5);
    letter-spacing: 0.5px;
  }
}
.label__image {
  z-index: 1;
  position: absolute;
  left: 15px;
}
.label__hide {
  z-index: 1;
  position: absolute;
  right: 15px;
}
</style>
