<template>
  <dashboard-layout>
    <div class="row justify-content-center mt-5">
      <h2 class="text-center">Admin's Home!</h2>
    </div>
    <template v-slot:sidebar>
      <div>
        <div class="row">
          <div class="d-flex flex-column justify-content-between col-auto bg-dark min-vh-100">
            <ul class="nav nav-pills flex-column mt-2 mt-sm-0" id="menu">
              <a
                class="text-white text-decoration-none d-inline-flex justify-content-center align-items-center ms-2 my-2"
                rol="button"
              >
                <span class="fs-3 text-warning text-center">Admin</span>
              </a>
              <hr class="text-white p-0" />
              <li class="nav-item d-inline-flex align-items-center" @click="handleNav('admindashboard')">
                <a href="javascript:void(0)" class="nav-link text-white" aria-current="page">
                  <mdicon name="gauge" class="text-white" />
                  <span class="ms-2 fs-6">Dashboard</span>
                </a>
              </li>
              <li
                class="nav-item d-inline-flex align-items-center"
                @click="handleNav('adminusers')"
              >
                <a href="javascript:void(0)" class="nav-link text-white" aria-current="page">
                  <mdicon name="account-multiple" class="text-white" />
                  <span class="ms-2 fs-6">Users</span>
                </a>
              </li>
              <li
                class="nav-item d-inline-flex align-items-center"
                @click="handleNav('admincategories')"
              >
                <a href="javascript:void(0)" class="nav-link text-white" aria-current="page">
                  <mdicon name="shape" class="text-white" />
                  <span class="ms-2 fs-6">Categories</span>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </template>
    <suspense timeout="0">
      <template #default>
        <!-- <component :is="component"></component> -->
        <router-view></router-view>
      </template>
      <template #fallback>
        <loading-indicator></loading-indicator>
      </template>
    </suspense>
  </dashboard-layout>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterView } from 'vue-router'
import { useAuthStore } from '@/stores/authstore.js'
import router from '../router/index.js'
import DashboardLayout from '@/layouts/DashboardLayout.vue'
import LoadingIndicator from '@/components/LoadingIndicator.vue'

const auth = useAuthStore()

onMounted(() => {
  if (auth.user.role !== 'admin') {
    router.push({ name: 'login' })
  } 
})

const handleNav = (route) => {
  router.push({ name: route })
}
</script>

<style scoped>
.nav-pills .nav-item.active {
  background-color: #374151;
  border-radius: 5px;
}

.nav-pills .nav-item:hover {
  background-color: #374151;
  border-radius: 5px;
}
</style>
