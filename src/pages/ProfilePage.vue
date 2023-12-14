<template>
  <main-layout>
    <div class="container">
      <div v-if="component_loading">
        <loading-indicator></loading-indicator>
      </div>
      <div v-else>
        <div class="text-center mt-3">
          <img
            :src="`data:image/png;base64, ${user.image}`"
            alt="User Profile Image"
            style="width: 150px; height: 150px; border: 1px solid #808080; border-radius: 50%"
          />
        </div>
        <div class="row my-3">
          <div class="col-8 border rounded-2 p-0 m-auto">
            <h2 class="text-center mt-3">{{ user.name }}'s Profile</h2>
            <hr class="m-0" />
            <table class="table table-borderless">
              <tr>
                <td class="text-end fw-bolder">Name</td>
                <td class="mx-3">{{ user.name }}</td>
              </tr>
              <tr>
                <td class="text-end fw-bolder">User Name</td>
                <td>{{ user.username }}</td>
              </tr>
              <tr>
                <td class="text-end fw-bolder">E-Mail</td>
                <td>{{ user.email }}</td>
              </tr>
              <tr>
                <td class="text-end fw-bolder">Role</td>
                <td>{{ user.role }}</td>
              </tr>
              <tr>
                <td class="text-end fw-bolder">Status</td>
                <td>{{ accountStatus(user.approved) }}</td>
              </tr>
              <tr>
                <td class="text-end fw-bolder">Created on</td>
                <td>{{ user.created_timestamp }}</td>
              </tr>
              <tr>
                <td class="text-end fw-bolder">Last updated on</td>
                <td>{{ user.updated_timestamp }}</td>
              </tr>
            </table>
            <hr class="m-0" />
            <div class="text-center my-3">
              <button
                class="btn btn-sm btn-success mx-2 d-inline-flex align-items-center"
                @click="handleEditProfile"
              >
                <b
                  ><mdicon name="shape-square-rounded-plus" class="text-white mx-1" :size="18"
                /></b>
                <span>Edit</span>
              </button>
              <button
                class="btn btn-sm btn-danger mx-2 d-inline-flex align-items-center"
                v-if="user.role !== 'admin'"
                @click="handleDeleteProfile"
              >
                <b><mdicon name="delete" class="text-white mx-1" :size="18" /></b>
                <span>Delete</span>
              </button>
              <button class="btn btn-sm btn-secondary mx-2" @click="router.push('/')">
                <b><mdicon name="home" class="text-black" :size="18" /></b>
                Go Home
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Edit Modal -->
    <div
      class="modal fade"
      id="editProfile"
      data-bs-backdrop="static"
      data-bs-keyboard="false"
      tabindex="-1"
      aria-labelledby="editProfileLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="staticBackdropLabel">Edit {{ user.name }} Profile</h1>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <div class="row justify-content-center m-0 p-0">
              <div class="col-md-10 m-0 p-0">
                <div class="form-group mb-3">
                  <label for="name"
                    >Full Name<span class="text-danger"><b>*</b></span></label
                  >
                  <div class="input-group">
                    <span class="input-group-text" id="user">
                      <mdicon name="form-textbox" :size="20" />
                    </span>
                    <input
                      type="text"
                      :class="{ 'form-control': true, 'is-invalid': errors.name }"
                      placeholder="Kumar"
                      id="name"
                      v-model="user.name"
                      autofocus
                    />
                  </div>
                </div>
                <div class="form-group mb-3">
                  <label for="email"
                    >E-Mail<span class="text-danger"><b>*</b></span></label
                  >
                  <div class="input-group">
                    <span class="input-group-text" id="email">
                      <mdicon name="form-textbox-password" :size="20" />
                    </span>
                    <input
                      type="email"
                      :class="{ 'form-control': true, 'is-invalid': errors.email }"
                      v-model="user.email"
                      id="password"
                      class="form-control"
                      placeholder="user@butti.com"
                      required
                    />
                  </div>
                </div>
                <div class="form-group mb-3">
                  <label for="password"
                    >Password<span class="text-danger"><b>*</b></span></label
                  >
                  <div class="input-group">
                    <span class="input-group-text" id="password">
                      <mdicon name="form-textbox-password" :size="20" />
                    </span>
                    <input
                      type="password"
                      :class="{ 'form-control': true, 'is-invalid': errors.password }"
                      v-model="passwd"
                      id="password"
                      class="form-control"
                      placeholder="Enter Password"
                    />
                  </div>
                </div>
                <div class="form-group mb-3">
                  <label for="password2"
                    >Re-enter Password<span class="text-danger"><b>*</b></span></label
                  >
                  <div class="input-group">
                    <span class="input-group-text" id="password2">
                      <mdicon name="form-textbox-password" :size="20" />
                    </span>
                    <input
                      type="password"
                      :class="{ 'form-control': true, 'is-invalid': errors.password }"
                      v-model="passwd2"
                      id="password2"
                      class="form-control"
                      placeholder="Re-enter Password"
                    />
                  </div>
                </div>
                <div class="form-group mb-3">
                  <label for="profilePhoto">Select Profile Photo</label>
                  <div class="input-group">
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
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-sm btn-warning" @click="handleModalEditProfile">
              <span v-if="loading" class="spinner-border spinner-border-sm"></span>
              <span v-else>
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
            <button
              type="button"
              id="modalEditUserClose"
              class="btn btn-sm btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>
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
    </div>

    <!--  Delete Modal -->
    <div class="modal fade" id="deleteProfile" role="dialog" tabindex="-1">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Delete Profile</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <p>This will delete your account.</p>
            <p>All the account data will be deleted. This action is irreversible</p>
            <p>Are you sure you want to do this?</p>
          </div>
          <div class="modal-footer">
            <button @click="handleModalProfileDelete" type="button" class="btn btn-danger">
              <span v-if="loading" class="spinner-border spinner-border-sm"></span>
              <span v-else><mdicon name="delete" class="text-white" :size="16" /></span>
              Delete
            </button>
            <button
              type="button"
              id="modalDeleteUserClose"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
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
  </main-layout>
</template>

<script setup>
import { onMounted, ref, reactive } from 'vue'
import { useAuthStore } from '@/stores/authstore'
import { Modal } from 'bootstrap'
import router from '@/router'
import axiosClient from '@/js/axios.js'
import MainLayout from '@/layouts/MainLayout.vue'
import LoadingIndicator from '@/components/LoadingIndicator.vue'

const auth = useAuthStore()
const component_loading = ref(true)
const loading = ref(false)
const user = ref({})
const passwd = ref('')
const passwd2 = ref('')
const errors = reactive({
  name: false,
  username: false,
  email: false,
  role: false,
  password: false
})
const errordata = reactive({
  isError: false,
  msg: ''
})
let image_changed = false

let image = null
// let image_name = null
let modal = null
let modalDelete = null

onMounted(async () => {
  if (auth.authenticated === false) {
    console.warn('User not authenticated')
    router.push({ name: 'login' })
  }
})

const fetchUser = async () => {
  if (auth.user) {
    component_loading.value = true
    try {
      const resp = await axiosClient.get(`/api/user/${auth.user.username}`)
      console.log(resp)
      user.value = resp.data
    } catch (err) {
      console.log(err)
    } finally {
      component_loading.value = false
    }
  }
}

const accountStatus = (status) => {
  if (status === true) {
    return 'Approved'
  } else {
    return 'Pending'
  }
}

const handleEditProfile = () => {
  modal = new Modal(document.getElementById('editProfile'))
  modal.show()
}

const handleDeleteProfile = () => {
  modalDelete = new Modal(document.getElementById('deleteProfile'))
  modalDelete.show()
}

// modal functions
const handleImage = (e) => {
  console.log('modal: handle Image')
  // console.log(e)
  if (e.target.files.length === 0) {
    console.log('cancel file selection')
    // image_name = null
    image = null
    image_changed = false
    return
  }

  image = e.target.files[0]
  // image_name = image.name
  console.log(image)
  createBase64Image(image)
}

function createBase64Image(fObj) {
  const reader = new FileReader()
  reader.onload = (e) => {
    image = e.target.result.split(',')[1]
  }
  reader.readAsDataURL(fObj)
  image_changed = true
}
const handleModalEditProfile = async () => {
  // console.log(user.value)
  loading.value = true
  try {
    const formData = new FormData()
    formData.append('name', user.value.name)
    formData.append('username', user.value.username)
    formData.append('email', user.value.email)

    if (passwd.value !== '' && passwd2.value !== '')
      if (passwd.value === passwd2.value) {
        user.value.password = passwd.value
        formData.append('password', user.value.password)
      } else {
        errordata.isError = true
        errordata.msg = 'Passwords do not match'
        return
      }

    formData.append('image_name', user.value.image_name)
    if (image !== null && image_changed) formData.append('image', image)

    // console.log('Form data: ', formData)
    const resp = await axiosClient.put(`/api/user/${user.value.username}`, formData)
    console.log(resp)
    user.value = resp.data
    auth.setUser(user.value)
    document.getElementById('modalEditUserClose').click()
  } catch (err) {
    console.log(err)
  } finally {
    loading.value = false
  }
}

const handleModalProfileDelete = async () => {
  errordata.isError = false
  errordata.msg = ''
  loading.value = true
  try {
    await axiosClient.delete(`/api/user/${auth.user.username}`)
    document.getElementById('modalDeleteUserClose').click()
    auth.logout()
  } catch (err) {
    errordata.isError = true
    errordata.msg = err.response.data
  } finally {
    loading.value = false
  }
}

fetchUser()
</script>

<style scoped>
table {
  table-layout: fixed;
}

td {
  padding: 0.75em;
}
</style>
