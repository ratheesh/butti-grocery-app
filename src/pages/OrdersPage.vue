<template>
  <main-layout>
    <h3 class="text-center mt-3">Your Orders</h3>
    <div class="row col-8 m-auto">
      <div class="card border-1 rounded p-0">
        <div class="card-body">
          <div v-if="loading">
            <loading-indicator></loading-indicator>
          </div>
          <div v-else>
            <div v-if="orders.length > 0">
              <div class="row justify-content-center m-auto">
                <div class="col-12">
                  <table class="table table-responsive">
                    <thead class="table-light">
                      <tr>
                        <th scope="col"><b>ID</b></th>
                        <th scope="col"><b>NAME</b></th>
                        <th scope="col"><b>ORDERED DATE</b></th>
                        <th scope="col"><b>ITEMS</b></th>
                        <th scope="col"><b>AMOUNT</b></th>
                        <th scope="col"><b>DELIVERY DATE</b></th>
                        <th scope="col"><b>ACTIONS</b></th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="order in orders" :key="order.id">
                        <td>{{ order.id }}</td>
                        <td>{{ order.name }}</td>
                        <td>{{ formatDate(order.created_timestamp) }}</td>
                        <td>{{ order.items.length }}</td>
                        <td>{{ order.total_amount }}</td>
                        <td>{{ formatDate(order.delivery_date) }}</td>
                        <td>
                          <button class="btn btn-sm btn-primary" @click="router.push(`/order/${order.id}`)">
                            <mdicon
                              name="format-list-bulleted"
                              :width="18"
                              :height="18"
                              aria-expanded="false"
                            />
                            Details
                          </button>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
            <div v-else class="text-center my-3">
              <h4>You have No Orders!</h4>
              <p>Goto Homepage and order something!</p>
            </div>
          </div>
        </div>
      </div>
      <div class="d-inline-flex justify-content-end my-2">
        <a href="#" class="btn btn-sm btn-primary">
          <div class="d-inline-flex justify-content-center align-items-end">
            <mdicon name="home" class="text-white" />
            <span>Go Home</span>
          </div>
        </a>
      </div>
    </div>
    <!-- <pre>{{ orders }}</pre> -->
  </main-layout>
</template>

<script setup>
import { ref, reactive } from 'vue'
import router from '@/router/index.js'
import axiosClient from '@/js/axios.js'
import MainLayout from '@/layouts/MainLayout.vue'
import LoadingIndicator from '@/components/LoadingIndicator.vue'

const loading = ref(true)
const orders = ref([])
const errordata = reactive({
  isErr: false,
  msg: ''
})

function formatDate(timestamp) {
  const date = new Date(timestamp)
  const options = {
    weekday: 'short',
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    timeZone: 'Asia/Kolkata'
  }
  return date.toLocaleDateString('en-IN', options)
}

const fetchOrders = async () => {
  try {
    loading.value = true
    const resp = await axiosClient(`/api/order`)
    orders.value = resp.data
    console.log(resp)
  } catch (err) {
    console.log(err)
    errordata.isErr = true
    // errordata.msg = err.response.data
  } finally {
    loading.value = false
  }
}

fetchOrders()
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
