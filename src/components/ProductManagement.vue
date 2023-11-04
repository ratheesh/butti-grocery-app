<template>
  <div class="row col-6 m-auto">
    <h2 class="text-center mt-5">Product Management</h2>
    <div class="card">
      <div class="row justify-content-end">
        <div class="col-auto">
          <button class="btn btn-sm btn-success" @click="handleProductAdd({}, false)">
            <b><mdicon name="plus" class="text-white" :size="18" /></b>
            Add
          </button>
        </div>
      </div>
      <div v-if="products.length > 0">
        <div class="row justify-content-center m-auto">
          <div class="col-8">
            <hr />
            <table class="table table-hover text-center">
              <thead>
                <tr>
                  <th scope="col"><b>ID</b></th>
                  <th scope="col"><b>ID</b></th>
                  <th scope="col"><b>Name</b></th>
                  <th scope="col"></th>
                  <th scope="col"></th>
                  <th scope="col"></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(product, idx) in products" :id="idx" :key="idx">
                  <th></th>
                  <th>{{ product.id }}</th>
                  <th>{{ product.name }}</th>
                  <th>
                    <button class="btn btn-sm btn-secondary" @click="handleProductDetails(product)">
                      <mdicon name="cog" class="text-white" :size="16" />
                      Details
                    </button>
                  </th>
                  <th>
                    <button class="btn btn-sm btn-primary" @click="handleProductAdd(product, true)">
                      <mdicon name="pencil" class="text-white" :size="16" />
                      Edit
                    </button>
                  </th>
                  <th>
                    <button class="btn btn-sm btn-danger" @click="handleProductDelete(product.id)">
                      <mdicon name="delete" class="text-white" :size="16" />
                      Delete
                    </button>
                  </th>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div v-else>
        <h2 class="text-center mt-5">No Products. Add one!</h2>
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
            <select class="form-select" id="productUnit" aria-label="Unit" v-model="data.unit">
              <option value="piece">Piece</option>
              <option value="kg">Kg</option>
              <option value="500gm">500gm</option>
              <option value="litre">Litre</option>
              <option value="dozen">Dozen</option>
            </select>
            <label for="productUnit">Unit</label>
          </div>
          <pre>{{ data.unit }}</pre>
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
              @change="handleImage"
            />
          </div>
        </div>
        <div class="modal-footer text-center">
          <button
            v-if="edit"
            @click="handleProductModalEdit(true)"
            type="button"
            class="btn btn-sm btn-success"
          >
            <span v-if="loading" class="spinner-border spinner-border-sm"></span>
            <mdicon name="pencil" class="text-white" :size="16" />
            Update
          </button>
          <button
            v-else
            @click="handleProductModalEdit(false)"
            type="button"
            class="btn btn-sm btn-success"
          >
            <span v-if="loading" class="spinner-border spinner-border-sm"></span>
            <b><mdicon name="plus" class="text-white" :size="18" /></b>
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
            <mdicon name="delete" class="text-white" :size="16" />
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
import { Modal } from 'bootstrap'

// data
const categories = ref([])
const products = ref([])
const errordata = reactive({
  isError: false,
  msg: ''
})
let modal
let modalDelete
let loading = ref(false)
const data = reactive({
  id: 0,
  name: '',
  description: '',
  unit: '',
  price: 0,
  stock: 0,
  expiry_date: '',
  image: '',
  created_timestamp: '',
  updated_timestamp: '',
  categories: []
})
const category_id = ref(1)
const edit = ref(false)

// Main Functions
onMounted(async () => {
  refreshCategories()
  refreshProducts()

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
    console.log(data.expiry_date)
    data.image = product.image
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
    data.image = ''
    data.image_file = ''
    data.created_timestamp = ''
    data.updated_timestamp = ''
    data.categories = []
    for (const category of categories.value) {
      data.categories.push(category)
    }
  }
  edit.value = isEdit

  modal.show()
}

const handleProductDelete = async (id) => {
  console.log('Delete Product:', id)
  data.id = id
  modalDelete.show()
}

function handleProductDetails(id) {
  console.log(id)
}

// Modal Functions
const handleImage = (e) => {
  console.log('modal: handle Image')
  data.file = e.target.files[0]
  data.image = data.file.name
  createBase64Image(data.file)
}

function createBase64Image(fObj) {
  const reader = new FileReader()
  reader.onload = (e) => {
    data.file = e.target.result.split(',')[1]
  }
  reader.readAsDataURL(fObj)
}

async function handleProductModalEdit(edit) {
  console.log('modal: isEdit :', edit)

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
  formData.append('image', data.image)
  formData.append('image_file', data.image_file)

  loading.value = true
  let resp = {}
  try {
    if (edit) resp = await axiosClient.put(`/api/product/${category_id.value}/${data.id}`, formData)
    else resp = await axiosClient.post(`/api/product/${category_id.value}`, formData)

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
}

async function handleProductModalDelete() {
  console.log('modal:Delete Product')

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
