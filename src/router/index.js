import { createRouter, createWebHashHistory } from 'vue-router'

import AdminPage from '@/pages/AdminPage.vue'
import ManagerPage from '@/pages/ManagerPage.vue'
import HomePage from '@/pages/HomePage.vue'
import SignupPage from '@/pages/SignupPage.vue'
import LoginPage from '@/pages/LoginPage.vue'
import LogoutPage from '@/pages/LogoutPage.vue'
import ProfilePage from '@/pages/ProfilePage.vue'
import CartPage from '@/pages/CartPage.vue'
import CheckoutPage from '@/pages/CheckoutPage.vue'
import OrderPage from '@/pages/OrderPage.vue'
import CategoryManagement from '@/components/CategoryManagement.vue'
import ProductManagement from '@/components/ProductManagement.vue'
import ProductPage from '@/pages/ProductPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupPage
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutPage,
    meta: {
      title: 'Logout',
      requiresAuth: true
    }
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfilePage,
    meta: {
      title: 'Logout',
      requiresAuth: true
    }
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminPage,
    meta: {
      title: 'Admin',
      requiresAuth: true
    }
  },
  {
    path: '/manager',
    name: 'manager',
    component: ManagerPage
  },
  {
    path: '/cart',
    name: 'cart',
    component: CartPage
  },
  {
    path: '/checkout',
    name: 'checkout',
    component: CheckoutPage
  },
  {
    path: '/order',
    name: 'order',
    component: OrderPage
  },
  {
    path: '/category',
    name: 'category',
    component: CategoryManagement,
    props: true
  },
  {
    path: '/product',
    name: 'product',
    component: ProductManagement,
    props: true,
    meta: {
      title: 'Product',
      requiresAuth: true
    }
  },
  {
    path: '/product/:id',
    name: 'product_id',
    component: ProductPage,
    props: true,
    meta: {
      title: 'Product',
      requiresAuth: true
    }
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

router.beforeResolve((to, from) => {
  console.log('Coming from:', from.path)
  if (to.meta.requiresAuth && !localStorage.getItem('access_token')) {
    return {
      path: '/login',
      query: { redirect: to.fullPath }
    }
  }
  console.log('Going to:', to.path)
})

export default router
