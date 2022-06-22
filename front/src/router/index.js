
import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },

  {
    path: '/scrap-inform',
    name: 'ScrapInform',
    component: () => import('@/pages/scrap-inform/ScrapInformPage.vue'),
  },
  {
    path: '/process/:id',
    name: 'EventDetail',
    component: () => import('@/pages/details/EventDetailPage.vue'),
    props:true
  },
  {
    path: '/manager-inform',
    name: 'ManagerPage',
    component: () => import('@/pages/manager/ManagerPage.vue'),
    props:true
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router

