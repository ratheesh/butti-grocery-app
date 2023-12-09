<template>
  <main-layout>
    <div v-if="loading" class="text-center my-3">
      <loading-indicator />
    </div>
    <div v-else>
      <h2 class="text-center my-3">{{ product.name }} Page</h2>
      <div class="row col-md-10 col-lg-12">
        <div class="col-md-3 col-lg-4">
          <img
            :src="`data:image/png;base64,${product.image}`"
            :alt="product.name"
            class="img-fluid border-1 rounded"
            height="250"
            width="250"
          />
        </div>
        <div class="col-md-9 col-lg-8">
          <p>Name: {{ product.name }}</p>
          <p>ID: {{ product.id }}</p>
          <p>Unit Cost: {{ product.price }}/{{ product.unit }}</p>
          <p>Expiry Date: {{ product.expiry_date }}</p>
          <p>Description: {{ product.description }}</p>
        </div>
      </div>
      <div class="row col-md-10 col-lg-12 d-inline-flex justify-content-end">
        <div class="col-md-3 col-lg-4">
          <button class="btn btn-sm btn-primary">
            <mdicon name="home" class="text-white" />
            Go Home
          </button>
        </div>

        <div class="col-md-3 col-lg-4">

        </div>
        <div class="col-md-3 col-lg-4">
          <button class="btn btn-sm btn-primary">
            <mdicon name="cart-plus" class="text-white" />
            Add to Cart
          </button>
        </div>
        </div>
    </div>
  </main-layout>
</template>

<script setup>
import { ref } from 'vue';
import  axiosClient  from '@/js/axios.js'
import MainLayout from '@/layouts/MainLayout.vue';
import LoadingIndicator from '@/components/LoadingIndicator.vue';

const props = defineProps({
  category_id:{
    type: String,
    required: true,
  },
  id: {
    type: String,
    required: true,
  },
});

const product = ref({})
const loading = ref(false);

const fetchProduct = async() => {
  if (props.category_id === undefined || props.id === undefined) {
    console.log('fetchProduct: category_id and(or) id is(are) are not defined(or)passed');
    return;
  }

  try {
    loading.value = true;
    const resp = await axiosClient.get(`/api/product/${props.category_id}/${props.id}`);
    product.value = resp.data;
    console.log(product.value);
  } catch (err) {
    console.log(err);
  } finally {
    loading.value = false;
  }
};

fetchProduct();
</script>

<style scoped></style>
