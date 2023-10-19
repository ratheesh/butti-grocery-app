<template>
  <main-layout>
    <h2 class="text-center">Admin Dash Board!</h2>
    <div>
      <button class="btn btn-outline-success"
      data-bs-toggle="modal" data-bs-target="#modalAddCategory">
      Add Category</button>
      &nbsp;
      <button class="btn btn-outline-success"
      data-bs-toggle="modal" data-bs-target="#modalAddProduct">Add product</button>
    </div>

    <!-- category Modal -->
    <div class="modal fade" id="modalAddCategory" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="staticBackdropLabel">Add Category</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="form-floating mb-3">
              <input type="text" class="form-control" id="floatingInput" v-model="category" placeholder="Fruits/Vegetables">
              <label for="floatingInput">Category</label>
            </div> 
          </div>
          <div class="modal-footer text-center">
            <button type="button" class="btn btn-sm btn-outline-success" @click="addCategory">Add</button>
            <button type="button" class="btn btn-sm btn-outline-danger" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

  </main-layout>
</template>

<script setup>
import { ref } from "vue";
import axiosClient from "@/js/axios.js";
import MainLayout from "@/layouts/MainLayout.vue";

const category = ref("");

const addCategory = async () => {
  console.log("add category");
  try {
    const resp = await axiosClient.post("/api/category", {
      name: category.value,
    });
    console.log(resp);
  } catch (err) {
    console.log("error");
  }
};

</script>

<style scoped></style>
