import { createRouter, createWebHashHistory } from 'vue-router'

  const routes = [
    {
      path: '/',
      name: 'home',
      component: () => import('@/pages/HomePage.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('@/pages/SignupPage.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/pages/LoginPage.vue')
    },
    {
      path: '/logout',
      name: 'logout',
      component: () => import('@/pages/LogoutPage.vue')
    },
    {
      path: '/cart',
      name: 'cart',
      component: () => import('@/pages/CartPage.vue')
    },
    {
      path: '/product/:id',
      name: 'product',
      component: () => import('@/pages/ProductPage.vue'),
      props: true,
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'error',
      component: () => import('@/pages/ErrorPage.vue'),
    },
  ]

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
