/* stylelint-disable block-no-empty */
<template>
  <div class="video-page">
    <main class="video-page">
      <section class="video-page__video video">
        <iframe
          class="video__iframe"
          :src="`${data.video_url}`"
          title="YouTube video player"
          frameborder="0"
          allow="autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        />
      </section>
      <section class="video-page__information information">
        <h1 class="information__heading">
          {{data.title}}
        </h1>
        <div class="information__image-wrapper">
          <img
            class="information__image"
            :src="data.image_url"
            :srcset="data.image_url_x2"
            :alt="Обложка - `${data.title}`"
          >
          <my-button-outline
            @click="toggleFavouriteVideo"
            v-if="$store.state.isAuth"
            class="information__favourites"
          >
            <span>
              Избранное
            </span>
            <img 
              class="information__icon information__icon--unactive"
              v-svg-inline
              height="30"
              src="@/assets/star-icon.svg"
              alt="Иконка избранного">
          </my-button-outline>
          <my-button-outline 
            @click="ModalWindowVisible = true"
            v-if="$store.state.isAuth"
            class="information__favourites">
            <span>
              Редактировать
            </span>
            <img class="information__icon"
                 v-svg-inline
                 height="35"
                 src="@/assets/edit-icon.svg"
                 alt="Иконка редактирования">
          </my-button-outline>
        </div>
        <div class="information__properties">
          <div class="information__row" v-for="row in info" v-bind:key="row">
            <p v-if="row.key != null" class="information__key">
              {{row.key}}
            </p>
            <ul v-if="typeof row.value == 'object' " class="information__value">
              <li class="information__list" v-bind:key="i.id" v-for="i of row.value">{{Object.values(i).slice(-1)[0]}}</li>
            </ul>
            <p v-else class="information__value">
              {{row.value}}
            </p>
          </div>
        </div>
      </section>
      <section>
        <video-comments />
      </section>
      <modal-window v-model:showModalWindow="ModalWindowVisible">
        <edit-video-info @close="closeModelWindow" v-model:data="data" v-model:info="info" />
      </modal-window>
    </main>
    <my-spinner v-if="isVideosLoading" class="main__spinner" />
    <div v-if="errorMassage && !isVideosLoading" class="main__load-error">
      <h2 class="main__error-title">
        Ошибка загрузки видео
      </h2>
      <p class="main__error-massage">
        {{errorMassage}}
      </p>
      <my-button-outline
        class="main__error-button"
        @click="refatchVideos"
      >
        Повторить попытку
      </my-button-outline>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import EditVideoInfo from '@/components/VideoPage/EditVideoForm.vue';
import ModalWindow from '@/components/UI/ModalWindow.vue';
import VideoComments from '@/components/VideoPage/VideoComments.vue';
export default {
  components: {
    EditVideoInfo,
    ModalWindow,
    VideoComments,
  },

  name: 'VideoComponent',
  props: {
    video: Object,
  },
  data() {
    return {
      isCommentsLoading: false,
      ModalWindowVisible: false,
      data: [],
      info: [],
    };
  },
  computed: {},
  watch: {},
  created() {
    this.isVideosLoading = true;
    this.fetchVideo();
  },
  methods: {
    closeModelWindow() {
      this.ModalWindowVisible = false;
    },
    async fetchVideo() {
      try {
        const response = await axios.get(
          `http://coursework.std-1724.ist.mospolytech.ru/api/videos/${this.$route.params.id}`
        );
        this.data = response.data;

        this.info = {
          'description': {
            key: null,
            value: this.data.description,
            input: 'textarea',
          },
          'directors': {
            key: 'Режисёры:',
            value: this.data.directors,
            options: [{id: 1, name: 'one'}, {id: 2, name: 'two'}, {id: 3, name: 'three'}, {id: 4, name: 'four'}],
            input: 'multiselect',
            track: 'name',
          },
          'actors': {
            key: 'Актеры:',
            value: this.data.actors,
            options: [{id: 1, name: 'one'}, {id: 2, name: 'two'}, {id: 3, name: 'three'}, {id: 4, name: 'four'}],
            input: 'multiselect',
            track: 'name',
          },
          'genres': {
            key: 'Жанры:',
            value: this.data.genres,
            input: 'multiselect',
            options: [{id: 1, title: 'one'}, {id: 2, title: 'two'}, {id: 3, title: 'three'}, {id: 4, title: 'four'}],
            track: 'title',
          },
          'duration': {
            key: 'Продолжительность:',
            value: this.data.duration,
            input: 'input',
            type: 'time',
            step: '1',
          },
          'country': {
            key: 'Cтрана:',
            value: this.data.country,
            input: 'input',
            type: 'text',
          },
          'release': {
            key: 'Дата выхода:',
            value: this.data.release,
            input: 'input',
            type: 'date',
            min: '1900-01-01',
            max: '2030-01-01',
          },
          'budget': {
            key: 'Бюджет:',
            value: this.data.budget,
            input: 'input',
            type: 'text',
          },
          'fees': {
            key: 'Сборы:',
            value: this.data.fees,
            input: 'input',
            type: 'text',
          },
          'age_restriction': {
            key: 'Возрастное ограничение:',
            value: this.data.age_restriction,
            input: 'input',
            type: 'number',
            inputmode: 'numeric',
            min: 0,
            max: 99,
          },
        };
      } catch (e) {
        this.errorMassage = e.message;
      } finally {
        this.isVideosLoading = false;
      }
    },
    toggleFavouriteVideo(e) {
      e.currentTarget.lastElementChild.classList.toggle('information__icon--unactive');
      if (this.$store.state.isAuth) {
        axios({
          method: 'post',
          url: `http://coursework.std-1724.ist.mospolytech.ru/api/users/${this.$store.state.userAuth}/toggle-favourite-video/`,
          data: {
            video_id: this.$route.params.id,
          },
        })
          .then((response) => {
            this.$store.commit('setFavouriteVideos', response.data);
          })
          .catch((response) => {
            this.errorMessage = response.response.data.error;
          })
          .finally(() => {
            window.localStorage.setItem('isAuth', this.$store.state.isAuth);
            window.localStorage.setItem('userId', this.$store.state.userId);
          });
      }
    },
  },
};
</script>

<style type="scss">
.video-page {
  display: flex;
  flex-direction: column;
  gap: 2em;
}

.video-page__video {
  grid-column: 1 / -1;
  background-color: black;
  border-radius: 12px;
}

.video__iframe {
  width: 100%;
  aspect-ratio: 16 / 9;
  border-radius: 12px;
}

.video-page__information {
  display: grid;
  margin-bottom: 5rem;
  font-size: clamp(0.75rem, 1vw, 1.563rem);
}

.information {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 1em;
  font-size: clamp(0.75rem, 1vw, 1.875rem);
}

.information__heading {
  grid-column: 1 / -1;
  font-size: 60px;
}

.information__image {
  border-radius: 12px;
  aspect-ratio: 2 / 3;
}

.information__image-wrapper {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

@media (width <= 768px) {
  .information {
    grid-template-columns: 1fr;
  }
}

.information__favourites {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  font-size: clamp(1.125rem, 0.5vw + 1rem, 1.5rem);
}

.information__icon {
  margin-bottom: 5px;
  outline: none;
}

.information__icon--unactive {
  color: transparent;
}

.information__properties {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 0.5em 1em;
  font-size: clamp(1rem, 1vw + 0.8rem, 2rem);
  background-color: rgba(0 0 0 / 0.2);
  border-radius: 12px;
}

.information__description {
  grid-column: 1 / -1;
  margin-bottom: 1rem;
}

.information__row {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 1em;
}

.information__row:nth-child(1) > .information__value {
  text-align: start;
}

.information__row:last-of-type > .information__value::after {
  content: '+';
}

.information__key {
  font-weight: 700;
}

.information__list {
  display: flex;
  flex-direction: column;
}

.information__value {
  margin-top: 0;
  color: white;
  text-align: end;
}

.comments__send {
  width: fit-content;
  margin-left: auto;
}

/*
.comments__number {

}

.comments__item {

}

.comments__user-image {
}

.comment__user-name {
}

.comment__text {
} */

@media print {
  .video {
    display: none;
  }

  .information__heading {
    font-size: 18pt !important;
  }

  .comments {
    display: none;
  }

  .information__favourites {
    display: none;
  }
}
</style>
