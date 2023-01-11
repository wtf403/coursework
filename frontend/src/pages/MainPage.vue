<!-- eslint-disable vue/no-use-v-if-with-v-for -->
<template>
  <main class="main">
    <h1 class="main__heading">
      Главная
    </h1>
    <my-input
      v-model="searchQuery"
      v-focus
      :input="$store.state.inputs.searchInput"
      class="main__search"
    />
    <div class="main__sorting">
      <my-switch v-model="currentCategory" class="main__category" :navigation="'arrow'" :options="categories" />
      <my-select v-model="sortValue" class="main__select" :options="sortOptions" />
    </div>
    <div class="main__helpers">
      <span class="main__count">
        <p class="main__text">
          Всего
        </p>
        <p v-if="isVideosLoading || errorMassage" class="main__number">
          (0)
        </p>
        <p v-else class="main__number">
          ({{totalCount}})
        </p>
      </span>
      <my-button-outline @click="fetchVideos" class="main__refresh">
        <img v-svg-inline src="@/assets/refresh-icon.svg" alt="Refresh video list"> 
      </my-button-outline>
    </div>
    <section class="main__video-list">
      <video-sceleton v-if="isVideosLoading" class="main__video-item" v-bind:key="id" v-for="id in 24"  />
      <video-item
        v-for="video in sortedAndSearchedVideos"
        v-else
        :key="video.id"
        class="main__video-item"
        :video="video"
      />
    </section>
    <my-switch
      v-model="currentPage"
      class="main__pages"
      :navigation="'tab'"
      :options="pages"
      @click="
        fetchVideos();
        focusFirst();
      "
    />
    <div v-if="errorMassage && !isVideosLoading" class="main__load-error">
      <h2 class="main__error-title">
        Ошибка загрузки видео
      </h2>
      <p class="main__error-massage">
        {{errorMassage}}
      </p>
      <my-button-outline class="main__error-button" @click="refatchVideos">
        Повторить попытку
      </my-button-outline>
    </div>
    <div v-if="notFound" class="main__sort-not-found">
      <h2 class="main__error-title">
        По вашему запросу ничего не найдено!
      </h2>
    </div>
  </main>
</template>

<script>
import axios from 'axios';
import VideoItem from '@/components/VideoItem.vue';
import VideoSceleton from '@/components/VideoSceleton.vue';
import MyButtonOutline from '@/components/UI/MyButtonOutline.vue';
export default {
  components: {
    VideoItem,
    VideoSceleton,
    MyButtonOutline,
  },
  data() {
    return {
      isVideosLoading: false,
      videos: [],
      currentCategory: 'all',
      categories: [
        { name: 'all', title: 'Всё' },
        { name: 'film', title: 'Фильмы' },
        { name: 'series', title: 'Сериалы' },
      ],
      currentPage: '1',
      pages: [],
      sortOptions: [
        { value: 'id', name: 'По умолчанию' },
        { value: 'title', name: 'По названию' },
        { value: 'release', name: 'По дате выхода' },
      ],
      sortValue: '',
      notFound: false,
      errorMassage: '',
      searchQuery: '',
    };
  },
  computed: {
    sortedVideos() {
      let results = [...this.videos].sort((v1, v2) =>
        String(v1[this.sortValue])?.localeCompare(String(v2[this.sortValue]))
      );
      return results;
    },

    sortedAndSearchedVideos() {
      let videos = this.sortedVideos.filter((v) =>
        v.title.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
      // eslint-disable-next-line vue/no-side-effects-in-computed-properties
      this.notFound = !videos.length && !this.isVideosLoading;
      return videos.filter((v) => {
        if (this.currentCategory === 'film') {
          return v.type.video_type === 'Кино';
        }
        if (this.currentCategory === 'series') {
          return v.type.video_type === 'Сериал';
        }
        return true;
      });
    },
  },
  mounted() {
    this.isVideosLoading = true;
    setTimeout(() => this.fetchVideos(), 1500);
  },
  methods: {
    refatchVideos() {
      this.isVideosLoading = true;
      window.setTimeout(() => {
        this.fetchVideos();
      }, 1500);
    },
    async fetchVideos() {
      try {
        const response = await axios.get(
          'http://coursework.std-1724.ist.mospolytech.ru/api/videos',

          {
            params: {
              page: this.currentPage,
            },
          }
        );
        this.videos = this.shuffleArray(response.data.results);
        this.totalCount = response.data.count;
        const totalPages = Math.ceil(this.totalCount / 24);
        let pages = [];
        for (let p = 1; p <= totalPages; p++) {
          pages.push({ name: `${p}`, title: `${p}` });
        }
        this.pages = pages;
      } catch (e) {
        this.errorMassage = e.message;
      } finally {
        this.isVideosLoading = false;
      }
    },
    focusFirst() {
      let el = document.querySelector('.video');
      el.focus();
    },
    shuffleArray(array) {
      let currentIndex = array.length,
        randomIndex;
      while (currentIndex !== 0) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;
        [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
      }
      return array;
    },
  },
};
</script>

<style type="scss">
.main {
  position: relative;
  display: grid;
  grid-template-rows: min-content min-content min-content 1fr min-content;
  grid-template-columns: 1fr 1.2fr;
  align-items: stretch;
  gap: 1em;
  height: fit-content;
  min-height: 80vh;
}

.main__heading {
  grid-row: 1 / 2;
  color: white;
}

.main__search {
  grid-row: 1 / 2;
}

/* filters */

.main__sorting {
  display: flex;
  grid-column: span 2;
  flex-wrap: wrap;
  justify-content: space-between;
  row-gap: 0.5rem;
  column-gap: 2rem;
}

.main__category {
  display: flex;
  grid-row: 2 / 3;
  padding-right: 1rem;
}

.main__select {
  justify-self: end;
}

.main__helpers {
  display: flex;
  grid-column: span 2;
  justify-content: space-between;
}

svg { outline: none; }

.main__count {
  display: inline-flex;
  grid-row: 3 / 4;
  flex-direction: row;
  align-items: center;
  gap: 0.5em;
  color: white;
}

.main__text {
  font-size: 1.5em;
}

.main__number {
  font-size: 1em;
}

@media (max-width: 600px) {
  .main__sorting {
    justify-content: center;
  }

  .main__category {
    padding-right: 0;
  }
}

@media (max-width: 768px) {
  .main {
    grid-template-rows: repeat(5, min-content), 1fr, min-content;
  }

  .main__search {
    grid-row: 2 / 3;
    grid-column: span 2;
  }

  .main__select {
    grid-row: 4 / 5;
    justify-self: start;
  }

  .main__category {
    grid-row: 3 / 4;
  }

  .main__count {
    grid-row: 1 / 2;
  }

  .main__video-list {
    justify-items: stretch;
  }
}

.main__video-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(clamp(6.25rem, 30vw, 16.75rem), 1fr));
  grid-column: span 2;
  justify-items: center;
  gap: 1rem;
  width: 100%;
  height: min-content;
}

.main__video-item {
  width: 100%;
}

.main__spinner {
  position: absolute;
  bottom: -200%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.main__load-error {
  position: absolute;
  bottom: -200%;
  left: 50%;
  display: flex;
  flex-direction: column;
  justify-items: center;
  text-align: center;
  transform: translate(-50%, -50%);
}

.main__error-title {
  color: red;
}

.main__sort-not-found {
  position: absolute;
  bottom: 0%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.main__pages {
  margin-top: auto;
  padding-top: 2rem;
}

.main__error-button {
  margin-top: 0.5em;
}
</style>
