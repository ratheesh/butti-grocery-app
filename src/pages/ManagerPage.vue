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
      <pre>Categories: {{ categories }}</pre>
      <pre>Products: {{ products }}</pre>
    </div>
  </main-layout>
</template>

<script setup>
import MainLayout from "@/layouts/MainLayout.vue";
import CategoryModal from "@/components/CategoryModal.vue";
import ProductModal from "@/components/ProductModal.vue";
import axiosClient from '@/js/axios.js';
import { ref, onMounted } from 'vue';
// import bootstrap from "bootstrap";

const categories = ref([]);
const products = ref([]);

onMounted(async() => {
  try {
    const res = await axiosClient.get("http://localhost:5000/api/category");
    console.log(res)
    categories.value = res.data
  } catch (error) {
    console.log('Error: ', error);
  }

  try {
    const res = await axiosClient.get("http://localhost:5000/api/product/1");
    console.log(res)
    products.value = res.data
  } catch (error) {
    console.log('Error: ', error);
  }
})

function refreshCategories() {
  console.log('refreshing categories')
  axiosClient.get("http://localhost:5000/api/category")
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
  axiosClient.get("http://localhost:5000/api/product/1")
    .then((res) => {
      console.log(res)
      categories.value = res.data
    })
    .catch((err) => {
      console.log('Error: ', err);
    })
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
