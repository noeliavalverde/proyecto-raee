
import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/pages/about/AboutPage.vue'),
  },
  {
    path: '/register',
    name: 'RegisterMachine',
    component: () => import('@/pages/register-machine/RegisterMachinePage.vue'),
  },
  {
    path: '/scrap-inform',
    name: 'ScrapInform',
    component: () => import('@/pages/scrap-inform/ScrapInformPage.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router

