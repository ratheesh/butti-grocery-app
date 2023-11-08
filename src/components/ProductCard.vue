<template>
  <div>
    <div class="card mb-3 h-100" style="width: 16rem">
      <img
        class="card-img-top object-fit-cover shadow"
        :src="data.image"
        alt="apples"
        height="150"
      />
      <div class="card-body">
        <div class="inline-flex justify-content-between">
          <div class="row">
            <div class="col">
              <b class="fs-6">Apples</b>
            </div>
            <div class="col">
              <span class="text-dark fw-bold fs-6"><b>₹</b>{{ data.price }}</span>
            </div>
          </div>
        </div>
        <!-- <p class="card-text">{{ data.description }}</p> -->
        <br/>
        <div class="inline-flex">
          <div class="row text-center d-inline-flex align-items-center">
            <div class="col d-flex align-items-center">
              <mdicon @click="updateCount()" name="minus-circle" class="text-danger"/>
              <label class="text-center" style="width: 2em">{{ data.quantity }}</label>
              <mdicon
                @click="updateCount(true)"
                name="plus-circle"
                class="text-success"
              />
            </div> 
            <div class="col">
              <form @submit.prevent="addToCart">
                <button class="btn btn-success btn-sm">
                  <mdicon name="cart-plus" :size="20"/>Add
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from "vue";

const data = reactive({
  id: 1,
  name: "Apples",
  price: 1.99,
  description: "Kashmir Apples",
  // image: 'https://images.squarespace-cdn.com/content/v1/5b5b5824f2e6b10639fdaf09/1651599956690-0CE43F9HKEXIEK89CY0B/1.png',
  image: "https://picsum.photos/200/300?random=1",
  quantity: 0,
});

const updateCount = (add) => {
  if (add) {
    if (data.quantity < 0) data.quantity = 0;
    data.quantity++;
  } else {
    if (data.quantity < 0) data.quantity = 0;
    if (data.quantity > 0) {
      data.quantity--;
    }
  }
};
</script>

<style scoped></style>
