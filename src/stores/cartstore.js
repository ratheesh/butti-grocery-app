
import { reactive } from 'vue';
import { defineStore } from 'pinia';

export const useCartStore = defineStore('cartStore', () => {
  const products = reactive([
    {
      id: 1,
      name: 'Product 1',
      desc: 'Description 1',
      price: 100,
      unit: 1,
      image: 'https://picsum.photos/200/300',
      quantity: 1,
    }
  ]);

  return { products };
})