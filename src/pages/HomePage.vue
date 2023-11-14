<template>
  <main-layout>
  <div class="main mt-3">
    <div class="container">
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 rows-cols-lg-3 rows-cols-xl-4 row-cols-xxl-4 g-1" >
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
