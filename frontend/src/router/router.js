import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '@/pages/LoginPage';
import RegisterPage from '@/pages/RegisterPage';
import MainPage from '@/pages/MainPage';
import store from '@/store';

const routes = [
  {
    path: '/sign-up',
    name: 'sign-up',
    component: RegisterPage,
    beforeEnter: () => {
      store.state.isAuth ? router.push('/') : '';
    },
  },
  {
    path: '/sign-in',
    name: 'sign-in',
    component: LoginPage,
    beforeEnter: () => {
      store.state.isAuth ? router.push('/') : '';
    },
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('@/pages/NotFoundPage.vue'),
  },
  {
    path: '/',
    name: 'main',
    component: MainPage,
  },
  {
    path: '/videos/:id',
    name: 'video',
    component: () => import('@/pages/VideosIdPage.vue'),
  },
  {
    path: '/actors/:id',
    name: 'actor',
    component: () => import('@/pages/NotFoundPage.vue'),
  },
  {
    path: '/directors/:id',
    name: 'director',
    component: () => import('@/pages/NotFoundPage.vue'),
  },
  {
    path: '/:pathMatch(.*)*',
    beforeEnter: (to, from, next) => {
      next('/404');
    },
  },
  {
    path: '/404',
    name: '404',
    component: () => import('@/pages/NotFoundPage.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
