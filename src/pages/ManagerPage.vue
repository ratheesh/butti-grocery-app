<template>
  <main-layout>
    <h2 class="text-center">Manager Dashboard</h2>
    <div>
      <button class="btn btn-outline-success"
      data-bs-toggle="modal" data-bs-target="#modalAddCategory">
      Add Category
      </button>
      &nbsp;
      <button class="btn btn-outline-success"
      data-bs-toggle="modal" data-bs-target="#modalAddProduct">
      Add Product
      </button>
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
              <input type="text" class="form-control" id="floatingInput" placeholder="Fruits/Vegetables">
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

    <!-- Add product Modal -->
    <div class="modal fade" id="modalAddProduct" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="staticBackdropLabel">Add Product</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="form-floating mb-3">
              <select name="category" id="category" class="form-control" required="yes" v-model="category">
                <!-- <option v-for='option in options' :value='option'>{{ option }}</option> -->
                <option value="test">test</option>
                <option value="test1">test1</option>
              </select>
              <label for="category" class="form-label">Category</label>
            </div>
            <div class="form-floating mb-3">
              <input type="text" class="form-control" id="floatingInput" placeholder="Apples/Oranges...">
              <label for="floatingInput">Product</label>
            </div> 
          </div>
          <div class="modal-footer text-center">
            <button type="button" class="btn btn-sm btn-outline-success" @click="addProduct">Add</button>
            <button type="button" class="btn btn-sm btn-outline-danger" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </main-layout>
</template>

<script setup>
import MainLayout from "@/layouts/MainLayout.vue";

const addCategory = () => {
  console.log("add category");
};

const addProduct = () => {
  console.log("add product");
};
</script>

<style scoped></style>
