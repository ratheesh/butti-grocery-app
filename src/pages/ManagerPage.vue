<template>
  <main-layout>
    <h2 class="text-center">Manager Dashboard</h2>
    <div>
      <button class="btn btn-outline-success"
      data-bs-toggle="modal" data-bs-target="#modalCategory">
      Add Category
      </button>
      &nbsp;
      <button class="btn btn-outline-success"
      data-bs-toggle="modal" data-bs-target="#modalProduct">
      Add Product
      </button>
      <category-modal @add-category="addCategory" ></category-modal>
      <product-modal :categories="categories" @add-product="addProduct" ></product-modal>
      <div class="row col-10 g-3 m-3">
        <category-card v-for='category in categories' :key='category.id' :category='category'></category-card>
      </div>
      <pre>Categories: {{ categories }}</pre>
      <pre>Products: {{ products }}</pre>
    </div>
  </main-layout>
</template>

<script setup>
import MainLayout from "@/layouts/MainLayout.vue";
import CategoryModal from "@/components/CategoryModal.vue";
import ProductModal from "@/components/ProductModal.vue";
import CategoryCard from "@/components/CategoryCard.vue";
import axiosClient from '@/js/axios.js';
import { ref, onMounted } from 'vue';
// import bootstrap from "bootstrap";

const categories = ref([]);
const products = ref([]);

onMounted(async() => {
  try {
    const res = await axiosClient.get("/api/category");
    console.log(res)
    categories.value = res.data
  } catch (error) {
    console.log('Error: ', error);
  }

  products.value = []
  for (const category of categories.value) {
    console.log('Category:', category.id)
    axiosClient.get(`/api/product/${category.id}`)
      .then((res) => {
        console.log(res)
        products.value.push(...res.data)
      })
      .catch((err) => {
        console.log('Error: ', err);
      })
  }
})

async function refreshCategories() {
  console.log('refreshing categories')
  axiosClient.get("/api/category")
    .then((res) => {
      console.log(res)
      categories.value = res.data
    })
    .catch((err) => {
      console.log('Error: ', err);
    })
}

function refreshProducts() {
  console.log('refreshing products')
  products.value = []
  for (const category of categories.value) {
    console.log('Category:', category.id)
    axiosClient.get(`/api/product/${category.id}`)
      .then((res) => {
        console.log(res)
        products.value.push(...res.data)
      })
      .catch((err) => {
        console.log('Error: ', err);
      })
  }
}

const addCategory = (category) => {
  console.log("add category");
  console.log(category)
  refreshCategories()
};

const addProduct = (product) => {
  console.log("add product");
  console.log(product)
  refreshProducts()
};

</script>

<style scoped></style>
