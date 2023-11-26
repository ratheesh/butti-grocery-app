<template>
  <main-layout>
  <div class="main">
    <div v-if="!loading">
      <div class="container">
        <div class="row col-12 justify-content-end rounded m-auto mb-2">
          <div class="col-4 col-auto">
            <select class="form-select">
              <option value="1">All</option>
              <option value="2">Fruits</option>
              <option value="3">Vegetables</option>
              <option value="4">Grocery</option>
              <option value="5">Dairy</option>
            </select>
          </div>
        </div>
        <div class="row row-cols-sm-2 row-cols-md-3 rows-cols-lg-3 rows-cols-xl-4 row-cols-xxl-5 gx-5 gy-3" >
          <div v-for="product in products" class="col" :key="product.id">
            <ProductCard :data="product"/>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <loading-indicator></loading-indicator>
    </div>
  </div>
  </main-layout>
</template>

<script setup>
import MainLayout from "@/layouts/MainLayout.vue";
import ProductCard from "@/components/ProductCard.vue";
import LoadingIndicator from '@/components/LoadingIndicator.vue';

import { ref } from "vue";
import axiosClient from '@/js/axios.js'

const products=ref([])
const loading = ref(true)

async function fetchData() {
  console.log('Fetching data...')
  loading.value = true
  try {
    const resp = await axiosClient.get('/api/product')
    console.log(resp)
    products.value = resp.data
  } catch (err) {
    console.log(err)
  } finally {
    loading.value = false
  }
}

fetchData()
</script>
