<template>
  <main-layout>
    <div class="main">
      <div class="row col-10 m-auto justify-content-around">
        <div class="col-12">
          <h3 class="text-center mt-3">Welcome to Butti Grocery Shop!</h3>
          <hr />
        </div>
      </div>
      <div v-if="loading">
        <loading-indicator></loading-indicator>
      </div>
      <div v-else>
        <div class="container">
          <div v-if="!products.length">
            <div class="row col-md-6 justify-content-center m-auto mt-5">
              <div class="col-8">
                <h3 class="text-center">We are Sorry!</h3>
                <hr />
                <h4>We have nothing to offer!</h4>
                <h5>Do visit again for fresh groceries!</h5>
                <small class="row justify-content-end">Butti Groceries Admin Team</small>
              </div>
            </div>
          </div>
          <div v-else>
            <div class="row justify-content-end align-content-center mt-3">
              <div class="col-auto">
                <select
                  class="form-select me-3"
                  aria-label="Default select example"
                  @change="onCategoryChange($event)"
                >
                  <option value="all" selected>All</option>
                  <option v-for="category in categories" :key="category.id" :value="category.name">
                    {{ category.name }}
                  </option>
                </select>
              </div>
              <div class="col-auto">
                <button class="btn btn-primary" @click="fetchData">
                  <mdicon name="refresh" size="20" />
                  <span class="mx-2">Refresh</span>
                </button>
              </div>
            </div>
            <div v-if="!show_products.length">
              <h5 class="text-center mt-5">No products found!</h5>
              <p class="text-center">Select diffent Category product from the drop down.</p>
            </div>
            <div v-else>
              <div
                class="row row-cols-sm-2 row-cols-md-3 rows-cols-lg-3 rows-cols-xl-4 row-cols-xxl-5 gx-5 gy-3 mt-3"
              >
                <div v-for="product in show_products" class="col" :key="product.id">
                  <ProductCard :data="product" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main-layout>
</template>

<script setup>
import MainLayout from '@/layouts/MainLayout.vue'
import ProductCard from '@/components/ProductCard.vue'
import LoadingIndicator from '@/components/LoadingIndicator.vue'

import { ref, onMounted } from 'vue'
import axiosClient from '@/js/axios.js'
import router from '@/router/index.js'
import { storeToRefs } from 'pinia'
import { useAuthStore } from '../stores/authstore'

const products = ref([])
const show_products = ref([])
const categories = ref([])
const loading = ref(true)

onMounted(() => {
  const auth = useAuthStore()
  const { user, authenticated } = storeToRefs(auth)
  if (authenticated) {
    if (user.value.role === 'admin') {
      router.push({ name: 'admin' })
    } else if (user.value.role === 'manager') {
      router.push({ name: 'manager' })
    }
  }
})

async function fetchData() {
  console.log('Fetching data...')
  loading.value = true
  try {
    const resp = await axiosClient.get('/home')
    console.log(resp)
    categories.value = resp.data[0]
    products.value = resp.data[1]
    show_products.value = products.value

    // sort based on the updated timestamp
    show_products.value.sort(
      (a, b) => new Date(a.updated_timestamp).getDate() < new Date(b.updated_timestamp).getDate()
    )
    // products.value = products.value.filter((x) => new Date(x.expiry_date) > Date.now());
  } catch (err) {
    console.log(err)
  } finally {
    loading.value = false
  }
}

const onCategoryChange = (event) => {
  console.log(event.target.value)
  if (event.target.value === 'all') {
    show_products.value = products.value
  } else {
    show_products.value = products.value.filter((x) => x.category_name === event.target.value)
  }
  show_products.value.sort(
    (a, b) => new Date(a.updated_timestamp).getDate() < new Date(b.updated_timestamp).getDate()
  )
}

fetchData()
</script>
