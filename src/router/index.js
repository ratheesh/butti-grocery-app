import { createRouter, createWebHashHistory } from 'vue-router'

import AdminPage from '@/pages/AdminPage.vue'
import ManagerPage from '@/pages/ManagerPage.vue'
import HomePage from '@/pages/HomePage.vue'
import SignupPage from '@/pages/SignupPage.vue'
import LoginPage from '@/pages/LoginPage.vue'
import LogoutPage from '@/pages/LogoutPage.vue'
import ProfilePage from '@/pages/ProfilePage.vue'
import CartPage from '@/pages/CartPage.vue'
import CategoryManagement from '@/components/CategoryManagement.vue'
import ProductPage from '@/pages/ProductPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage,
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupPage,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage,
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutPage,
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfilePage,
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminPage,
  },
  {
    path: '/manager',
    name: 'manager',
    component: ManagerPage,
  },
  {
    path: '/cart',
    name: 'cart',
    component: CartPage,
  },
  {
    path: '/category',
    name: 'category',
    component: CategoryManagement,
    props: true
  },
  {
    path: '/product/:id',
    name: 'product',
    component: ProductPage,
    props: true
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'error',
    component: () => import('@/pages/ErrorPage.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes
})

export default router
