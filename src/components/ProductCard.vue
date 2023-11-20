<template>
  <div>
    <div class="card mb-3 h-100" style="width: 16rem">
      <img
        class="card-img-top object-fit-contain shadow"
        :src="`data:image/png;base64,${data.image}`"
        alt="product image"
        height="150"
      />
      <div class="card-body">
        <div class="row justify-content-between">
          <div class="col">
            <b class="fs-6">{{ data.name }}</b>
          </div>
          <div class="col-auto">
            <span class="text-dark text-right fw-normal fs-6"
              ><b>₹</b><b>{{ data.price }}</b
              >/{{ data.unit }}</span
            >
          </div>
        </div>
        <br />
        <br />
        <div class="row justify-items-between">
          <div class="col d-inline-flex align-items-center">
            <mdicon @click="updateCount()" name="minus-circle" class="text-danger" />
            <label class="text-center" style="width: 2em">{{ quantity }}</label>
            <mdicon @click="updateCount(true)" name="plus-circle" class="text-success" />
          </div>
          <div class="col-auto">
            <form @submit.prevent="addToCart(data)">
              <button class="btn btn-success btn-sm">
                <mdicon name="cart-plus" :size="20" />Add
              </button>
            </form>
          </div>
        </div>
      </div>
      <!-- <pre>{{ data }}</pre> -->
    </div>
  </div>
</template>

<script setup>
import { ref, toRef } from 'vue'
import { useCartStore } from '@/stores/cartstore.js'

const props = defineProps({
  data: {
    type: Object,
    required: true
  }
})

const data = toRef(props, 'data')
const quantity = ref(1)

const updateCount = (add) => {
  if (add) {
    if (quantity.value < 1) quantity.value = 1
    quantity.value++
  } else {
    if (quantity.value < 1) quantity.value = 1
    if (quantity.value > 1) {
      quantity.value--
    }
  }
}

const cart = useCartStore()
function addToCart(product) {
  if (quantity.value < 1) {
    console.log('addToCart: Quantity cannot be zero')
    return
  }

  // if the added item is already in the cart, update the quantity
  const _item = cart.items.find((item) => item.id === product.id)
  if (_item) {
    const index = cart.items.indexOf(_item)
    // cart.items.splice(index, 1, _item)
    const item = cart.items[index]
    item.quantity += quantity.value
    return
  }

  let item = {}
  item.id = product.id
  item.name = product.name
  item.unit = product.unit
  item.unit_price = product.price
  item.quantity = quantity.value

  cart.items.push(item)
}
</script>

<style scoped></style>
