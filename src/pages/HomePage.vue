<template>
  <main-layout>
    <div class="main">
      <div v-if="loading">
        <loading-indicator></loading-indicator>
      </div>
      <div v-else>
        <div class="container">
          <div v-if="!products.length">
            <div class="row col-md-6 justify-content-center m-auto mt-5">
              <div class="col-8">
                <h3 class="text-center">We are Sorry!</h3>
                <hr>
                <h4>We have nothing to offer!</h4>
                <h5>Do visit again for fresh groceries!</h5>
                <small class="row justify-content-end">Butti Groceries Admin Team</small>
              </div>
              
            </div>
          </div>
          <div v-else>
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
            <div class="row row-cols-sm-2 row-cols-md-3 rows-cols-lg-3 rows-cols-xl-4 row-cols-xxl-5 gx-5 gy-3">
              <div v-for="product in products" class="col" :key="product.id">
                <ProductCard :data="product" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main-layout>
</template>

<script setup>
import MainLayout from "@/layouts/MainLayout.vue";
import ProductCard from "@/components/ProductCard.vue";
import LoadingIndicator from "@/components/LoadingIndicator.vue";

import { ref, onMounted } from "vue";
import axiosClient from "@/js/axios.js";
import router from "@/router/index.js";
import { storeToRefs } from "pinia";
import { useAuthStore } from "../stores/authstore";

const products = ref([]);
const loading = ref(true);

onMounted(() => {
  const auth = useAuthStore();
  const { user, authenticated } = storeToRefs(auth);
  if (authenticated) {
    if (user.value.role === "admin") {
      router.push({ name: "admin" });
    } else if (user.value.role === "manager") {
      router.push({ name: "manager" });
    }
  }
});

async function fetchData() {
  console.log("Fetching data...");
  loading.value = true;
  try {
    const resp = await axiosClient.get("/home");
    console.log(resp);
    products.value = resp.data;
    // products.value = products.value.filter((x) => new Date(x.expiry_date) > Date.now());
  } catch (err) {
    console.log(err);
  } finally {
    loading.value = false;
  }
}

fetchData();
</script>
