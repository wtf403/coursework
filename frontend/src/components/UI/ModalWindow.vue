<template>
  <dialog class="modal" ref="modal" @click="closeModalWindow">
    <div @click.stop @keyup.stop class="modal__content">
      <button @click="closeModalWindow" class="modal__close">
        <img height="30" src="@/assets/close-icon.svg" alt="Close modal window">
      </button>
      <slot  /> 
    </div>
  </dialog>
</template>
<script>

export default {
  props: {
    showModalWindow: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    closeModalWindow() {
      this.$emit('update:showModalWindow', false);
    },
  },
  created: function() {
    document.addEventListener('keyup', (event) => {
      if (event.key === 'Escape') {
        this.closeModalWindow();
      }
    });
  },
  watch: {
    showModalWindow(newValue) {
      if (newValue) {
        this.$refs.modal.showModal();
      } else {
        this.$refs.modal.close(); 
      }
    },
  },
};
</script>
<style lang="scss" scoped>
.modal {
  position: relative;
  padding: 0;
  background-color: #c7c1ff;
  border-radius: 12px;

  &::backdrop {
    background-color: rgba(0, 0, 0, 0.8);
  }
}

.modal__close {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background-color: transparent;
  border: 0;
}

.modal__content {
  min-width: min(95vw, 600px);
  padding: 1rem 2rem;
}
</style>
