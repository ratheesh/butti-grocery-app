<template>
  <div class="row col-8 m-auto ">
    <h2 class="text-center mt-3">Category Management</h2>
    <div class="card">
      <div class="row col-10 justify-content-end m-auto my-3">
        <div class="col-auto">
          <button class="btn btn-sm btn-success" @click="handleCategoryAdd({}, false)">
            <b>
              <mdicon name="shape-square-rounded-plus" class="text-white" :size="18" />
            </b>
            Add
          </button>
        </div>
      </div>
      <div v-if="categories.length > 0">
        <div class="row justify-content-center m-auto">
          <div class="col-10">
            <table class="table table-hover text-center">
              <thead class="table-dark">
                <tr>
                  <th scope="col"><b>ID</b></th>
                  <th scope="col"><b>NAME</b></th>
                  <th scope="col"></th>
                  <th scope="col"></th>
                  <th scope="col"></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for='(category, idx) in categories' :id="idx" :key="idx">
                  <th>{{ category.id }}</th>
                  <th>{{ category.name }}</th>
                  <th>
                    <button class="btn btn-sm btn-secondary" @click="count++">
                      <mdicon name="cog" class="text-white" :size="16" />
                      Manage
                    </button>
                  </th>
                  <th>
                    <button class="btn btn-sm btn-warning" @click="handleCategoryAdd(category, true)">
                      <!-- <mdicon name="pencil" class="text-white" :size="16" /> -->
                      <svg width="18px" height="18px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M21.1213 2.70705C19.9497 1.53548 18.0503 1.53547 16.8787 2.70705L15.1989 4.38685L7.29289 12.2928C7.16473 12.421 7.07382 12.5816 7.02986 12.7574L6.02986 16.7574C5.94466 17.0982 6.04451 17.4587 6.29289 17.707C6.54127 17.9554 6.90176 18.0553 7.24254 17.9701L11.2425 16.9701C11.4184 16.9261 11.5789 16.8352 11.7071 16.707L19.5556 8.85857L21.2929 7.12126C22.4645 5.94969 22.4645 4.05019 21.2929 2.87862L21.1213 2.70705ZM18.2929 4.12126C18.6834 3.73074 19.3166 3.73074 19.7071 4.12126L19.8787 4.29283C20.2692 4.68336 20.2692 5.31653 19.8787 5.70705L18.8622 6.72357L17.3068 5.10738L18.2929 4.12126ZM15.8923 6.52185L17.4477 8.13804L10.4888 15.097L8.37437 15.6256L8.90296 13.5112L15.8923 6.52185ZM4 7.99994C4 7.44766 4.44772 6.99994 5 6.99994H10C10.5523 6.99994 11 6.55223 11 5.99994C11 5.44766 10.5523 4.99994 10 4.99994H5C3.34315 4.99994 2 6.34309 2 7.99994V18.9999C2 20.6568 3.34315 21.9999 5 21.9999H16C17.6569 21.9999 19 20.6568 19 18.9999V13.9999C19 13.4477 18.5523 12.9999 18 12.9999C17.4477 12.9999 17 13.4477 17 13.9999V18.9999C17 19.5522 16.5523 19.9999 16 19.9999H5C4.44772 19.9999 4 19.5522 4 18.9999V7.99994Z"
                         fill="#000"/>
                      </svg>
                      Edit
                    </button>
                  </th>
                  <th>
                    <button class="btn btn-sm btn-danger" @click="handleCategoryDelete(category.id)">
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
        <h2 class="text-center mt-5 ">No Categories. Add one!</h2>
      </div>
    </div>
  </div>

  <!-- Modal Windows -->

  <!-- Add/Edit Category -->
  <div class="modal fade" id="modalCategory" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
    aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h1 v-if="!edit" class="modal-title fs-5" id="staticBackdropLabel">Add Category</h1>
          <h1 v-else class="modal-title fs-5" id="staticBackdropLabel">Update Category</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="form-floating mb-3">
            <input type="text" class="form-control" id="floatingInput" placeholder="Fruits/Vegetables" v-model="data.name"
              required>
            <label for="floatingInput">Category</label>
          </div>
        </div>
        <div class="modal-footer text-center">
          <button v-if="edit" @click="handleCategoryModalEdit(true)" type="button" class="btn btn-sm btn-success">
            <span v-if="loading" class="spinner-border spinner-border-sm"></span>
            <mdicon name="update" class="text-white" :size="18" />
            Update
          </button>
          <button v-else @click="handleCategoryModalEdit(false)" type="button" class="btn btn-sm btn-success">
            <span v-if="loading" class="spinner-border spinner-border-sm"></span>
            <b>
              <mdicon name="shape-square-rounded-plus" class="text-white" :size="18" />
            </b>
            Add
          </button>
          <button type="button" class="btn btn-sm btn-danger" id="categoryModalClose" data-bs-dismiss="modal">
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

<!-- Delete Category -->
  <div class="modal fade" id="modalCategoryDelete" role="dialog" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Delete Category</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <p>This will delete the category and all the products under this</p>
          <p>This action is irreversible</p>
          <p>Are you sure you want to do this?</p>
        </div>
        <div class="modal-footer">
          <button @click="handleCategoryModalDelete" type="button" class="btn btn-danger">
            <span v-if="loading" class="spinner-border spinner-border-sm"></span>
            <mdicon name="delete" class="text-white" :size="16" />
            Delete
          </button>
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
            <mdicon name="window-close" class="text-white" :size="18" />
            Cancel
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive } from 'vue';
import axiosClient from '@/js/axios.js';
import { Modal } from 'bootstrap';

// data
const categories = ref([]);
const errordata = reactive({
  isError: false,
  msg: ""
})
let modal;
let modalDelete;
let loading = ref(false);
const data = reactive({
  id: 0,
  name: "",
});
const edit = ref(false)

// Main Functions
onMounted(async () => {
  refreshCategories()

  modal = new Modal(document.getElementById('modalCategory'), {
    keyboard: false
  })

  modalDelete = new Modal(document.getElementById('modalCategoryDelete'), {
    keyboard: false
  })
})

async function refreshCategories() {
  console.log('refreshing categories')
  axiosClient.get("/api/category")
    .then((res) => {
      console.log(res)
      categories.value = res.data
    })
    .catch((err) => {
      console.log('Error: ', err);
    })
}

function handleCategoryAdd(category, isEdit) {
  console.log('Add/Edit Category:', category)

  if (isEdit) {
    data.id = category.id
    data.name = category.name
  } else {
    data.id = 0
    data.name = ""
  }
  edit.value = isEdit

  modal.show()
}

const handleCategoryDelete = async (id) => {
  console.log('Delete Category:', id)
  data.id = id
  modalDelete.show()
}

// Modal Functions
async function handleCategoryModalEdit(edit) {
  console.log('modal: isEdit :', edit)

  if (data.name === '') {
    errordata.isError = true;
    errordata.msg = "Category name cannot be empty";
    return;
  }

  const formData = new FormData();
  formData.append("name", data.name);

  loading.value = true;
  let resp = {}
  try {
    if (edit)
      resp = await axiosClient.put(`/api/category/${data.id}`, formData);
    else
      resp = await axiosClient.post("/api/category", formData);

    console.log(resp);
    console.log('modal: closing modal')
    document.getElementById("categoryModalClose").click()
    modal.hide()
    refreshCategories()
    // force update
    // const instance = getCurrentInstance();
    // instance.proxy.$forceUpdate();
  } catch (err) {
    console.log(err);
    errordata.isError = true;
    errordata.msg = err.response.data.message;
  } finally {
    data.name = "";
    data.image = null;
    data.file = null;
    errordata.isError = false;
    loading.value = false;
  }
}

async function handleCategoryModalDelete() {
  console.log('modal:Delete Category')

  try {
    const resp = await axiosClient.delete(`/api/category/${data.id}`);

    console.log(resp);
    console.log('modal: closing modal')
    document.getElementById("categoryModalClose").click()
    modal.hide()
    refreshCategories()
  } catch (err) {
    console.log(err);
    errordata.isError = true;
    errordata.msg = err.response.data.message;
  } finally {
    data.name = "";
    errordata.isError = false;
    errordata.msg = "";
    loading.value = false;
  }

  modalDelete.hide()
  refreshCategories()
  // force updated
  // const instance = getCurrentInstance();
  // return () => instance.proxy.$forceUpdate();
}

</script>

<style scoped></style>