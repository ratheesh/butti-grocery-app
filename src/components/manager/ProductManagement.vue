<template>
  <div class="row col-10 justify-content-center m-auto">
    <div class="card shadow-sm mt-4 p-0">
      <div class="card-header m-0 p-0">
        <div class="row col-10 d-flex justify-content-between align-items-center m-auto my-2">
          <div class="col-auto">
            <span class="text-center fs-6 fw-bold mt-3">Product Management</span>
          </div>
          <div class="col-6 d-inline-flex justify-content-end m-auto me-0">
            <div class="col-auto mx-2">
              <button
                class="btn btn-sm btn-secondary mx-2"
                v-show="categories.length > 0"
                @click="refresh"
              >
                <mdicon name="refresh" class="text-dark" :size="18" />
                Refresh
              </button>
              <button
                class="btn btn-sm btn-success"
                v-show="categories.length > 0"
                @click="handleProductAdd({}, false)"
              >
                <b><mdicon name="shape-square-rounded-plus" class="text-white" :size="18" /></b>
                Add
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="card-body">
        <div v-if="main_loading">
          <loading-indicator></loading-indicator>
        </div>
        <div v-else>
          <div v-if="products.length > 0">
            <div class="row justify-content-center mt-3 m-auto">
              <div class="m-0 p-0">
                <!-- <hr /> -->
                <div class="table-responsive">
                  <table class="table table-centered table-nowrap rounded">
                    <thead class="border-bottom table-light">
                      <tr>
                        <th scope="col"><b>#</b></th>
                        <th scope="col"><b>NAME</b></th>
                        <th scope="col"><b>UNIT PRICE</b></th>
                        <th scope="col"><b>TOTAL STOCK</b></th>
                        <th scope="col"><b>STOCK AVAILABLE</b></th>
                        <th scope="col"><b>EXPIRY DATE</b></th>
                        <th scope="col"><b>ACTIONS</b></th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr
                        v-for="(product, idx) in products"
                        :id="idx"
                        :key="idx"
                        class="align-middle"
                      >
                        <td>{{ product.id }}</td>
                        <td>
                          <div class="d-flex align-items-center">
                            <img
                              class="mx-2"
                              :src="`data:image/png;base64,${product.image}`"
                              height="60"
                              width="60"
                            />
                            <span class="d-inline-block align-items-center">
                              <span>{{ product.name }}</span>
                              <br />
                              <small>{{ product.category_name }}</small>
                            </span>
                          </div>
                        </td>
                        <td><b>₹</b>{{ product.price }}/{{ product.unit }}</td>
                        <td>
                          {{ product.stock }}
                        </td>
                        <td>
                          {{ product.stock_available }}
                        </td>
                        <td>
                          {{ formatDate(product.expiry_date) }}
                        </td>
                        <td>
                          <button
                            class="btn btn-link dropdown-toggle px-0"
                            data-bs-toggle="dropdown"
                            aria-expanded="false"
                          >
                            <mdicon
                              name="dots-horizontal"
                              :width="24"
                              :height="24"
                              aria-expanded="false"
                            />
                          </button>
                          <ul class="dropdown-menu">
                            <li>
                              <a
                                class="dropdown-item"
                                href="javascript:void(0)"
                                @click="handleViewDescription(product)"
                              >
                                <mdicon name="eye" class="text-gray" :size="20" />
                                Description
                              </a>
                            </li>
                            <li>
                              <a
                                class="dropdown-item"
                                href="javascript:void(0)"
                                @click="handleProductAdd(product, true)"
                              >
                                <svg
                                  width="20"
                                  height="20"
                                  viewBox="0 0 24 24"
                                  fill="text-gray"
                                  xmlns="http://www.w3.org/2000/svg"
                                >
                                  <path
                                    fill-rule="evenodd"
                                    clip-rule="evenodd"
                                    d="M21.1213 2.70705C19.9497 1.53548 18.0503 1.53547 16.8787 2.70705L15.1989 4.38685L7.29289 12.2928C7.16473 12.421 7.07382 12.5816 7.02986 12.7574L6.02986 16.7574C5.94466 17.0982 6.04451 17.4587 6.29289 17.707C6.54127 17.9554 6.90176 18.0553 7.24254 17.9701L11.2425 16.9701C11.4184 16.9261 11.5789 16.8352 11.7071 16.707L19.5556 8.85857L21.2929 7.12126C22.4645 5.94969 22.4645 4.05019 21.2929 2.87862L21.1213 2.70705ZM18.2929 4.12126C18.6834 3.73074 19.3166 3.73074 19.7071 4.12126L19.8787 4.29283C20.2692 4.68336 20.2692 5.31653 19.8787 5.70705L18.8622 6.72357L17.3068 5.10738L18.2929 4.12126ZM15.8923 6.52185L17.4477 8.13804L10.4888 15.097L8.37437 15.6256L8.90296 13.5112L15.8923 6.52185ZM4 7.99994C4 7.44766 4.44772 6.99994 5 6.99994H10C10.5523 6.99994 11 6.55223 11 5.99994C11 5.44766 10.5523 4.99994 10 4.99994H5C3.34315 4.99994 2 6.34309 2 7.99994V18.9999C2 20.6568 3.34315 21.9999 5 21.9999H16C17.6569 21.9999 19 20.6568 19 18.9999V13.9999C19 13.4477 18.5523 12.9999 18 12.9999C17.4477 12.9999 17 13.4477 17 13.9999V18.9999C17 19.5522 16.5523 19.9999 16 19.9999H5C4.44772 19.9999 4 19.5522 4 18.9999V7.99994Z"
                                    fill="#000"
                                  />
                                </svg>
                                Edit
                              </a>
                            </li>
                          </ul>
                          <button
                            class="btn btn-link text-decoration-none px-0"
                            aria-expanded="false"
                          >
                            <mdicon
                              name="close-circle"
                              class="text-danger"
                              :size="20"
                              @click="handleProductDelete(product)"
                            />
                          </button>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
          <div v-else>
            <div v-if="categories.length === 0" class="row col-12">
              <p class="text-center mt-1">
                No Categories. Atleast one category should be added before adding a product
              </p>
              <p class="text-center mt-1">Click <b>here</b> go to category page and add one!</p>
            </div>
            <div v-else class="row col-12">
              <h4 class="text-center mt-1">No Products. Add one!</h4>
            </div>
          </div>
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
        <form
          @submit.prevent="handleProductModalEdit"
          needs-validation
          novalidate
          :class="{ 'was-validated': wasValidated }"
        >
          <div class="modal-body">
            <div class="form-floating mb-3">
              <input
                type="text"
                class="form-control"
                :class="{ 'form-control': true, 'is-invalid': errors.name }"
                id="productName"
                placeholder="apple/bananas"
                v-model="data.name"
                required
              />
              <label for="productName">Name</label>
              <div class="invalid-feedback">
                <span>Name should be given</span>
              </div>
            </div>
            <div class="form-floating mb-3">
              <textarea
                type="text"
                class="form-control"
                :class="{ 'form-control': true, 'is-invalid': errors.description }"
                id="productDescription"
                placeholder="Description"
                v-model="data.description"
                required
              ></textarea>
              <label for="productDescription">Description</label>
              <div class="invalid-feedback">
                <span>Description should be present</span>
              </div>
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
              <select
                class="form-select"
                id="productUnit"
                aria-label="Unit"
                required
                v-model="data.unit"
              >
                <option v-for="(unit, idx) in units" :key="idx" :value="unit">{{ unit }}</option>
              </select>
              <label for="productUnit">Unit</label>
            </div>
            <div class="form-floating mb-3">
              <input
                type="number"
                class="form-control"
                :class="{ 'form-control': true, 'is-invalid': errors.price }"
                id="productPrice"
                placeholder="Price"
                v-model="data.price"
                required
              />
              <label for="productPrice">Price</label>
              <div class="invalid-feedback">
                <span>Price can not be zero</span>
              </div>
            </div>
            <div class="form-floating mb-3">
              <input
                type="number"
                class="form-control"
                :class="{ 'form-control': true, 'is-invalid': errors.stock }"
                id="productStock"
                placeholder="Stock"
                v-model="data.stock"
                required
              />
              <label for="productStock">Stock(> {{ data.stock_sold }})</label>
              <div class="invalid-feedback">
                <span>Stock size is invalid. must be > {{ data.stock_sold }}</span>
              </div>
            </div>
            <div class="form-group mb-3">
              <label for="productExpireyDate">Expiry Date</label>
              <div class="input-group">
                <span class="input-group-text" id="expiry_date">
                  <mdicon name="calendar-today" :size="20" />
                </span>
                <input
                  type="date"
                  class="form-control rounded-end"
                  :class="{ 'form-control': true, 'is-invalid': errors.expiry_date }"
                  id="productExpiryDate"
                  placeholder="Expiry Date"
                  v-model="data.expiry_date"
                  required
                />
                <div class="invalid-feedback">
                  <span>Expiry Date can not be in past tense</span>
                </div>
              </div>
            </div>
            <div class="mb-0">
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
            <button v-if="edit" type="submit" class="btn btn-sm btn-warning">
              <span v-if="loading" class="spinner-border spinner-border-sm"></span>
              <span v-else>
                <!-- <mdicon name="pencil" class="text-white" :size="16" /> -->
                <svg
                  width="16px"
                  height="16px"
                  viewBox="0 0 24 24"
                  fill="#fff"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M21.1213 2.70705C19.9497 1.53548 18.0503 1.53547 16.8787 2.70705L15.1989 4.38685L7.29289 12.2928C7.16473 12.421 7.07382 12.5816 7.02986 12.7574L6.02986 16.7574C5.94466 17.0982 6.04451 17.4587 6.29289 17.707C6.54127 17.9554 6.90176 18.0553 7.24254 17.9701L11.2425 16.9701C11.4184 16.9261 11.5789 16.8352 11.7071 16.707L19.5556 8.85857L21.2929 7.12126C22.4645 5.94969 22.4645 4.05019 21.2929 2.87862L21.1213 2.70705ZM18.2929 4.12126C18.6834 3.73074 19.3166 3.73074 19.7071 4.12126L19.8787 4.29283C20.2692 4.68336 20.2692 5.31653 19.8787 5.70705L18.8622 6.72357L17.3068 5.10738L18.2929 4.12126ZM15.8923 6.52185L17.4477 8.13804L10.4888 15.097L8.37437 15.6256L8.90296 13.5112L15.8923 6.52185ZM4 7.99994C4 7.44766 4.44772 6.99994 5 6.99994H10C10.5523 6.99994 11 6.55223 11 5.99994C11 5.44766 10.5523 4.99994 10 4.99994H5C3.34315 4.99994 2 6.34309 2 7.99994V18.9999C2 20.6568 3.34315 21.9999 5 21.9999H16C17.6569 21.9999 19 20.6568 19 18.9999V13.9999C19 13.4477 18.5523 12.9999 18 12.9999C17.4477 12.9999 17 13.4477 17 13.9999V18.9999C17 19.5522 16.5523 19.9999 16 19.9999H5C4.44772 19.9999 4 19.5522 4 18.9999V7.99994Z"
                    fill="#000"
                  />
                </svg>
              </span>
              Update
            </button>
            <button v-else type="submit" class="btn btn-sm btn-success">
              <span v-if="loading" class="spinner-border spinner-border-sm"></span>
              <span v-else
                ><b><mdicon name="shape-square-rounded-plus" class="text-white" :size="18" /></b
              ></span>
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
        </form>
      </div>
    </div>
  </div>

  <!-- Description Modal -->
  <div class="modal fade" id="modalProductDescription" role="dialog" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title text-center">{{ data.name }}</h5>
        </div>
        <div class="modal-body">
          <p>{{ data.description }}</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-danger" data-bs-dismiss="modal">
            <mdicon name="window-close" class="text-white" :size="18" />
            Close
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Delete Modal -->
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
import { Modal } from 'bootstrap'
import LoadingIndicator from '@/components/LoadingIndicator.vue'

// data
const categories = ref([])
const products = ref([])
const errordata = reactive({
  isError: false,
  msg: ''
})
const errors = reactive({
  name: false,
  description: false,
  price: false,
  stock: false,
  expiry_date: false
})
const wasValidated = ref(false)

let modal
let modalDescription
let modalDelete

const main_loading = ref(true)
const loading = ref(false)
const units = ['piece', 'kg', 'litre', 'dozen']
const data = reactive({
  id: 0,
  name: '',
  description: '',
  unit: '',
  price: 0,
  stock: 0,
  stock_sold: 0,
  expiry_date: '',
  image_name: null,
  image: null,
  created_timestamp: '',
  updated_timestamp: '',
  categories: []
})
const category_id = ref(1)
const edit = ref(false)

// main function
async function refreshData() {
  console.log('Refreshing data...')
  main_loading.value = true
  try {
    await refreshCategories()
    await refreshProducts()
  } catch (err) {
    console.log(err)
  } finally {
    main_loading.value = false
  }
}

const refresh = async () => {
  await refreshData()
}

onMounted(async () => {
  modal = new Modal(document.getElementById('modalProduct'), {
    keyboard: false
  })

  modalDescription = new Modal(document.getElementById('modalProductDescription'), {
    keyboard: false
  })

  modalDelete = new Modal(document.getElementById('modalProductDelete'), {
    keyboard: false
  })
})

function formatDate(timestamp) {
  const date = new Date(timestamp)
  const options = {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  }
  return date.toLocaleDateString('en-IN', options)
}

async function refreshProducts() {
  console.log('refreshing products')
  try {
    const resp = await axiosClient.get('/api/product')
    products.value = resp.data
  } catch (err) {
    console.log('Error: ', err)
  }
}

async function refreshCategories() {
  console.log('refreshing categories')
  try {
    const resp = await axiosClient.get('/api/category')
    categories.value = resp.data
    categories.value = categories.value.filter((category) => category.approved == true)
  } catch (err) {
    console.log('Error: ', err)
  }
}

function handleProductAdd(product, isEdit) {
  if (isEdit) {
    data.id = product.id
    data.name = product.name
    data.description = product.description
    data.unit = product.unit
    data.price = product.price
    data.stock = product.stock
    data.stock_sold = product.stock_sold
    const date = new Date(product.expiry_date)
    // data.expiry_date = `${date.getFullYear()}-${date.getMonth()}-${date.getDay()}`
    data.expiry_date = date.toISOString().split('T')[0]
    // console.log(data.expiry_date)
    data.image_name = product.image_name
    data.image = product.image
    data.created_timestamp = product.created_timestamp
    data.updated_timestamp = product.updated_timestamp
    for (const category of categories.value) {
      data.categories.push(category)
    }
    category_id.value=product.category_id
  } else {
    data.id = 0
    data.name = ''
    data.description = ''
    data.unit = 'piece'
    data.price = 0
    data.stock = 0
    data.expiry_date = new Date().toISOString().split('T')[0]
    data.image_name = null
    data.image = null
    data.created_timestamp = ''
    data.updated_timestamp = ''
    data.categories = []
    for (const category of categories.value) {
      data.categories.push(category)
    }
  }
  edit.value = isEdit
  document.getElementById('productImage').value = ''

  errordata.isError = false
  errordata.msg = ''
  errors.name = false
  errors.description = false
  errors.price = false
  errors.stock = false
  errors.expiry_date = false
  wasValidated.value = false

  modal.show()
}

const handleViewDescription = (product) => {
  console.log('View Product Description')
  data.name = product.name
  data.description = product.description
  modalDescription.show()
}

const handleProductDelete = async (product) => {
  console.log('Delete Product:', product.id)
  data.id = product.id
  category_id.value = product.category_id
  modalDelete.show()
}

// Modal Functions
const handleImage = (e) => {
  console.log('modal: handle Image')
  // console.log(e)
  if (e.target.files.length === 0) {
    console.log('cancel file selection')
    data.image_name = null
    data.image = null
    return
  }

  data.image = e.target.files[0]
  data.image_name = data.image.name
  console.log(data.image)
  createBase64Image(data.image)
}

function createBase64Image(fObj) {
  const reader = new FileReader()
  reader.onload = (e) => {
    data.image = e.target.result.split(',')[1]
  }
  reader.readAsDataURL(fObj)
}

async function handleProductModalEdit() {
  console.log('handleProductModalEdit')
  wasValidated.value = false
  errordata.isError = false
  errordata.msg = ''
  errors.name = false
  errors.description = false
  errors.price = false
  errors.stock = false
  errors.expiry_date = false

  if (!data.name || !data.description || !data.price || !data.stock || !data.expiry_date) {
    errordata.isError = true
    errordata.msg = 'All fields are required'
    errors.name = !data.name
    errors.description = !data.description
    errors.price = !data.price
    errors.stock = !data.stock
    errors.expiry_date = !data.expiry_date
    return
  }

  if (data.price <= 0 || data.price > 10000) {
    errors.price = true
    return
  }

  if (data.stock <= data.stock_sold || data.stock > 10000) {
    errors.stock = true
    return
  }

  if (data.expiry_date < new Date().toISOString().split('T')[0]) {
    errors.expiry_date = true
    return
  }

  wasValidated.value = true

  const formData = new FormData()
  formData.append('name', data.name)
  formData.append('description', data.description)
  formData.append('unit', data.unit)
  formData.append('price', data.price)
  formData.append('stock', data.stock)
  const expiry_date = data.expiry_date + ' 18:29'
  formData.append('expiry_date', expiry_date)
  if (data.image_name !== null) formData.append('image_name', data.image_name)
  if (data.image !== null) formData.append('image', data.image)

  loading.value = true
  let resp = {}
  try {
    if (edit.value)
      resp = await axiosClient.put(`/api/product/${category_id.value}/${data.id}`, formData)
    else resp = await axiosClient.post(`/api/product/${category_id.value}`, formData)

    console.log(resp)
    console.log('modal: closing modal')
    document.getElementById('productModalClose').click()
    modal.hide()
    refreshData()
  } catch (err) {
    console.log(err)
    errordata.isError = true
    errordata.msg = err.response.data
    errors.name = errordata.msg.includes('name')
    errors.description = errordata.msg.includes('description')
    errors.price = errordata.msg.includes('price')
    errors.stock = errordata.msg.includes('stock')
    errors.expiry_date = errordata.msg.includes('expiry_date')
  } finally {
    wasValidated.value = false
    loading.value = false
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
    refreshData()
  } catch (err) {
    console.log(err)
    errordata.isError = true
    errordata.msg = err.response.data
  } finally {
    loading.value = false
    errordata.isError = false
    errordata.msg = ''
  }

  modalDelete.hide()

  await refreshData()
}

await refreshData()
</script>

<style scoped>
th {
  vertical-align: middle;
  border-bottom: 3px solid #485460;
  font-size: 12px, bold;
}
.dropdown-toggle::after {
  content: none;
}
</style>
