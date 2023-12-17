<template>
  <manager-layout>
    <div class="text-center">
      <h3>Checkout</h3>
    </div>
    <div class="row col-md-6 col-lg-8 m-auto gy-3 p-0">
      <cart-component></cart-component>
    </div>
    <div v-if="cart.items.length > 0" class="row col-md-6 col-lg-8 m-auto gy-3 p-0">
      <div class="card rounded shadow-sm border-1 p-0">
        <div class="card-header">
          <h4 class="text-center">Delivery Information</h4>
        </div>
        <div class="card-body mt-3 p-0">
          <form
            @submit.prevent="placeOrder"
            needs-validation
            novalidate
            :class="{ 'was-validated ': wasValidated }"
          >
            <div class="col-md-6 col-lg-8 m-auto">
              <div class="form-group mb-4">
                <label for="name"
                  >Name<span class="text-danger"><b>*</b></span></label
                >
                <div class="input-group">
                  <span class="input-group-text" id="username">
                    <mdicon name="account" :size="20" />
                  </span>
                  <input
                    type="text"
                    :class="{
                      'form-control': true,
                      'rounded-end': true,
                      'is-invalid': errors.name
                    }"
                    placeholder="Receipt Name"
                    id="name"
                    v-model="delivery_info.name"
                    required
                    autofocus
                  />
                  <div class="invalid-feedback">
                    <p class="text-danger">Provide receiver name</p>
                  </div>
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
                    :class="{
                      'form-control': true,
                      'rounded-end': true,
                      'is-invalid': errors.address
                    }"
                    placeholder="Delivery Address"
                    id="address"
                    v-model="delivery_info.address"
                    required
                    autofocus
                  />
                  <div class="invalid-feedback">
                    <p class="text-danger">Provide valid address</p>
                  </div>
                </div>
              </div>
              <div class="form-group mb-4">
                <label for="phone"
                  >Phone Number<span class="text-danger"><b>*</b></span></label
                >
                <div class="input-group">
                  <span class="input-group-text" id="phone">
                    <mdicon name="phone" :size="20" />&nbsp; +91-
                  </span>
                  <input
                    type="number"
                    :class="{
                      'form-control': true,
                      'rounded-end': true,
                      'is-invalid': errors.phone_number
                    }"
                    placeholder="9876543210"
                    id="phone"
                    v-model="delivery_info.phone_number"
                    required
                    autofocus
                    min="1000000000"
                    max="9999999999"
                  />
                  <div class="invalid-feedback">
                    <p class="text-danger">Provide valid phone number</p>
                  </div>
                </div>
              </div>
              <div class="form-group mb-4">
                <label for="deliveryDate"
                  >Delivery Date<span class="text-danger"><b>*</b></span></label
                >
                <div class="input-group">
                  <span class="input-group-text" id="email">
                    <mdicon name="calendar" :size="20" />
                  </span>
                  <input
                    type="date"
                    :class="{
                      'form-control': true,
                      'rounded-end': true,
                      'is-invalid': errors.delivery_date
                    }"
                    placeholder=""
                    id="deliveryDate"
                    v-model="delivery_info.delivery_date"
                    required
                    autofocus
                  />
                  <div class="invalid-feedback">
                    <p class="text-danger">Delivery date should be in future</p>
                  </div>
                </div>
              </div>
              <hr />
              <div class="d-flex align-items-center justify-content-end mb-3">
                <a class="btn btn-sm btn-warning mx-2" href="#">
                  <mdicon name="home" :size="18" />
                  Go Home
                </a>
                <button type="submit" class="btn btn-sm btn-primary mx-2">
                  <mdicon name="shopping-outline" :size="16" />
                  Place Order
                </button>
              </div>
              <div
                v-if="errorinfo.isErr"
                class="alert alert-danger mx-2 text-center d-flex justify-content-center"
                role="alert"
              >
                {{ errorinfo.msg }}
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
    <!-- <pre>{{ cart }}</pre> -->
    <!-- <pre>{{ delivery_info }}</pre> -->
  </manager-layout>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useAuthStore } from '@/stores/authstore.js'
import axiosClient from '@/js/axios.js'
import router from '@/router/index.js'
import { useCartStore } from '@/stores/cartstore.js'
import ManagerLayout from '@/layouts/MainLayout.vue'
import CartComponent from '@/components/CartComponent.vue'

const loading = ref(false)
const auth = useAuthStore()
// const cart = useCartStore()

const delivery_info = reactive({
  name: auth.user.name,
  address: '',
  phone_number: 0,
  delivery_date: new Date().toISOString().split('T')[0]
})

const errorinfo = reactive({
  isErr: false,
  msg: ''
})
const errors = reactive({
  name: false,
  address: false,
  phone: false,
  delivery_date: false
})
const wasValidated = ref(false)

// const router = useRouter()
const cart = useCartStore()

const placeOrder = async () => {
  console.log('validating order')

  wasValidated.value = false
  errorinfo.isErr = false
  errorinfo.msg = ''
  errors.name = false
  errors.address = false
  errors.phone_number = false
  errors.delivery_date = false

  if (
    !delivery_info.name ||
    !delivery_info.address ||
    !delivery_info.phone_number ||
    !delivery_info.delivery_date
  ) {
    errors.name = !delivery_info.name
    errors.address = !delivery_info.address
    errors.phone_number = !delivery_info.phone_number
    errors.delivery_date = !delivery_info.delivery_date
    return
  }

  if (delivery_info.phone_number < 1000000000 || delivery_info.phone_number > 9999999999) {
    errors.phone_number = true
    errorinfo.isErr = true
    errorinfo.msg = 'Provide valid phone number'
    return
  }

  if (delivery_info.delivery_date < new Date().toISOString().split('T')[0]) {
    errors.delivery_date = true
    errorinfo.isErr = true
    errorinfo.msg = 'Delivery date should be in future'
    return
  }

  wasValidated.value = true

  console.log('Placing order')
  const formData = new FormData()
  formData.append('name', delivery_info.name)
  formData.append('address', delivery_info.address)
  formData.append('phone_number', parseInt(delivery_info.phone_number))
  // for (const item of cart.items) {
  //   formData.append('items', JSON.stringify(item))
  // }
  formData.append('items', JSON.stringify(cart.items))
  const deliverydate = new Date(delivery_info.delivery_date)
    .toISOString()
    .slice(0, 16)
    .replace('T', ' ')
  // console.log(deliverydate)
  formData.append('delivery_date', deliverydate)
  // console.log(cart.totalAmount)
  formData.append('total_amount', cart.totalAmount)
  // console.log(formData)

  try {
    loading.value = true
    const resp = await axiosClient.post(`/api/order`, formData)
    console.log(resp)
    cart.clear()
    router.push('/orders')
  } catch (err) {
    console.log(err)
    errorinfo.isErr = true
    errorinfo.msg = err.response.data
  } finally {
    loading.value = false
    wasValidated.value = false
    // errorinfo.isErr = false
    // errorinfo.msg = ''
    errors.name = false
    errors.address = false
    errors.phone = false
    errors.delivery_date = false
  }
}
</script>

<style scoped lang="scss"></style>
