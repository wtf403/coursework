<template>
  <label ref="label" class="label" @focus="activateInput">
    <input
      ref="input"
      class="label__input"
      :value="modelValue"
      :type="input.inputType"
      :placeholder="input.placeholderText"
      @input="updateInput"
    >
    <img v-svg-inline class="label__image" :src="input.iconPath" alt="Icon">
    <button
      v-if="input.inputType === 'password'"
      class="label__hide-button"
      @click="togglePasswordVisibility"
    >
      <img
        ref="eyeImage"
        v-svg-inline
        :src="require('@/assets/eye-icon.svg')"
        alt="Toggle password visibility"
      >
    </button>
    <span class="visually-hidden">
      {{input.inputType}} field
    </span>
  </label>
</template>

<script>
export default {
  name: 'MyInput',
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
      if (this.$props.input.inputType === 'password') {
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
  position: relative;
  display: flex;
  align-items: center;
  min-height: 50px;
  padding: 15px 20px;
  border: 1px solid #8f99b6;
  border-radius: 12px;
  isolation: isolate;

  &:has(> button:focus) > input {
    border: 1px solid #ffffff;
    border-radius: 12px;
    outline: 0;

    & + svg {
      stroke: #ffffff;
    }

    & ~ button > svg {
      stroke: #ffffff;
    }
  }
}

.label__input {
  position: absolute;
  inset: 5px;
  inset: 0;
  width: 100%;
  height: 100%;
  color: inherit;
  background: transparent;
  background-color: var(--darken-blur);
  border: 0;
  border: 1px solid transparent;
  border-radius: 12px;
  padding-inline: 55px;

  &:focus {
    border: 1px solid #ffffff;
    border-radius: 12px;
    outline: 0;

    &::placeholder {
      color: white;
    }
  }

  &:focus + svg {
    stroke: #ffffff;
  }

  &:focus ~ button > svg {
    stroke: #ffffff;
  }

  &::placeholder {
    color: #8f99b6;
    letter-spacing: 0.5px;
  }
}

.label__image {
  position: absolute;
  left: 15px;
  z-index: 1;
  width: max-content;

  &:focus {
    outline: none;
    box-shadow: none;
  }
}

.label__hide-button {
  position: absolute;
  right: 15px;
  z-index: 1;
  max-height: 24px;
  padding: 0;
  background: transparent;
  border: 0;

  &:focus {
    outline-offset: 2px;
  }
}
</style>
