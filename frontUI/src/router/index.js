import { createRouter, createWebHistory } from 'vue-router'; // Change here
import Home from '../views/Home.vue';
import Page from '../views/page/Page.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/blog/:id',
    name: 'blog-post',
    component: Page
  },
];

const router = createRouter({
  history: createWebHistory(), // Change here
  routes,
})

export default router;
