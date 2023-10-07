
import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useCartStore = defineStore('cartStore', () => {
  const items = ref([
    {
      id: 0,
      item: 'apples',
      quantity: 10,
      unit_price: 100,
    },
    {
      id: 1,
      item: 'banana',
      quantity: 3,
      unit_price: 100,
    },
    {
      id: 2,
      item: 'lemons',
      quantity: 10,
      unit_price: 10,
    },
    {
      id: 3,
      item: 'oranges',
      quantity: 3,
      unit_price: 50,
    },
  ]);

  return { items };
})