<!-- eslint-disable vue/no-mutating-props -->
<!-- eslint-disable vue/require-v-for-key -->
<template>
  <div>
    <form v-if="navigation === 'arrow'" class="switch">
      <div v-for="option in options" class="switch__outer">
        <input
          :id="option.name"
          v-model="modelValue"
          class="switch__input visually-hidden"
          type="radio"
          name="switch"
          :value="option.name"
          @change="changeOption"
        >
        <label :for="option.name" class="switch__inner">
          {{option.title}}
        </label>
      </div>
    </form>
    <nav v-if="navigation === 'tab'" class="switch">
      <div v-for="option in options" class="switch__outer">
        <button class="switch__inner switch__button"
                @click="changeOption"
                :value="option.name">
          {{option.title}}
        </button>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'MySwitch',
  props: {
    modelValue: {
      type: String,
    },
    options: {
      type: Array,
      default: () => [],
    },
    navigation: {
      type: String,
      default: 'tab',
    },
  },
  watch: {
    // eslint-disable-next-line vue/no-arrow-functions-in-watch
    modelValue: () => {},
  },
  updated() {
    document.querySelectorAll('.switch__button').forEach((button) => {
      if (button.value === this.modelValue) {
        button.classList.add('switch__inner--active');
      } else {
        button.classList.remove('switch__inner--active');
      }
    });
  },
  methods: {
    changeOption(event) {
      this.$emit('update:modelValue', event.target.value);
    },
  },
};
</script>
<style lang="scss">
.siwtch {
  display: flex;
  flex-direction: column;
}

.switch__inner {
  flex-shrink: 1;
  padding: clamp(0.438rem, 0.5vw + 0.4rem, 0.938rem) clamp(0.938rem, 0.5vw + 0.8rem, 1.875rem);
  color: white;
  background-color: rgba(0 0 0 / 0.2);
  border: 0;
  border-radius: 8px;
  cursor: pointer;
  user-select: none;

  &:hover {
    background-color: #20283e;
  }
}

.switch__input:checked + .switch__inner, .switch__inner--active {
  color: white;
  background-color: #7b6ef6;
}

.switch__inner--active:hover {
  background-color: #7b6ef6;
}

.switch__outer {
  display: inline-flex;
  padding: 5px 0;
  padding-left: 5px;
  background-color: rgba(0 0 0 / 0.2);

  &:first-child {
    border-radius: 12px 0 0 12px;
  }

  &:last-child {
    padding-right: 5px;
    border-radius: 0 12px 12px 0;
  }

  &:has(> input:focus-visible) > .switch__inner {
    outline: 2px solid red;
  }
}
</style>
