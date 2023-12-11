<template>
  <!-- <h2 class="text-center">Your Cart</h2> -->
  <div class="card card-body col-md-8 col-lg-10 m-auto p-0">
    <div class="row col-12 justify-content-center m-auto p-0">
      <div v-if="cart.items.length > 0" class="mt-3">
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
                <mdicon
                  @click="updateCount(item)"
                  name="minus-circle"
                  class="text-danger"
                />
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
              <td></td>
              <td></td>
              <td>
                <button type="button" class="btn btn-sm btn-danger" @click="clearCart">
                  <mdicon name="cart-remove" :height="18" />Clear Cart
                </button>
              </td>
            </tr>
          </tfoot>
        </table>
      </div>
      <div v-else>
        <div class="row justify-content-center align-items-center">
          <h2 class="text-center my-5">Your Cart is Empty!</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useCartStore } from "@/stores/cartstore.js";

const cart = useCartStore();
const total = computed(() =>
  cart.items.reduce((y, x) => (y += x.quantity * x.unit_price), 0)
);

const deleteItem = (id) => {
  console.log("delete item event");
  cart.items.splice(id, 1);
  cart.update();
};

const clearCart = () => {
  cart.items = [];
  cart.update();
};

const updateCount = (item, add) => {
  if (add) {
    if (item.quantity < 1) item.quantity = 1;
    item.quantity++;
  } else {
    if (item.quantity < 1) item.quantity = 1;
    if (item.quantity > 1) {
      item.quantity--;
    }
  }
  cart.update();
};
</script>

<style scoped></style>
