<template>
  <main-layout>
    <!-- <pre>{{ cart.items }}</pre> -->
    <div>
      <h2 class="text-center">Your Cart</h2>
      <div class="card col-8 m-auto">
        <div class="row col-12 justify-content-center m-auto">
          <div v-if="cart.items.length > 0" class="col-10 mt-3">
            <table class="table table-responsive table-nowrap text-center">
              <thead class="border-bottom table-light">
                <tr>
                  <th scope="col"><b>#</b></th>
                  <th scope="col"><b>ITEM</b></th>
                  <th scope="col"><b>QTY</b></th>
                  <th scope="col"><b>DELETE</b></th>
                  <th scope="col"><b>UNIT PRICE</b></th>
                  <th scope="col"><b>TOTAL</b></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, idx) in cart.items" :key="idx" :id="item.id">
                  <td>{{ item.id }}</td>
                  <td>{{ item.name }}</td>
                  <td>
                    <mdicon @click="updateCount(item)" name="minus-circle" class="text-danger" />
                    <label class="text-center" style="width: 2em">{{ item.quantity }}</label>
                    <mdicon
                      @click="updateCount(item, true)"
                      name="plus-circle"
                      class="text-success"
                    />
                  </td>
                  <td>
                    <mdicon name="trash-can" class="text-danger" @click="deleteItem(idx)" />
                  </td>
                  <td>₹{{ item.unit_price }}/-</td>
                  <td>₹{{ item.quantity * item.unit_price }}/-</td>
                </tr>
              </tbody>
              <tfoot>
                <tr>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td><b>Order Total Amount</b></td>
                  <td class="fw-bold">₹{{ total }}/-</td>
                </tr>
                <tr>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td style="text-right">
                    <button
                      type="button"
                      class="btn btn-sm btn-secondary"
                      @click="router.push('/')"
                    >
                      <mdicon name="home" :height="20" />Goto Home
                    </button>
                  </td>
                  <td>
                    <button type="button" class="btn btn-sm btn-danger" @click="clearCart">
                      <mdicon name="cart-remove" :height="18" />Clear Cart
                    </button>
                  </td>
                  <td>
                    <button
                      type="button"
                      class="btn btn-sm btn-primary ml-auto"
                      @click="showDeliveryInfo = true"
                    >
                      <svg
                        width="16px"
                        height="16px"
                        viewBox="0 0 1024 1024"
                        fill="#ffffff"
                        class="icon"
                        version="1.1"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          d="M53.6 1023.2c-6.4 0-12.8-2.4-17.6-8-4.8-4.8-7.2-11.2-6.4-18.4L80 222.4c0.8-12.8 11.2-22.4 24-22.4h211.2v-3.2c0-52.8 20.8-101.6 57.6-139.2C410.4 21.6 459.2 0.8 512 0.8c108 0 196.8 88 196.8 196.8 0 0.8-0.8 1.6-0.8 2.4v0.8H920c12.8 0 23.2 9.6 24 22.4l49.6 768.8c0.8 2.4 0.8 4 0.8 6.4-0.8 13.6-11.2 24.8-24.8 24.8H53.6z m25.6-48H944l-46.4-726.4H708v57.6h0.8c12.8 8.8 20 21.6 20 36 0 24.8-20 44.8-44.8 44.8s-44.8-20-44.8-44.8c0-14.4 7.2-27.2 20-36h0.8v-57.6H363.2v57.6h0.8c12.8 8.8 20 21.6 20 36 0 24.8-20 44.8-44.8 44.8-24.8 0-44.8-20-44.8-44.8 0-14.4 7.2-27.2 20-36h0.8v-57.6H125.6l-46.4 726.4zM512 49.6c-81.6 0-148.8 66.4-148.8 148.8v3.2h298.4l-0.8-1.6v-1.6c0-82.4-67.2-148.8-148.8-148.8z"
                          fill=""
                        />
                      </svg>
                      Checkout
                    </button>
                  </td>
                </tr>
              </tfoot>
            </table>
          </div>
          <div v-else>
            <h2 class="text-center mt-5">Your Cart is Empty!</h2>
          </div>
        </div>
      </div>
    </div>

    <div v-show="showDeliveryInfo">
      <div class="row col-8 m-auto gy-3">
        <div class="card rounded shadow-sm border-1 p-0">
          <div class="card-header">
            <h4 class="text-center">Delivery Information</h4>
          </div>
          <div class="card-body">
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
                    :class="{ 'form-control': true, 'is-invalid': errors.username }"
                    placeholder="Receipt Name"
                    id="username"
                    v-model="delivery_info.name"
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
                    :class="{ 'form-control': true, 'is-invalid': errors.address }"
                    placeholder="Delivery Address"
                    id="address"
                    v-model="delivery_info.address"
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
                    :class="{ 'form-control': true, 'is-invalid': errors.phone }"
                    placeholder="Phone Number(10 digits)"
                    id="phone"
                    v-model="delivery_info.phone"
                    autofocus
                  />
                </div>
              </div>
              <div class="form-group mb-4">
                <label for="deliverydate"
                  >Delivery Date<span class="text-danger"><b>*</b></span></label
                >
                <div class="input-group">
                  <span class="input-group-text" id="email">
                    <mdicon name="calendar" :size="20" />
                  </span>
                  <input
                    type="date"
                    :class="{ 'form-control': true, 'is-invalid': errors.deliverydate }"
                    placeholder="user@email.com"
                    id="deliverydate"
                    v-model="delivery_info.email"
                    autofocus
                  />
                </div>
              </div>
              <hr />
              <div class="d-flex align-items-center justify-content-end mb-3">
                <a class="btn btn-sm btn-warning mx-2" href="#">
                  <mdicon name="home" :size="18" />
                  Go Home
                </a>
                <button class="btn btn-sm btn-primary mx-2" @click="gotoOrderPage">
                  <mdicon name="shopping-outline" :size="16" />
                  Place Order
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main-layout>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { useCartStore } from '@/stores/cartstore.js'
import { useRouter } from 'vue-router'
import MainLayout from '@/layouts/MainLayout.vue'

const router = useRouter()
const cart = useCartStore()
const total = computed(() => cart.items.reduce((y, x) => (y += x.quantity * x.unit_price), 0))
const showDeliveryInfo = ref(false)
const delivery_info = reactive({
  name: '',
  address: '',
  phone: '',
  delivery_date: ''
})

const errors = reactive({
  username: false,
  address: false,
  phone: false,
  email: false,
  delivery_date: false
})

const deleteItem = (id) => {
  console.log('delete item event')
  cart.items.splice(id, 1)
  cart.updateItems()
}

const clearCart = () => {
  cart.items = []
  cart.updateItems()
}

const updateCount = (item, add) => {
  if (add) {
    if (item.quantity < 1) item.quantity = 1
    item.quantity++
  } else {
    if (item.quantity < 1) item.quantity = 1
    if (item.quantity > 1) {
      item.quantity--
    }
  }
  cart.updateItems()
}
</script>

<style scoped>
th {
  vertical-align: middle;
  border-bottom: 3px solid #485460;
  font-size: 12px, bold;
}
</style>
