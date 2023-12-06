import { createRouter, createWebHashHistory } from 'vue-router'
import { useAuthStore } from '@/stores/authstore.js'

import AdminPage from '@/pages/AdminPage.vue'
import ManagerPage from '@/pages/ManagerPage.vue'
import HomePage from '@/pages/HomePage.vue'
import SignupPage from '@/pages/SignupPage.vue'
import LoginPage from '@/pages/LoginPage.vue'
import LogoutPage from '@/pages/LogoutPage.vue'
import ProfilePage from '@/pages/ProfilePage.vue'
import CartPage from '@/pages/CartPage.vue'
import CheckoutPage from '@/pages/CheckoutPage.vue'
import OrdersPage from '@/pages/OrdersPage.vue'
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
      title: 'Profile',
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
    path: '/orders',
    name: 'orders',
    component: OrdersPage
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
    const auth = useAuthStore()
    auth.clearAuth()
    return {
      path: '/login',
      query: { redirect: to.fullPath }
    }
  }
  console.log('Going to:', to.path)
})

export default router
