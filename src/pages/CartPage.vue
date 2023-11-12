<template>
  <main-layout>
    <!-- <pre>{{ cart.items }}</pre> -->
    <div>
      <h2 class="text-center">Your Cart</h2>
      <div class="card col-8 m-auto">
        <div class="row col-12 justify-content-center m-auto">
          <div v-if="cart.items.length > 0" class="col-8 mt-3">
            <div class="table-responsive">
              <table class="table table-hover text-center">
                <thead>
                  <tr class="table-light rounded-1">
                    <th scope="col"><b>ID</b></th>
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
                    <td>{{ item.item }}</td>
                    <td>
                      <mdicon @click="item.quantity--" name="minus-circle" class="text-danger" />
                      <label class="text-center" style="width: 2em">{{ item.quantity }}</label>
                      <mdicon @click="item.quantity++" name="plus-circle" class="text-success" />
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
                    <td>₹{{ total }}/-</td>
                  </tr>
                  <tr>
                    <td></td>
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
                      <button type="button" class="btn btn-sm btn-primary ml-auto">
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
                        Order
                      </button>
                    </td>
                  </tr>
                </tfoot>
              </table>
            </div>
          </div>
          <div v-else>
            <h2 class="text-center mt-5">Your Cart is Empty!</h2>
          </div>
        </div>
      </div>
    </div>
  </main-layout>
</template>

<script setup>
import { computed } from 'vue'
import { useCartStore } from '@/stores/cartstore.js'
import { useRouter } from 'vue-router'
import MainLayout from '@/layouts/MainLayout.vue'

const router = useRouter()
const cart = useCartStore()
const total = computed(() => cart.items.reduce((y, x) => (y += x.quantity * x.unit_price), 0))

const deleteItem = (id) => {
  console.log('delete item event')
  cart.items.splice(id, 1)
}
</script>

<style scoped></style>
