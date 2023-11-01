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
              <input type="text" class="form-control" id="floatingInput" placeholder="Fruits/Vegetables" v-model="category.name" required>
              <label for="floatingInput">Category</label>
            </div> 
            <div class="mb-3">
              <label for="imageFile mb-1">Category Image</label>
              <input class="form-control" type="file" id="imageFile" accept="image/jpeg" @change='handleImage'>
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
          <pre>{{ category }}</pre>
        </div>
      </div>
    </div>
</template>


<script setup>
import { ref, reactive } from "vue";
import axiosClient from '@/js/axios.js';

const loading = ref(false);
const emit = defineEmits(["add-category"]);
const category = reactive({
  name: "",
  image: null,
  file: null,
});

const errordata = reactive({
  isError: false,
  msg: "",
})

const handleImage = (e) => {
  console.log("modal: handle Image");
  category.file = e.target.files[0];
  category.image = category.file.name;
  createBase64Image(category.file);
};

function createBase64Image(fObj) {
    const reader = new FileReader();
    reader.onload = (e) => {
      category.file = e.target.result.split(",")[1];
    };
    reader.readAsDataURL(fObj);
  }

const addCategory = async() => {
  console.log("modal: add category");

  const formData = new FormData();
  formData.append("name", category.name);
  formData.append("image", category.image);
  formData.append("file", category.file);

  console.log(formData.getAll('file'))

  loading.value = true;
  try {
    const resp = await axiosClient.post("/api/category", formData);
    console.log(resp);
    console.log('modal: closing modal')
    document.getElementById("categoryModalClose").click()
    emit("add-category", category);
  } catch (err) {
    console.log(err);
    errordata.isError = true;
    errordata.msg = err.response.data.message;
  } finally {
    category.name = "";
    category.image = null;
    category.file = null;
    errordata.isError = false;
    loading.value = false;
  }

};
</script>

<style scoped></style>