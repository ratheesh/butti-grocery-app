<template>
  <div class="row justify-content-center">
    <div class="col-8">
      <div class="card">
        <div class="card-header m-0 p-0">
          <div class="row col-12 d-flex justify-content-between align-items-center m-auto my-2">
            <div class="col-auto">
              <span class="text-center fs-6 fw-bold mt-3">User Management</span>
            </div>
            <div class="col-6 d-inline-flex justify-content-end m-auto me-0">
              <div class="col-auto mx-2">
                <button class="btn btn-sm btn-secondary mx-2" @click="refresh">
                  <mdicon name="refresh" class="text-white" :size="18" />
                  Refresh
                </button>
              </div>
            </div>
          </div>
        </div>
        <div class="card-body shadow-sm">
          <div v-if="main_loading">
            <loading-indicator></loading-indicator>
          </div>
          <div v-else>
            <div v-if="users.length > 0">
              <table class="table table-responsive">
                <thead class="table-light border-bottom table-hover align-items-center">
                  <tr>
                    <th scope="col" class="fw-bold">ID</th>
                    <th scope="col" class="fw-bold">NAME</th>
                    <th scope="col" class="fw-bold">ROLE</th>
                    <th scope="col" class="fw-bold">CREATED ON</th>
                    <th scope="col" class="fw-bold">STATUS</th>
                    <th scope="col" class="fw-bold">ACTION</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="user in users" :key="user.id" class="align-middle">
                    <td>{{ user.id }}</td>
                    <td class="align-items-center">
                      <a class="d-flex align-items-center text-decoration-none">
                        <img
                          :src="`data:image/png;base64,${user.image}`"
                          height="40"
                          width="40"
                          class="avatar rounded-circle me-3"
                          alt="profile"
                        />
                        <div class="d-block">
                          <span class="fw-bold">{{ user.name }}</span>
                          <div class="small text-black">
                            <span>@{{ user.username }}</span>
                          </div>
                          <div class="small text-gray">
                            <span>{{ user.email }}</span>
                          </div>
                        </div>
                      </a>
                    </td>
                    <td>{{ user.role }}</td>
                    <td>{{ formatDate(user.created_timestamp) }}</td>
                    <td v-if="user.approved">
                      <div class="d-flex align-items-center">
                        <mdicon
                          name="check-circle"
                          :width="16"
                          :height="16"
                          class="text-success p-1"
                          data-bs-toggle="dropdown"
                          aria-expanded="false"
                        />
                        Active
                      </div>
                    </td>
                    <td v-else>
                      <div class="d-flex align-items-center">
                        <mdicon
                          name="clock-time-four"
                          :width="16"
                          :height="16"
                          class="text-purple p-1"
                          data-bs-toggle="dropdown"
                          aria-expanded="false"
                        />
                        <span class="text-purple">Pending</span>
                      </div>
                    </td>
                    <td>
                      <button
                        class="btn btn-link dropdown-toggle px-0"
                        data-bs-toggle="dropdown"
                        aria-expanded="false"
                        :disabled="user.role === 'user' || user.role === 'admin'"
                      >
                        <mdicon name="dots-horizontal" :width="24" :height="24" />
                      </button>
                      <ul class="dropdown-menu">
                        <div v-if="user.role === 'manager'">
                          <li v-if="!user.approved">
                            <b
                              ><a
                                class="dropdown-item d-flex align-items-center"
                                href="javascript:void(0)"
                                @click="approveUser(user, true)"
                              >
                                <mdicon name="check-circle" class="text-success me-2" :size="20" />
                                Approve
                              </a></b
                            >
                          </li>
                          <li v-else>
                            <b
                              ><a
                                class="dropdown-item d-flex align-items-center"
                                href="javascript:void(0)"
                                @click="approveUser(user, false)"
                              >
                                <mdicon name="cancel" class="fw-bold text-danger me-2" :size="20" />
                                Revoke
                              </a></b
                            >
                          </li>
                        </div>
                      </ul>
                      <button class="btn btn-link text-decoration-none px-0" aria-expanded="false">
                        <mdicon
                          name="close-circle"
                          class="text-danger"
                          :size="20"
                          @click="deleteUser(user)"
                        />
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div v-else>No Users to show!</div>
          </div>
        </div>
      </div>
    </div>
    <!-- <pre>{{ users }}</pre> -->
  </div>

  <!-- Delete Modal -->
  <div class="modal fade" id="modalUserDelete" role="dialog" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Delete User</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <p>All the data of the user will be deleted. This action is irreversible</p>
          <p>Are you sure you want to do this?</p>
        </div>
        <div class="modal-footer">
          <button @click="modalUserDelete" type="button" class="btn btn-danger">
            <span v-if="loading" class="spinner-border spinner-border-sm"></span>
            <span v-else>
              <mdicon name="delete" class="text-white me-1" :size="16" />
            </span>
            Delete
          </button>
          <button
            type="button"
            class="btn btn-secondary"
            id="modalUserDeleteClose"
            data-bs-dismiss="modal"
          >
            <mdicon name="window-close" class="text-white me-1" :size="18" />
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
import { ref, onMounted } from 'vue'
import axiosClient from '@/js/axios.js'
import { Modal } from 'bootstrap'
import LoadingIndicator from '@/components/LoadingIndicator.vue'

const users = ref([])
const main_loading = ref(true)
const loading = ref(false)
const errordata = {
  isError: false,
  msg: ''
}

const current_user = ref('')

// let modal
let modalDelete
onMounted(() => {
  modalDelete = new Modal(document.getElementById('modalUserDelete'), {
    keyboard: false
  })
})

async function fetchUsers() {
  console.log('Fetching Users...')
  main_loading.value = true
  try {
    const res = await axiosClient.get('/api/user')
    users.value = res.data
  } catch (err) {
    console.log(err)
  } finally {
    main_loading.value = false
  }
}

const refresh = async () => {
  console.log('Refreshing Users...')
  await fetchUsers()
}

function formatDate(timestamp) {
  const date = new Date(timestamp)
  const options = {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  }
  return date.toLocaleDateString('en-IN', options)
}

// const showUser = (user) => {
//   console.log('show user details')
// }

const approveUser = async (user, approved) => {
  console.log('approve user')
  const formData = new FormData()
  // formData.append('user_id', user.id)
  // formData.append('approved', !!approved)
  formData.append('name', user.name)
  formData.append('username', user.username)
  formData.append('email', user.email)
  formData.append('approved', approved)

  try {
    main_loading.value = true
    await axiosClient.put(`/api/user/${user.username}`, formData)
  } catch (err) {
    console.log(err)
  } finally {
    main_loading.value = false
  }

  await fetchUsers()
}

// const revokeUser = (user) => {
//   console.log('reject user')
// }

const deleteUser = (user) => {
  // console.log('delete user')
  current_user.value = user.username
  errordata.isError = false
  errordata.msg = ''
  modalDelete.show()
}

const modalUserDelete = async () => {
  console.log('modal: deleting user')
  errordata.isError = false
  errordata.msg = ''
  loading.value = true

  try {
    const resp = await axiosClient.delete(`api/user/${current_user.value}`)
    console.log(resp)
    console.log('modal:Closing modal')
    document.getElementById('modalUserDeleteClose').click()
    fetchUsers()
  } catch (err) {
    console.log(err)
    ;(errordata.isError = true), (errordata.msg = err.response.data)
  } finally {
    loading.value = false
  }
}

await fetchUsers()
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
