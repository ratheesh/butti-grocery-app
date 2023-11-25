<template>
  <main-layout>
    <div class="container">
      <h1 class="text-center pt-3">Order Summary</h1>
      <div class="row justify-content-center border border-dark-subtle">
        <div class="col-10">
          <table class="table table-hover text-center">
            <thead class="table-light rounded-1">
              <tr>
                <th scope="col"><b>ID</b></th>
                <th scope="col"><b>ITEM</b></th>
                <th scope="col"><b>QTY</b></th>
                <th scope="col"><b>UNIT PRICE</b></th>
                <th scope="col"><b>TOTAL</b></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, idx) in cart.items" :key="idx" :id="item.id">
                <td>{{ item.id }}</td>
                <td>{{ item.name }}</td>
                <td>
                  <label class="text-center" style="width: 2em">{{ item.quantity }}</label>
                </td>
                <td>₹{{ item.unit_price }}/-</td>
                <td>₹{{ item.quantity * item.unit_price }}/-</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="row">
        <div class="col-10">
          <h4>Shipping Info</h4>
          <h5><span>Name:</span><span>Ratheesh</span></h5>
          <h5><span>Phone Number:</span><span>+91 9876543210</span></h5>
          <h5>Shipping Address:</h5>
          <p>
            123, Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam voluptatum,
            voluptatibus, quibusdam, quia voluptas quod quos voluptates quae quidem doloribus quas.
            Quisquam voluptatum, voluptatibus, quibusdam, quia voluptas quod quos voluptates quae
            quidem doloribus quas.
          </p>
        </div>
      </div>
      <div class="row">
        <div class="col-10">
          <h4>Payment</h4>
          <h5>Payment Method: <span>Cash on Delivery</span></h5>
        </div>
      </div>
      <div class="row">
        <div class="col-10">
          <button class="btn btn-sm btn-primary">Place Order</button>
        </div>
      </div>
      <pre>{{ items }}</pre>
    </div>
  </main-layout>
</template>

<script setup>
import { useCartStore } from '@/stores/cartstore.js'
import { onMounted, ref } from 'vue'
import MainLayout from '@/layouts/MainLayout.vue'

const items = ref([])

const cart = useCartStore()

onMounted(() => {
  items.value = cart.items
})
</script>

<style scoped>
th {
  vertical-align: middle;
  border-bottom: 3px solid #485460;
  font-size: 12px, bold;
}
</style>
