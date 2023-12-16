<template>
  <main-layout>
    <h3 class="text-center mt-3">Searching for {{ query }}</h3>
    <div v-if="loading">
      <loading-indicator></loading-indicator>
    </div>
    <div v-else>
      <div v-if="search_results.length < 1">
        <div class="row justify-content-center align-items-center">
          <h2 class="text-center my-5">No Results Found!</h2>
        </div>
      </div>
      <div v-else>
        <div class="row col-10 m-auto justify-content-around">
          <div
            class="row row-cols-sm-2 row-cols-md-3 rows-cols-lg-3 rows-cols-xl-4 row-cols-xxl-5 gx-5 gy-3"
          >
            <div v-for="product in search_results" class="col" :key="product.id">
              <ProductCard :data="product" />
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- <pre>{{ query }}</pre>
    <pre> search results: {{ search_results }}</pre>
    <pre> categories products: {{ categories }}</pre>
    <pre> product search: {{ products }}</pre> -->
  </main-layout>
</template>

<script setup>
import { onMounted, ref, toRefs } from 'vue'
import axiosClient from '@/js/axios.js'
import MainLayout from '@/layouts/MainLayout.vue'
import LoadingIndicator from '@/components/LoadingIndicator.vue'
import ProductCard from '@/components/ProductCard.vue'

const props = defineProps({
  query: {
    type: String,
    required: true
  }
})
const { query } = toRefs(props)
const loading = ref(true)
const search_results = ref([])
const categories = ref([])
const products = ref([])

onMounted(async () => {
  console.log(query.value)
  loading.value = true
  try {
    const resp = await axiosClient.get('/search', { params: { query: query.value } })
    console.log(resp)
    categories.value = resp.data[0] || []
    products.value = resp.data[1] || []
    search_results.value = [...categories.value, ...products.value]
  } catch (err) {
    console.log(err)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped></style>
