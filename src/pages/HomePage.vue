<template>
  <main-layout>
  <div class="main">
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
      <div class="row row-cols-sm-2 row-cols-md-3 rows-cols-lg-3 rows-cols-xl-4 row-cols-xxl-5 g-2" >
        <div v-for="product in products" class="col" :key="product.id">
          <ProductCard :data="product"/>
        </div>
      </div>
    </div>
  </div>
  </main-layout>
</template>

<script setup>
import MainLayout from "@/layouts/MainLayout.vue";
import ProductCard from "@/components/ProductCard.vue";

import { ref, onMounted } from "vue";
import axiosClient from '@/js/axios.js'

const products=ref([])
onMounted(async() => {
  console.log('Fetching products')
  axiosClient.get('/api/product')
    .then(res => {
      console.log(res)
      products.value = res.data
    })
    .catch(err => {
      console.log(err)
    })
});


</script>
