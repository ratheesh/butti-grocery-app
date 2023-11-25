<template>
  <main-layout>
    <h2 class="text-center">Manager Dashboard</h2>
    <div>
      <suspense>
        <template #default>
          <div>
            <category-management></category-management>
            <product-management></product-management>
          </div>
        </template>
        <template #fallback>
          <loading-indicator></loading-indicator>
        </template>
      </suspense>
    </div>
  </main-layout>
</template>

<script setup>
import MainLayout from "@/layouts/MainLayout.vue";
import CategoryManagement from "@/components/CategoryManagement.vue";
import ProductManagement from "@/components/ProductManagement.vue";
import LoadingIndicator from '@/components/LoadingIndicator.vue'
// import axiosClient from '@/js/axios.js';
// import { ref, onMounted } from 'vue';

</script>

<style scoped></style>
