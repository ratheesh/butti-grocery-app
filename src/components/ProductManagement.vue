<template>
  <div class="row col-8 m-auto">
    <h2 class="text-center mt-5">Product Management</h2>
    <div class="card">
      <div class="row col-10 justify-content-between m-auto mt-3">
        <div class="col-auto">
          <button class="btn btn-sm btn-outline-rosy-brown" @click="gotoCategories">
            <b><mdicon name="cog" :size="18" /></b>
            Categories
          </button>
        </div>
        <div class="col-auto">
          <button class="btn btn-sm btn-success" @click="handleProductAdd({}, false)">
            <b><mdicon name="shape-square-rounded-plus" class="text-white" :size="18" /></b>
            Add
          </button>
        </div>
      </div>
      <div v-if="products.length > 0">
        <div class="row justify-content-center mt-3 m-auto">
          <div class="col-10">
            <!-- <hr /> -->
            <table class="table text-center">
              <thead class="fs-6 table-secondary">
                <tr>
                  <th scope="col"><b>#</b></th>
                  <th scope="col"><b>NAME</b></th>
                  <th scope="col"></th>
                  <th scope="col"></th>
                  <th scope="col"></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(product, idx) in products" :id="idx" :key="idx">
                  <td class="align-middle">{{ product.id }}</td>
                  <td class="align-middle"><img class="mx-2" :src="`${backend_url_base}/${product.image_name}`" height="40" width="40"/>{{ product.name }}</td>
                  <td class="align-middle">
                    <button class="btn btn-sm btn-secondary" @click="handleProductDetails(product)">
                      <mdicon name="cog" class="text-white" :size="16" />
                      Details
                    </button>
                  </td>
                  <td class="align-middle">
                    <button class="btn btn-sm btn-warning" @click="handleProductAdd(product, true)">
                      <!-- <mdicon name="pencil" class="text-white" :size="16" /> -->
                      <svg width="18px" height="18px" viewBox="0 0 24 24" fill="#fff" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M21.1213 2.70705C19.9497 1.53548 18.0503 1.53547 16.8787 2.70705L15.1989 4.38685L7.29289 12.2928C7.16473 12.421 7.07382 12.5816 7.02986 12.7574L6.02986 16.7574C5.94466 17.0982 6.04451 17.4587 6.29289 17.707C6.54127 17.9554 6.90176 18.0553 7.24254 17.9701L11.2425 16.9701C11.4184 16.9261 11.5789 16.8352 11.7071 16.707L19.5556 8.85857L21.2929 7.12126C22.4645 5.94969 22.4645 4.05019 21.2929 2.87862L21.1213 2.70705ZM18.2929 4.12126C18.6834 3.73074 19.3166 3.73074 19.7071 4.12126L19.8787 4.29283C20.2692 4.68336 20.2692 5.31653 19.8787 5.70705L18.8622 6.72357L17.3068 5.10738L18.2929 4.12126ZM15.8923 6.52185L17.4477 8.13804L10.4888 15.097L8.37437 15.6256L8.90296 13.5112L15.8923 6.52185ZM4 7.99994C4 7.44766 4.44772 6.99994 5 6.99994H10C10.5523 6.99994 11 6.55223 11 5.99994C11 5.44766 10.5523 4.99994 10 4.99994H5C3.34315 4.99994 2 6.34309 2 7.99994V18.9999C2 20.6568 3.34315 21.9999 5 21.9999H16C17.6569 21.9999 19 20.6568 19 18.9999V13.9999C19 13.4477 18.5523 12.9999 18 12.9999C17.4477 12.9999 17 13.4477 17 13.9999V18.9999C17 19.5522 16.5523 19.9999 16 19.9999H5C4.44772 19.9999 4 19.5522 4 18.9999V7.99994Z"
                         fill="#000"/>
                      </svg>
                      Edit
                    </button>
                  </td>
                  <td class="align-middle">
                    <button class="btn btn-sm btn-danger" @click="handleProductDelete(product)">
                      <mdicon name="delete" class="text-white" :size="16" />
                      Delete
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div v-else>
        <div v-if="categories.length === 0" class="row col-12">
          <p class="text-center mt-1">
            No Categories. Atleast one category should be added before adding a product
          </p>
          <p class="text-center mt-1">
            Click <b>here</b> go to category page and add one!
          </p>
        </div>
        <div v-else class="row col-12">
          <h4 class="text-center mt-1">No Products. Add one!</h4>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Windows -->

  <!-- Add/Edit Category -->
  <div
    class="modal fade"
    id="modalProduct"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="staticBackdropLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h1 v-if="!edit" class="modal-title fs-5" id="staticBackdropLabel">Add Product</h1>
          <h1 v-else class="modal-title fs-5" id="staticBackdropLabel">Update Product</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="form-floating mb-3">
            <input
              type="text"
              class="form-control"
              id="productName"
              placeholder="apple/bananas"
              v-model="data.name"
              required
            />
            <label for="productName">Name</label>
          </div>
          <div class="form-floating mb-3">
            <textarea
              type="text"
              class="form-control"
              id="productDescription"
              placeholder="Description"
              v-model="data.description"
              required
            ></textarea>
            <label for="productDescription">Description</label>
          </div>
          <div class="form-floating mb-3">
            <select
              class="form-select"
              id="productCategory"
              aria-label="Category"
              v-model="category_id"
            >
              <option v-for="category in data.categories" :key="category.id" :value="category.id">
                {{ category.name }}
              </option>
            </select>
            <label for="productCategory">Category</label>
          </div>
          <div class="form-floating mb-3">
            <select class="form-select" id="productUnit" aria-label="Unit" required=yes v-model="data.unit">
              <option v-for='(unit, idx) in units' :key="idx" :value='unit'>{{ unit }}</option>
            </select>
            <label for="productUnit">Unit</label>
          </div>
          <div class="form-floating mb-3">
            <input
              type="text"
              class="form-control"
              id="productPrice"
              placeholder="Price"
              v-model="data.price"
              required
            />
            <label for="productPrice">Price</label>
          </div>
          <div class="form-floating mb-3">
            <input
              type="text"
              class="form-control"
              id="productStock"
              placeholder="Stock"
              v-model="data.stock"
              required
            />
            <label for="productStock">Stock</label>
          </div>
          <div class="form-floating mb-3">
            <input
              type="date"
              class="form-control"
              id="productExpiryDate"
              placeholder="Expiry Date"
              v-model="data.expiry_date"
              required
            />
            <label for="productExpiryDate">Expiry Date</label>
          </div>
          <div class="mb-3">
            <label for="productImage">Product Image</label>
            <input
              type="file"
              class="form-control"
              id="productImage"
              placeholder="Product Image"
              accept="image/png, image/jpeg"
              value=""
              @change="handleImage"
            />
          </div>
        </div>
        <div class="modal-footer text-center">
          <button
            v-if="edit"
            @click="handleProductModalEdit(true)"
            type="button"
            class="btn btn-sm btn-warning"
          >
            <span v-if="loading" class="spinner-border spinner-border-sm"></span>
            <span v-else>
              <!-- <mdicon name="pencil" class="text-white" :size="16" /> -->
              <svg width="16px" height="16px" viewBox="0 0 24 24" fill="#fff" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M21.1213 2.70705C19.9497 1.53548 18.0503 1.53547 16.8787 2.70705L15.1989 4.38685L7.29289 12.2928C7.16473 12.421 7.07382 12.5816 7.02986 12.7574L6.02986 16.7574C5.94466 17.0982 6.04451 17.4587 6.29289 17.707C6.54127 17.9554 6.90176 18.0553 7.24254 17.9701L11.2425 16.9701C11.4184 16.9261 11.5789 16.8352 11.7071 16.707L19.5556 8.85857L21.2929 7.12126C22.4645 5.94969 22.4645 4.05019 21.2929 2.87862L21.1213 2.70705ZM18.2929 4.12126C18.6834 3.73074 19.3166 3.73074 19.7071 4.12126L19.8787 4.29283C20.2692 4.68336 20.2692 5.31653 19.8787 5.70705L18.8622 6.72357L17.3068 5.10738L18.2929 4.12126ZM15.8923 6.52185L17.4477 8.13804L10.4888 15.097L8.37437 15.6256L8.90296 13.5112L15.8923 6.52185ZM4 7.99994C4 7.44766 4.44772 6.99994 5 6.99994H10C10.5523 6.99994 11 6.55223 11 5.99994C11 5.44766 10.5523 4.99994 10 4.99994H5C3.34315 4.99994 2 6.34309 2 7.99994V18.9999C2 20.6568 3.34315 21.9999 5 21.9999H16C17.6569 21.9999 19 20.6568 19 18.9999V13.9999C19 13.4477 18.5523 12.9999 18 12.9999C17.4477 12.9999 17 13.4477 17 13.9999V18.9999C17 19.5522 16.5523 19.9999 16 19.9999H5C4.44772 19.9999 4 19.5522 4 18.9999V7.99994Z"
                 fill="#000"/>
              </svg>
            </span>
            Update
          </button>
          <button
            v-else
            @click="handleProductModalEdit(false)"
            type="button"
            class="btn btn-sm btn-success"
          >
            <span v-if="loading" class="spinner-border spinner-border-sm"></span>
            <span v-else><b><mdicon name="shape-square-rounded-plus" class="text-white" :size="18" /></b></span>
            Add
          </button>
          <button
            type="button"
            class="btn btn-sm btn-danger"
            id="productModalClose"
            data-bs-dismiss="modal"
          >
            <mdicon name="window-close" class="text-white" :size="18" />
            Close
          </button>
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

  <div class="modal fade" id="modalProductDelete" role="dialog" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Delete Product</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <p>This will delete the product. This action is irreversible</p>
          <p>Are you sure you want to do this?</p>
        </div>
        <div class="modal-footer">
          <button @click="handleProductModalDelete" type="button" class="btn btn-danger">
            <span v-if="loading" class="spinner-border spinner-border-sm"></span>
            <span v-else><mdicon name="delete" class="text-white" :size="16" /></span>
            Delete
          </button>
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
            <mdicon name="window-close" class="text-white" :size="18" />
            Cancel
          </button>
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
import { ref, onMounted, reactive } from 'vue'
import axiosClient from '@/js/axios.js'
import { useRouter } from 'vue-router'
import { Modal } from 'bootstrap'

// data
const backend_url_base = 'http://localhost:5000/images/products/'
const categories = ref([])
const products = ref([])
const errordata = reactive({
  isError: false,
  msg: ''
})
let modal
let modalDelete
const loading = ref(false)
const units = ['piece', 'kg', 'litre', 'dozen']
const data = reactive({
  id: 0,
  name: '',
  description: '',
  unit: '',
  price: 0,
  stock: 0,
  expiry_date: '',
  image_name: null,
  image: null,
  created_timestamp: '',
  updated_timestamp: '',
  categories: []
})
const category_id = ref(1)
const edit = ref(false)

// Main Functions
onMounted(async() => {
  loading.value = true
  refreshCategories()
  refreshProducts()
  // setTimeout(() => {
  //   loading.value = false
  // }, 5000)
  loading.value = false

  modal = new Modal(document.getElementById('modalProduct'), {
    keyboard: false
  })

  modalDelete = new Modal(document.getElementById('modalProductDelete'), {
    keyboard: false
  })
})

async function refreshProducts() {
  console.log('refreshing products')
  axiosClient
    .get('/api/product')
    .then((res) => {
      console.log(res)
      products.value = res.data
    })
    .catch((err) => {
      console.log('Error: ', err)
    })
}

async function refreshCategories() {
  console.log('refreshing categories')
  axiosClient
    .get('/api/category')
    .then((res) => {
      console.log(res)
      categories.value = res.data
    })
    .catch((err) => {
      console.log('Error: ', err)
    })
}

const router = useRouter()
const gotoCategories = () => {
  console.log('goto categories')
  router.push('/category')
  // window.location.href = '/#/categories'
}

function handleProductAdd(product, isEdit) {
  console.log('Add/Edit Product:', product)

  if (isEdit) {
    data.id = product.id
    data.name = product.name
    data.description = product.description
    data.unit = product.unit
    data.price = product.price
    data.stock = product.stock
    const date = new Date(product.expiry_date)
    // data.expiry_date = `${date.getFullYear()}-${date.getMonth()}-${date.getDay()}`
    data.expiry_date = date.toISOString().split('T')[0]
    // console.log(data.expiry_date)
    data.image_name = null
    data.image = null
    data.created_timestamp = product.created_timestamp
    data.updated_timestamp = product.updated_timestamp
    for (const category of categories.value) {
      data.categories.push(category)
    }
  } else {
    data.id = 0
    data.name = ''
    data.description = ''
    data.unit = ''
    data.price = 0
    data.stock = 0
    data.expiry_date = ''
    data.image_name = null
    data.image = null
    data.created_timestamp = ''
    data.updated_timestamp = ''
    data.categories = []
    for (const category of categories.value) {
      data.categories.push(category)
    }

    //set date input field to today
    // console.log('set exp. date', data.expiry_date.getDate())
    document.getElementById('productExpiryDate').valueAsDate = new Date()
  }
  edit.value = isEdit

  modal.show()
}

const handleProductDelete = async (product) => {
  console.log('Delete Product:', product.id)
  data.id = product.id
  category_id.value = product.category_id
  modalDelete.show()
}

function handleProductDetails(id) {
  console.log(id)
}

// Modal Functions
const handleImage = (e) => {
  console.log('modal: handle Image')
  // console.log(e)
  if (e.target.files.length === 0) {
    data.image_name = null
    data.image = null
   return
}

  data.image = e.target.files[0]
  data.image_name = data.image.name
  createBase64Image(data.image)
}

function createBase64Image(fObj) {
  const reader = new FileReader()
  reader.onload = (e) => {
    data.image = e.target.result.split(',')[1]
  }
  reader.readAsDataURL(fObj)
}

async function handleProductModalEdit(edit) {
  // console.log('modal: isEdit :', edit)
  // console.log('modal:add/edit data:', data)

  if (data.name === '') {
    errordata.isError = true
    errordata.msg = 'Product name cannot be empty'
    return
  }

  const formData = new FormData()
  formData.append('name', data.name)
  formData.append('description', data.description)
  formData.append('unit', data.unit)
  formData.append('price', data.price)
  formData.append('stock', data.stock)
  const expiry_date = data.expiry_date + ' 00:00'
  formData.append('expiry_date', expiry_date)
  if (data.image_name !== null)
    formData.append('image_name', data.image_name)
  if (data.image !== null)
    formData.append('image', data.image)

  loading.value = true
  let resp = {}
  try {
    if (edit) resp = await axiosClient.put(`/api/product/${category_id.value}/${data.id}`, formData)
    else resp = await axiosClient.post(`/api/product/${category_id.value}`, formData)

    console.log(resp)
    console.log('modal: closing modal')
    document.getElementById('productModalClose').click()
    modal.hide()
    loading.value = true
    refreshProducts()
    loading.value = false
  } catch (err) {
    console.log(err)
    errordata.isError = true
    errordata.msg = err.response.data.message
  } finally {
    loading.value = false
    errordata.isError = false
    errordata.msg = ''
  }
}

async function handleProductModalDelete() {
  console.log('modal:Delete Product')

  loading.value = true
  try {
    const resp = await axiosClient.delete(`/api/product/${category_id.value}/${data.id}`)
    console.log(resp)
    console.log('modal: closing modal')
    document.getElementById('productModalClose').click()
    modal.hide()
    refreshProducts()
  } catch (err) {
    console.log(err)
    errordata.isError = true
    errordata.msg = err.response.data.message
  } finally {
    loading.value = false
    errordata.isError = false
    errordata.msg = ''
  }

  modalDelete.hide()
  refreshProducts()
  // force updated
  // const instance = getCurrentInstance();
  // return () => instance.proxy.$forceUpdate();
}
</script>

<style scoped></style>
