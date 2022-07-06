import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/sign-up',
    component: () => import('@/pages/RegisterPage.vue'),
  },
  {
    path: '/sign-in',
    component: () => import('@/pages/LoginPage.vue'),
  },
  {
    path: '/about',
    component: () => import('@/pages/AboutPage.vue'),
  },
  {
    path: '/',
    component: () => import('@/pages/MainPage.vue'),
  },
  {
    path: '/videos/:id',
    component: () => import('@/pages/VideosIdPage.vue'),
  },
  {
    path: '/actors/:id',
    component: () => import('@/pages/NotFoundPage.vue'),
  },
  {
    path: '/directors/:id',
    component: () => import('@/pages/NotFoundPage.vue'),
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: () => import('@/pages/NotFoundPage.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
