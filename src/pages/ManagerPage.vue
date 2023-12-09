<template>
  <dashboard-layout>
    <h2 class="text-center">Dash Board!</h2>
    <template v-slot:sidebar>
      <div>
        <div class="row">
          <div class="d-flex flex-column justify-content-between col-auto bg-dark min-vh-100">
            <ul class="nav nav-pills flex-column mt-2 mt-sm-0" id="menu">
              <a
                class="text-white text-decoration-none d-inline-flex justify-content-center align-items-center ms-2 my-2"
                rol="button"
              >
                <span class="fs-3 text-warning text-center">Manager</span>
              </a>
              <hr class="text-white p-0" />
              <li class="nav-item d-inline-flex align-items-center" @click="component = DashBoard">
                <a href="javascript:void(0)" class="nav-link text-white" aria-current="page">
                  <mdicon name="gauge" class="text-white" />
                  <span class="ms-2 fs-6">Dashboard</span>
                </a>
              </li>
              <li
                class="nav-item d-inline-flex align-items-center"
                @click="component = CategoryManagement"
              >
                <a href="javascript:void(0)" class="nav-link text-white" aria-current="page">
                  <mdicon name="shape" class="text-white" />
                  <span class="ms-2 fs-6">Categories</span>
                </a>
              </li>
              <li
                class="nav-item d-inline-flex align-items-center"
                @click="component = ProductManagement"
              >
                <a href="javascript:void(0)" class="nav-link text-white" aria-current="page">
                  <mdicon name="list-box" class="text-white" />
                  <span class="ms-2 fs-6">Products</span>
                </a>
              </li>
              <li
                class="nav-item d-inline-flex align-items-center"
                @click="component = OrdersManagement"
              >
                <a href="javascript:void(0)" class="nav-link text-white" aria-current="page">
                  <mdicon name="format-list-bulleted-type" class="text-white" />
                  <span class="ms-2 fs-6">Orders</span>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </template>
    <suspense timeout="0">
      <template #default>
        <!-- <user-management></user-management> -->
        <component :is="component"></component>
      </template>
      <template #fallback>
        <loading-indicator></loading-indicator>
      </template>
    </suspense>
  </dashboard-layout>
</template>

<script setup>
// import axiosClient from "@/js/axios.js";
// import MainLayout from "@/layouts/MainLayout.vue";
import DashboardLayout from '@/layouts/DashboardLayout.vue'
import CategoryManagement from '@/components/manager/CategoryManagement.vue'
import ProductManagement from '@/components/manager/ProductManagement.vue'
import OrdersManagement from '@/components/OrdersManagement.vue'
import DashBoard from '@/components/manager/DashBoard.vue'
import LoadingIndicator from '@/components/LoadingIndicator.vue'
import { onMounted } from 'vue'
import { useAuthStore } from '@/stores/authstore.js'
import router from '../router/index.js'
import { shallowRef } from 'vue'

const auth = useAuthStore()

const component = shallowRef('DashBoard')
</script>

<style scoped>
.nav-pills .nav-link.active {
  background-color: #374151;
  border-radius: 5px;
}

.nav-pills .nav-item:hover {
  background-color: #374151;
  border-radius: 5px;
}
</style>
