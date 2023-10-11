<template>
  <main-layout>
    <!-- <pre>{{ cart.items }}</pre> -->
    <div v-if="cart.items.length > 0">
    <h2 class="text-center">Your Cart</h2> 
    <div class="row justify-content-center m-auto">
      <div class="col-8">
        <hr/>
        <table class="table table-hover text-center">
          <thead>
            <tr>
              <th scope="col"><b>Item#</b></th>
              <th scope="col"><b>Item</b></th>
              <th scope="col"><b>Quantity</b></th>
              <th scope="col"><b>Unit Price</b></th>
              <th scope="col"><b>Total</b></th>
              <th scope="col"><b>Delete</b></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for='(item, idx) in cart.items' :id="item.id">
            <th>{{ item.id }}</th>
            <th>{{ item.item }}</th>
            <th>
              <mdicon @click="item.quantity--" name="minus-circle" class="text-danger" />
              <label class="text-center" style="width: 2em">{{ item.quantity }}</label>
              <mdicon
                @click="item.quantity++"
                name="plus-circle"
                class="text-success"
              />
            </th>
            <th>₹{{ item.unit_price }}/-</th>
            <th>₹{{ item.quantity * item.unit_price }}/-</th>
            <th><mdicon name="delete" class="text-secondary" @click="deleteItem(idx)" /></th>
            </tr>
            <tr>
            <th></th>
            <th></th>
            <th></th>
            <th><b>Order Total Amount</b></th>
            <th>₹{{ total }}/-</th>
            <th></th>
            </tr>
            <tr>
            <th></th>
            <th></th>
            <th></th>
            <th style='text-right'><button type="button" class="btn btn-secondary" @click="router.push('/')"><mdicon name="home" :height='18'/>Goto Home</button></th>
            <th><button type="button" class="btn btn-success ml-auto">Order</button></th>
            <th></th>
            </tr>
          </tbody>
        </table>
      </div>
      </div>
  </div>
  <div v-else>
    <h2 class="text-center mt-5 ">Your Cart is Empty!</h2>
  </div>
  </main-layout>
</template>

<script setup>
import { computed } from 'vue';
import { useCartStore } from '@/stores/cartstore.js';
import { useRouter } from 'vue-router';
import MainLayout from '@/layouts/MainLayout.vue';

const router = useRouter();
const cart = useCartStore()
const total = computed(() => cart.items.reduce((y, x) => y+=(x.quantity * x.unit_price), 0))

const deleteItem=(id) => {
  console.log('delete item event')
  cart.items.splice(id, 1)
}

</script>

<style scoped></style>
