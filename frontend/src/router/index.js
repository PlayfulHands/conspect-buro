import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/order',
      name: 'order',
      component: () => import('../views/OrderView.vue')
    },
    {
      path: '/client',
      name: 'client',
      component: () => import('../views/ClientOrders.vue')
    },
    {
      path: '/offer',
      name: 'offer',
      component: () => import('../views/Offer.vue')
    },
    {
      path: '/privacy',
      name: 'privacy',
      component: () => import('../views/Privacy.vue')
    },
    {
      path: '/payment',
      name: 'payment',
      component: () => import('../views/PaymentView.vue')
    },
  ]
})

export default router