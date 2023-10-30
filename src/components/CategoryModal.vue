<template>
    <div class="modal fade" id="modalCategory" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="staticBackdropLabel">Add Category</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="form-floating mb-3">
              <input type="text" class="form-control" id="floatingInput" placeholder="Fruits/Vegetables" v-model="category" required>
              <label for="floatingInput">Category</label>
            </div> 
          </div>
          <div class="modal-footer text-center">
            <button type="button" class="btn btn-sm btn-outline-success" @click="addCategory">
              <span v-if="loading" class="spinner-border spinner-border-sm"></span>
              Add
            </button>
            <button type="button" class="btn btn-sm btn-outline-danger" id="categoryModalClose" data-bs-dismiss="modal">Close</button>
          </div>
          <div class="row d-flex justify-content-center" v-if="errordata.isError">
            <div class="col-11 text-center">
              <div class="alert alert-danger" role="alert">
                {{ errordata.msg }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>


<script setup>
import { ref, reactive } from "vue";
import axiosClient from '@/js/axios.js';

const loading = ref(false);
const emit = defineEmits(["add-category"]);
const category = ref("");
const errordata = reactive({
  isError: false,
  msg: "",
})

const addCategory = async() => {
  console.log("modal: add category");
  loading.value = true;
  try {
    const resp = await axiosClient.post("/api/category", {
      name: category.value,
    });
    console.log(resp);
    console.log('modal: closing modal')
    document.getElementById("categoryModalClose").click()
    emit("add-category", category);
  } catch (err) {
    console.log(err);
    errordata.isError = true;
    errordata.msg = err.response.data.message;
  } finally {
    loading.value = false;
  }

};
</script>

<style scoped></style>