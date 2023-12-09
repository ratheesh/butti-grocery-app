<template>
  <main-layout>
    <div class="container-fluid">
      <h3 class="text-center pt-3">Order Summary</h3>
      <div v-if="loading">
        <loading-indicator></loading-indicator>
      </div>
      <div v-else class="row col-md-6 col-lg-8 m-auto border border-dark border-5 rounded-1">
        <div class="row col-md-6 col-lg-8 m-auto mt-3 px-0 d-inline-flex justify-content-center">
          <div class="col-8 text-center d-flex align-items-end  justify-content-center ">
            <mdicon name="basket" class="text-center text-primary mx-2" height="50" width="50" />
            <span class="text-center mx-2" style="font-size:30px">Butti Grocery Store</span>
          </div>
        </div>
        <div class="row col-md-6 col-lg-8 m-auto mt-1">
          <hr class="text-center text-dark p-0 mt-2 border-bottom border-3 " />
          <div class="col-md-6 col-lg-8">
            <h6>Order ID: <span>#{{ order.id }}</span></h6>
            <h6>Order Date: <span>{{ formatDate(order.created_timestamp) }}</span></h6>
            <h6>Delivery Date: <span>{{ formatDate(order.delivery_date) }}</span></h6>
          </div>
        </div>  
        <div class="row justify-content-center m-auto mt-2">
          <div class="col-md-6 col-lg-8 m-auto">
            <table class="table text-center">
              <thead class="table-secondary">
                <tr>
                  <th scope="col"><b>ID</b></th>
                  <th scope="col"><b>ITEM</b></th>
                  <th scope="col"><b>QTY</b></th>
                  <th scope="col"><b>UNIT PRICE</b></th>
                  <th scope="col"><b>TOTAL</b></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, idx) in order.items" :key="idx" :id="item.id">
                  <td>{{ item.product.id }}</td>
                  <td>
                    <img
                       class="mx-2"
                       :src="`data:image/png;base64,${item.product.image}`"
                       height="30"
                       width="30"
                     />{{ item.product.name }}</td>
                  <td>
                    <label class="text-center" style="width: 2em">{{ item.quantity }}</label>
                  </td>
                  <td>₹{{ item.product.price }}/-</td>
                  <td>₹{{ item.quantity * item.product.price }}/-</td>
                </tr>
              </tbody>
              <tfoot>
                <tr>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td colspan="1" class="text-end"><b>Total</b></td>
                  <td>₹{{ totalAmount() }}/-</td>
                </tr>
              </tfoot>
            </table>
          <!-- <hr class="text-center text-dark p-0 mt-2 border-bottom border-3 " /> -->
          </div>
        </div>
        <div class="row m-auto">
          <div class="col-8 m-auto">
            <h5 class="fw-bolder">Shipping Info</h5>
            <h6><span>Name:</span><span>{{ order.name }}</span></h6>
            <h6><span>E-Mail:</span><span>{{ order.email }}</span></h6>
            <h6><span>Phone Number:</span><span>+91 {{ order.phone }}</span></h6>
            <h6>Shipping Address:</h6>
            <p> {{ order.address }} </p>
          <hr class="text-center text-dark p-0 mt-2 border-bottom border-3 " />
          </div>
        </div>
        <div class="row m-auto">
          <div class="col-8 m-auto">
            <h5 class="fw-bold">Payment</h5>
            <h6>Payment Method: <span>Cash on Delivery</span></h6>
            <h6>Total Amount Payable: <span>₹{{ order.total_amount }}/-</span></h6>
            <h6>Shipping Charges: <span>Free</span></h6>
          </div>
        </div>
          <hr class="text-center text-dark p-0 mt-2 border-bottom border-3 " />
          <small class="text-center">Butti Grocery Store(c) 2023</small>
      </div>
    </div>
    <!-- <pre>{{ props }}</pre> -->
  </main-layout>
</template>

<script setup>
import { ref, toRefs, onMounted } from 'vue'
import axiosClient from '@/js/axios.js'
import MainLayout from '@/layouts/MainLayout.vue'
import LoadingIndicator from '@/components/LoadingIndicator.vue'

const props = defineProps({
  id: String,
})

const { id } = toRefs(props)
const loading = ref(false)
const order = ref({})

function formatDate(timestamp) {
  const date = new Date(timestamp)
  const options = {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  }
  return date.toLocaleDateString('en-IN', options)
}

onMounted(() => {
  console.log(id.value)
})

const totalAmount = () => {
  let total = 0
  order.value.items.forEach(item => {
    total += item.quantity * item.product.price
  })
  return total
}

const fetchOrder = (async() => {
  try {
    loading.value = true
    const resp = await axiosClient.get(`/api/order/${id.value}`)
    console.log(resp)
    order.value = resp.data
  } catch (err) {
    console.log(err)
  } finally {
    loading.value = false
  }
})

fetchOrder()
</script>

<style scoped>
th {
  vertical-align: middle;
  border-bottom: 3px solid #485460;
  font-size: 12px, bold;
}
</style>
