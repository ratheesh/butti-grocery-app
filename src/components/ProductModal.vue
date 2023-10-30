<template>
    <div class="modal fade" id="modalProduct" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div v-if="categories.length > 0">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="staticBackdropLabel">Add Product</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="form-floating mb-3">
              <input type="text" class="form-control" id="productName" placeholder="apple/bananas" v-model="product.name" required>
              <label for="productName">Name</label>
            </div> 
            <div class="form-floating mb-3">
              <textarea type="text" class="form-control" id="productDescription" placeholder="Description" v-model="product.description" required></textarea>
              <label for="productDescription">Description</label>
            </div> 
            <div class="form-floating mb-3">
              <select class="form-select" id="productCategory" aria-label="Category" v-model="category_id">
                <option v-for='category in props.categories' :key="category.id" :value='category.id' >{{ category.name }}</option>
              </select>
              <label for="productCategory">Category</label>
            </div>
            <div class="form-floating mb-3">
              <select class="form-select" id="productCategory" aria-label="Category">
                <option selected value='piece'>Piece</option>
                <option value='kg'>Kg</option>
                <option value='500gm'>500gm</option>
                <option value='litre'>Litre</option>
                <option value='500ml'>500ml</option>
                <option value='dozen'>Dozen</option>
              </select>
              <label for="productCategory">Category</label>
            </div>
            <div class="form-floating mb-3">
              <input type="text" class="form-control" id="productPrice" placeholder="Price" v-model="product.price" required>
              <label for="productPrice">Price</label>
            </div> 
            <div class="form-floating mb-3">
              <input type="text" class="form-control" id="productStock" placeholder="Stock" v-model="product.stock" required>
              <label for="productStock">Stock</label>
            </div> 
            <div class="form-floating mb-3">
              <input type="date" class="form-control" id="productExpiryDate" placeholder="Expiry Date" v-model="product.expiry_date" required>
              <label for="productExpiryDate">Expiry Date</label>
            </div> 
            <div class="mb-3">
              <label for="productPhoto">Product Photo</label>
              <input type="file" class="form-control" id="productPhoto" placeholder="Photo">
            </div> 
          </div>
          <div class="modal-footer text-center">
            <button type="button" class="btn btn-sm btn-outline-success" @click="addProduct">
              <span v-if="loading" class="spinner-border spinner-border-sm"></span>
              Add
            </button>
            <button type="button" class="btn btn-sm btn-outline-danger" id="productModalClose" data-bs-dismiss="modal">Close</button>
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
        <div v-else>
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="staticBackdropLabel">Product Management</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <h4 class="mt-3 text-center">No Categories present!</h4>
            <p class="text-center">Add a category before adding Product</p>
            <div class="modal-footer text-center">
              <button type="button" class="btn btn-sm btn-outline-danger" id="productModalClose" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>


<script setup>
import { ref, reactive } from "vue";
import axiosClient from '@/js/axios.js';

const props = defineProps({
  categories: {
    type: Array,
    required: true,
  },
})  

const loading = ref(false);
const emit = defineEmits(["add-product"]);
const category_id = ref(1);
const product = reactive({
  name: "",
  description: "",
  unit: "",
  price: 0,
  stock: 0,
  expiry_date: "",
  image: "",
});
const errordata = reactive({
  isError: false,
  msg: "",
})

// const onCategoryChange = (event) => {
//   console.log('category changed')
//   console.log(event.target.value)
//   category_id.value = event.target.value
// }

const addProduct = async() => {
  console.log("modal: add product");
  loading.value = true;
  try {
    const resp = await axiosClient.post(`/api/product/${category_id.value}`, {
      name: product.name,
      description: product.description,
      unit: product.unit,
      price: product.price,
      stock: product.stock,
      expiry_date: String(`${product.expiry_date} 00:00`),
      image: product.image,
    });
    console.log(resp);
    console.log('modal: closing modal')
    document.getElementById("productModalClose").click()
    emit("add-product", product);
  } catch (err) {
    console.log(err);
    errordata.isError = true;
    errordata.msg = err.message;
  } finally {
    loading.value = false;
  }

};
</script>

<style scoped></style>