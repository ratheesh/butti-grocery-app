<template>
  <div>
    <div class="card shadow-sm h-100" style="width: 16rem">
      <img
        class="card-img-top object-fit-contain"
        :src="`data:image/png;base64,${data.image}`"
        alt="product image"
        height="150"
        @click="() => $router.push(`/product/${data.category_id}/${data.id}`)"
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
        <div class="row justify-items-between">
          <div v-if="outofstock" class="text-center p-1 fw-bolder">
            <span class="text-danger">Out of Stock</span>
          </div>
          <div v-else class="p-1">
            <br />
          </div>
          <div class="col d-inline-flex align-items-center" :disabled="outofstock">
            <mdicon @click="updateCount()" name="minus-circle" class="text-danger" />
            <label class="text-center" style="width: 2em">{{ quantity }}</label>
            <mdicon @click="updateCount(true)" name="plus-circle" class="text-success" />
          </div>
          <div class="col-auto">
            <form @submit.prevent="addToCart(data)">
              <button class="btn btn-success btn-sm" :disabled="outofstock">
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
import { ref, toRef, onMounted } from 'vue'
import { useCartStore } from '@/stores/cartstore.js'

const props = defineProps({
  data: {
    type: Object,
    required: true
  }
})

const data = toRef(props, 'data') || {}
const quantity = ref(1)
const outofstock = ref(true)

onMounted(() => {
  data.value.stock_available < 1 ? (outofstock.value = true) : (outofstock.value = false)
})

const updateCount = (add) => {
  if (outofstock.value) return

  if (add) {
    if (quantity.value < 1) quantity.value = 1
    if (quantity.value < data.value.stock_available) quantity.value++
  } else {
    if (quantity.value < 1) quantity.value = 1
    if (quantity.value > 1) {
      quantity.value--
    }
  }
  // cart.update()
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
    cart.update()
    return
  }

  let item = {}
  item.id = product.id
  item.name = product.name
  item.unit = product.unit
  item.unit_price = product.price
  item.quantity = quantity.value

  cart.items.push(item)
  console.log('add to cart')
  cart.update()
}
</script>

<style scoped></style>
