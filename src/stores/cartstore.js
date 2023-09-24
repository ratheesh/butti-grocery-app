
import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useCartStore = defineStore('cartStore', () => {
  const cart = ref([]);

  return { cart };
})