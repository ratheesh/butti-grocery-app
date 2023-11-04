<template>
  <div class="row col-6 m-auto ">
    <h2 class="text-center mt-5">Category Management</h2> 
  <div class="card">
    <div v-if="categories.length > 0">
    <div class="row justify-content-center m-auto">
      <div class="col-8">
        <hr/>
          <div class="row justify-content-end">
            <div class="col-auto">
              <button class="btn btn-sm btn-success" @click="handleCategoryAdd({}, false)">
                <b><mdicon name="plus" class="text-white" :size="18"/></b>
                Add
              </button>
            </div>
          </div>
        <table class="table table-hover text-center">
          <thead>
            <tr>
              <th scope="col"><b>ID</b></th>
              <th scope="col"><b>Name</b></th>
              <th scope="col"></th>
              <th scope="col"></th>
              <th scope="col"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for='(category, idx) in categories' :id="idx" :key="category.id">
            <th>{{ category.id }}</th>
            <th>{{ category.name }}</th>
            <th>
              <button class="btn btn-sm btn-secondary" @click="count++">
              <mdicon name="cog" class="text-white" :size="16"/>
              Manage
              </button>
            </th>
            <th>
              <button class="btn btn-sm btn-primary" @click="handleCategoryAdd(category, true)">
              <mdicon name="pencil" class="text-white" :size="16"/>
              Edit
              </button>
            </th>
            <th>
              <button class="btn btn-sm btn-danger" @click="handleCategoryDelete(category.id)">
              <mdicon name="delete" class="text-white" :size="16"/>
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
  <div class="modal fade" id="modalCategory" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="staticBackdropLabel">Add Category</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="form-floating mb-3">
            <input type="text" class="form-control" id="floatingInput" placeholder="Fruits/Vegetables" v-model="data.name" required>
            <label for="floatingInput">Category</label>
          </div> 
          <pre>{{ data }}</pre>
        </div>
        <div class="modal-footer text-center">
          <button v-if="edit" @click="handleCategoryModalEdit(true)" type="button" class="btn btn-sm btn-success">
            <span v-if="loading" class="spinner-border spinner-border-sm"></span>
            <mdicon name="pencil" class="text-white" :size="16"/>
            Update
          </button>
          <button v-else @click="handleCategoryModalEdit(false)" type="button" class="btn btn-sm btn-success">
            <span v-if="loading" class="spinner-border spinner-border-sm"></span>
            <b><mdicon name="plus" class="text-white" :size="18"/></b>
            Add
          </button>
          <button type="button" class="btn btn-sm btn-danger" id="categoryModalClose" data-bs-dismiss="modal">
          <mdicon name="window-close" class="text-white" :size="18"/>
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

  <div class="modal fade" id="modalCategoryDelete" role="dialog" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>Modal body text goes here.</p>
        <p>{{ data.id }}</p>
      </div>
      <div class="modal-footer">
        <button @click="handleCategoryModalDelete" type="button" class="btn btn-danger">
          <span v-if="loading" class="spinner-border spinner-border-sm"></span>
          <mdicon name="delete" class="text-white" :size="16"/>
          Delete
        </button>
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
          <mdicon name="window-close" class="text-white" :size="18"/>
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

const categories = ref([]);
const errordata = reactive({
  isError: false,
  msg: ""
})

let modal;
let modalDelete;
onMounted(async() => {
  try {
    const res = await axiosClient.get("/api/category");
    console.log(res)
    categories.value = res.data
  } catch (error) {
    console.log('Error: ', error);
  }

  modal = new Modal(document.getElementById('modalCategory'), {
    keyboard: false
  })

  modalDelete = new Modal(document.getElementById('modalCategoryDelete'), {
    keyboard: false
  })
})

let loading = ref(false);
const data = reactive({
  id  : 0,
  name: "",
});

const edit = ref(false)

// Main Functions
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

const handleCategoryDelete = async(id) => {
  console.log('Delete Category:', id)
  data.id = id
  modalDelete.show()
}

// Modal Functions
async function handleCategoryModalEdit(edit) {
  console.log('modal: isEdit :', edit)

  const formData = new FormData();
  formData.append("name", data.name);

  loading.value = true;
  let resp = {}
  try {
    if (edit)
      resp = await axiosClient.put("/api/category", formData);
    else
      resp = await axiosClient.post("/api/category", formData);

    console.log(resp);
    console.log('modal: closing modal')
    document.getElementById("categoryModalClose").click()
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

  modal.hide()
}

function handleCategoryModalDelete() {
  console.log('modal:Delete Category')

  modalDelete.hide()
}

</script>

<style scoped></style>