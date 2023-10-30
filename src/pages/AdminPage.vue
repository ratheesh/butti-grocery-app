<template>
  <main-layout>
    <h2 class="text-center">Admin Dash Board!</h2>
    <div>
      <button class="btn btn-outline-success"
      data-bs-toggle="modal" data-bs-target="#modalCategory">
      Add Category</button>
      &nbsp;
      <button class="btn btn-outline-success"
      data-bs-toggle="modal" data-bs-target="#modalProduct">Add product</button>
    </div>
    <category-modal @add-category="addCategory" ></category-modal>
  </main-layout>
</template>

<script setup>
// import axiosClient from "@/js/axios.js";
import MainLayout from "@/layouts/MainLayout.vue";
import CategoryModal from "@/components/CategoryModal.vue";
// import { onMounted } from "vue";
// import { Modal } from 'bootstrap'

const addCategory = (category) => {
  console.log("admin: complete category");
  console.log(category)
};

</script>

<style scoped></style>
