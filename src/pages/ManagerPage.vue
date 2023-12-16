<template>
  <dashboard-layout>
    <div class="container">
      <div class="row justify-content-center mt-5">
        <h2 v-if="user.approved" class="text-center">Manager's Home!</h2>
      </div>
    </div>
    <template v-slot:sidebar>
      <div v-if="user.approved">
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
              <li
                class="nav-item d-inline-flex align-items-center"
                :class="route.name == 'managerdashboard' ? 'active' : ''"
              >
                <router-link
                  to="/manager/dashboard"
                  class="nav-link text-white"
                  aria-current="page"
                >
                  <mdicon name="gauge" class="text-white" />
                  <span class="ms-2 fs-6">Dashboard</span>
                </router-link>
              </li>
              <li
                class="nav-item d-inline-flex align-items-center"
                :class="route.name == 'managercategories' ? 'active' : ''"
              >
                <router-link to="/manager/category" class="nav-link text-white" aria-current="page">
                  <mdicon name="shape" class="text-white" />
                  <span class="ms-2 fs-6">Categories</span>
                </router-link>
              </li>
              <li
                class="nav-item d-inline-flex align-items-center"
                :class="route.name == 'managerproducts' ? 'active' : ''"
              >
                <router-link to="/manager/products" class="nav-link text-white" aria-current="page">
                  <mdicon name="list-box" class="text-white" />
                  <span class="ms-2 fs-6">Products</span>
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </template>
    <div v-if="!user.approved">
      <div class="row col-md-6 m-auto">
        <div class="card card-body justify-content-center m-auto shadow-sm">
          <div class="fs-4">
            <div class="row col-md-6 m-auto">
              <p class="text-center">
                <span class="bold">You account is not approved yet! </span>
                <br />
                <span class="bold">Please wait for the admin to approve your account.</span>
              </p>
            </div>
            <div class="row col-md-6 m-auto">
              <a href="javascript:void(0)" class="btn btn-sm btn-primary" @click="auth.logout"
                >Logout</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <suspense timeout="0">
        <template #default>
          <router-view></router-view>
        </template>
        <template #fallback>
          <loading-indicator></loading-indicator>
        </template>
      </suspense>
    </div>
  </dashboard-layout>
</template>

<script setup>
import { RouterView } from 'vue-router'
import { storeToRefs } from 'pinia'
import { useAuthStore } from '../stores/authstore'
import { useRoute } from 'vue-router'
import DashboardLayout from '@/layouts/DashboardLayout.vue'
import LoadingIndicator from '@/components/LoadingIndicator.vue'

const auth = useAuthStore()
const route = useRoute()
const { user } = storeToRefs(auth)
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
