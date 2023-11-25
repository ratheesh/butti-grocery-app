<template>
  <main-layout>
    <h2 class="text-center">Admin Dash Board!</h2>
    <div>
      <suspense>
        <template #default>
          <user-management></user-management>
        </template>
        <template  #fallback>
         <loading-indicator></loading-indicator>
        </template>
      </suspense>
    </div>
  </main-layout>
</template>

<script setup>
// import axiosClient from "@/js/axios.js";
import MainLayout from "@/layouts/MainLayout.vue";
import UserManagement from "@/components/UserManagement.vue";
import LoadingIndicator from '@/components/LoadingIndicator.vue';

</script>

<style scoped></style>
