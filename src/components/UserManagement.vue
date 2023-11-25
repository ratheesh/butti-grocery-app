<template>
  <div class="row justify-content-center ">
    <div class="col-8">
      <div class="card">
        <div class="card-body shadow-sm">
          <div v-if="main_loading">
            <loading-indicator></loading-indicator>
          </div>
          <div v-else class="table-responsive">
            <table class="table">
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
                      <img src="https://appsrv1-147a1.kxcdn.com/volt-dashboard-pro-v141/img/team/profile-picture-1.jpg"
                        height="40" width="40" class="avatar rounded-circle me-3" alt="profile" />
                      <div class="d-block">
                        <span class="fw-bold">{{ user.name }}</span>
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
                      <mdicon name="check-circle" :width="16" :height="16" class="text-success p-1"
                        data-bs-toggle="dropdown" aria-expanded="false" />
                      Active
                    </div>
                  </td>
                  <td v-else>
                    <div class="d-flex align-items-center">
                      <mdicon name="clock-time-four" :width="16" :height="16" class="text-warning p-1"
                        data-bs-toggle="dropdown" aria-expanded="false" />
                      <span class="text-warning">Pending</span>
                    </div>
                  </td>
                  <td>
                    <button class="btn btn-link dropdown-toggle px-0 " data-bs-toggle="dropdown" aria-expanded="false">
                      <mdicon name="dots-horizontal" :width="24" :height="24" />
                    </button>
                    <ul class="dropdown-menu">
                      <li>
                        <b><a class="dropdown-item d-flex align-items-center" @click="showUser(user)">
                            <mdicon name="eye" class="text-gray me-2" :size="20" />
                            View Details
                          </a></b>
                      </li>
                      <li v-if="!user.approved">
                        <b><a class="dropdown-item d-flex align-items-center" @click="approveUser(user)">
                            <mdicon name="check-circle" class="text-success me-2" :size="20" />
                            Approve
                          </a></b>
                      </li>
                      <li v-else>
                        <b><a class="dropdown-item d-flex align-items-center" @click="revokeUser(user)">
                            <mdicon name="cancel" class="fw-bold text-danger me-2" :size="20" />
                            Revoke
                          </a></b>
                      </li>
                    </ul>
                    <button class="btn btn-link text-decoration-none px-0 " aria-expanded="false">
                      <mdicon name="close-circle" class="text-danger" :size="20" @click="deleteUser(user)" />
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
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
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
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
          <button type="button" class="btn btn-secondary" id="modalUserDeleteClose" data-bs-dismiss="modal">
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
import { ref, onMounted } from 'vue';
import axiosClient from '@/js/axios.js'; 
import { Modal } from 'bootstrap';
import LoadingIndicator from '@/components/LoadingIndicator.vue';

const users = ref([]);
const main_loading = ref(true)
const loading = ref(false)
const errordata = {
  isError:false,
  msg:''
}

const current_user=ref('')

let modal
let modalDelete
onMounted(() => {
  modalDelete = new Modal(document.getElementById('modalUserDelete'), {
    keyboard : false
  })
});

async function fetchUsers() {
  console.log('Fetching Users...')
  // await new Promise((resolve) => setTimeout(resolve, 3000));

  try {
  const res = await axiosClient .get('/api/user')
  users.value = res.data
  } catch(err) {
    console.log(err)
  } finally {
    main_loading.value = false
  }
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

const showUser = (user) => {
  console.log('show user details')
}

const approveUser = (user) => {
  console.log('approve user')
}

const revokeUser = (user) => {
  console.log('reject user')
}

const deleteUser = (user) => {
  // console.log('delete user')
  current_user.value = user.username
  modalDelete.show()
}

const modalUserDelete = async() => {
  console.log('modal: deleting user')
  loading.value = true
  
  try {
    const resp = await axiosClient.delete(`api/user/${current_user.value}`)
    console.log(resp)
    console.log('modal:Closing modal')
    document.getElementById('modalUserDeleteClose').click()
    fetchUsers()
  } catch(err) {
    console.log(err)
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
