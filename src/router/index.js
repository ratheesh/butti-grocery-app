import { createRouter, createWebHashHistory } from 'vue-router'
import { useAuthStore } from '@/stores/authstore.js'

import AdminPage from '@/pages/AdminPage.vue'
import ManagerPage from '@/pages/ManagerPage.vue'
import HomePage from '@/pages/HomePage.vue'
import SignupPage from '@/pages/SignupPage.vue'
import LoginPage from '@/pages/LoginPage.vue'
import ProfilePage from '@/pages/ProfilePage.vue'
import CartPage from '@/pages/CartPage.vue'
import CheckoutPage from '@/pages/CheckoutPage.vue'
import OrdersPage from '@/pages/OrdersPage.vue'
import OrderPage from '@/pages/OrderPage.vue'
import SearchPage from '@/pages/SearchPage.vue'
import UnauthorizedPage from '@/pages/UnauthorizedPage.vue'

import AdminDashboard from '@/components/admin/DashBoard.vue'
import AdminUserManagement from '@/components/admin/UserManagement.vue'
import AdminCategoryManagement from '@/components/manager/CategoryManagement.vue'

import ManagerDashboard from '@/components/manager/DashBoard.vue'
import ManagerCategoryManagement from '@/components/manager/CategoryManagement.vue'
import ManagerProductManagement from '@/components/manager/ProductManagement.vue'

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
    redirect: { name: 'admindashboard' },
    children: [
      {
        path: 'dashboard',
        name: 'admindashboard',
        component: AdminDashboard
      },
      {
        path: 'users',
        name: 'adminusers',
        component: AdminUserManagement
      },
      {
        path: 'category',
        name: 'admincategories',
        component: AdminCategoryManagement
      }
    ],
    meta: {
      title: 'Admin',
      requiresAuth: true,
      role: 'admin'
    }
  },
  {
    path: '/manager',
    name: 'manager',
    component: ManagerPage,
    redirect: { name: 'managerdashboard' },
    children: [
      {
        path: 'dashboard',
        name: 'managerdashboard',
        component: ManagerDashboard
      },
      {
        path: 'category',
        name: 'managercategories',
        component: ManagerCategoryManagement
      },
      {
        path: 'products',
        name: 'managerproducts',
        component: ManagerProductManagement
      }
    ],
    meta: {
      title: 'Manager',
      requiresAuth: true,
      role: 'manager'
    }
  },
  {
    path: '/cart',
    name: 'cart',
    component: CartPage,
    meta: {
      title: 'Cart',
      requiresAuth: true
    }
  },
  {
    path: '/checkout',
    name: 'checkout',
    component: CheckoutPage,
    meta: {
      title: 'Checkout',
      requiresAuth: true
    }
  },
  {
    path: '/orders',
    name: 'orders',
    component: OrdersPage,
    meta: {
      title: 'Orders',
      requiresAuth: true
      // role: 'user'
    }
  },
  {
    path: '/order/:id',
    name: 'order',
    component: OrderPage,
    props: true,
    meta: {
      title: 'Order Info',
      requiresAuth: true
    }
  },
  {
    path: '/search/:query',
    name: 'search',
    component: SearchPage,
    props: true
  },
  {
    path: '/forbidden',
    name: 'forbidden',
    component: UnauthorizedPage,
    meta: {
      title: 'Unauthorized'
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

router.beforeResolve((to, from, next) => {
  // console.log('Coming from:', from.path)
  // console.log('Going to:', to.path)
  const auth = useAuthStore()
  if (to.meta.requiresAuth) {
    if (auth.authenticated) {
      // console.log('authenticated', to.meta.role, auth.user.role, to.path)
      if (to.meta.role && auth.user.role && auth.user.role !== to.meta.role) {
        console.log('not authorized')
        router.push('/forbidden')
      } else {
        next()
      }
    } else {
      // console.log('to login page')
      auth.returnURL = to.fullPath
      next({ path: '/login', query: { redirect: to.fullPath } })
    }
  } else {
    next()
    // console.log('Going to:', to.path)
  }
})

export default router
