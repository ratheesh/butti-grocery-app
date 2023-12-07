<template>
  <dashboard-layout>
    <h2 class="text-center">Admin Dash Board!</h2>
    <template v-slot:sidebar>
      <div>
        <div class="row">
          <div class="d-flex flex-column justify-content-between col-auto bg-dark min-vh-100">
            <ul class="nav nav-pills flex-column mt-2 mt-sm-0" id="menu">
              <a class="text-white text-decoration-none d-inline-flex justify-content-center align-items-center ms-2 my-2" rol="button">
                <span class="fs-3 text-warning text-center">Admin</span>
              </a>
              <hr class="text-white p-0" />
              <li class="nav-item d-inline-flex align-items-center" @click="component=DashBoard">
                <a href="javascript:void(0)" class="nav-link text-white" aria-current="page">
                  <mdicon name="gauge" class="text-white" />
                  <span class="ms-2 fs-6">Dashboard</span>
                </a>
              </li>
              <li class="nav-item d-inline-flex align-items-center" @click="component=UserManagement">
                <a href="javascript:void(0)" class="nav-link text-white" aria-current="page">
                  <mdicon name="account-multiple" class="text-white" />
                  <span class="ms-2 fs-6">Users</span>
                </a>
              </li>
              <li class="nav-item d-inline-flex align-items-center" @click="component=CategoryRequests">
                <a href="javascript:void(0)" class="nav-link text-white" aria-current="page">
                  <mdicon name="shape" class="text-white" />
                  <span class="ms-2 fs-6">Categories</span>
                </a>
              </li>
              <li class="nav-item d-inline-flex align-items-center" @click="component=Analytics">
                <a href="javascript:void(0)" class="nav-link text-white" aria-current="page">
                  <mdicon name="chart-line" class="text-white" />
                  <span class="ms-2 fs-6">Analytics</span>
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
        <template  #fallback>
         <loading-indicator></loading-indicator>
        </template>
      </suspense>
  </dashboard-layout>
</template>

<script setup>
// import axiosClient from "@/js/axios.js";
// import MainLayout from "@/layouts/MainLayout.vue";
import DashboardLayout from "@/layouts/DashboardLayout.vue";
import UserManagement from "@/components/admin/UserManagement.vue";
import CategoryRequests from "@/components/admin/CategoryRequests.vue";
import Analytics from "@/components/admin/AnalyticsComponent.vue";
import LoadingIndicator from '@/components/LoadingIndicator.vue';
import DashBoard from '@/components/admin/DashBoard.vue';
import { onMounted } from "vue";
import { useAuthStore } from '@/stores/authstore.js';
import router from '../router/index.js'
import { shallowRef } from 'vue';

const auth = useAuthStore();

const component = shallowRef('DashBoard');

onMounted(() => {
  if (auth.user.role !== 'admin') {
    router.push({ name: 'login' });
  }
})

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
