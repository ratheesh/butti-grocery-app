<template>
<manager-layout>
    <div class="text-center">
        <h3>Checkout</h3>
    </div>
  <div class="row col-8 m-auto">
    <div class="col-6 m-auto">
      <div class="form-group mb-4">
        <label for="username"
          >Name<span class="text-danger"><b>*</b></span></label
        >
        <div class="input-group">
          <span class="input-group-text" id="username">
            <mdicon name="account" :size="20" />
          </span>
          <input
            type="text"
            :class="{ 'form-control':true, 'is-invalid':errors.username }"
            placeholder="Receipt Name"
            id="username"
            v-model="order_info.name"
            autofocus
          />
        </div>
      </div>
      <div class="form-group mb-4">
        <label for="address"
          >Delivery Address<span class="text-danger"><b>*</b></span></label
        >
        <div class="input-group">
          <span class="input-group-text" id="address">
            <mdicon name="map-marker" :size="20" />
          </span>
          <textarea
            type="text"
            :class="{ 'form-control':true, 'is-invalid':errors.address }"
            placeholder="Delivery Address"
            id="address"
            v-model="order_info.address"
            autofocus
          />
        </div>
      </div>
      <div class="form-group mb-4">
        <label for="phone"
          >Phone Number<span class="text-danger"><b>*</b></span></label
        >
        <div class="input-group">
          <span class="input-group-text" id="phone">
            <mdicon name="phone" :size="20" />
          </span>
          <input
            type="text"
            :class="{ 'form-control':true, 'is-invalid':errors.phone }"
            placeholder="Phone Number(10 digits)"
            id="phone"
            v-model="order_info.phone"
            autofocus
          />
        </div>
      </div>
      <div class="form-group mb-4">
        <label for="email"
          >Email<span class="text-danger"><b>*</b></span></label
        >
        <div class="input-group">
          <span class="input-group-text" id="email">
            <mdicon name="email" :size="20" />
          </span>
          <input
            type="email"
            :class="{ 'form-control':true, 'is-invalid':errors.email }"
            placeholder="user@email.com"
            id="email"
            v-model="order_info.email"
            autofocus
          />
        </div>
      </div>
      <hr/>
        <div class="d-flex align-items-center justify-content-end mb-3">
          <button class="btn btn-sm btn-warning mx-2" @click="gotoCartPage">
            <mdicon name="arrow-left-bold" :size="18" />
            Review Cart
          </button>
          <button class="btn btn-sm btn-primary mx-2" @click="gotoOrderPage">
              <mdicon name="shopping-outline" :size="16" />
              Place Order
          </button>
        </div>
    </div>
  </div>
</manager-layout>
</template>

<script setup>
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import ManagerLayout from '@/layouts/MainLayout.vue'
// import { useCartStore } from '@/stores/cartstore.js'

// const cart = useCartStore()
const order_info=reactive({
  name: '',
  address: '',
  phone: '',
  email: '',
  delivery_date: '',
})

const errors = reactive({
  username: false,
  address: false,
  phone: false,
  email: false,
  delivery_date: false,
})  

const router = useRouter()

const gotoCartPage = () => {
  router.push('/cart')
}

const gotoOrderPage = () => {
  router.push('/order')
}

</script>

<style scoped lang="scss"></style>