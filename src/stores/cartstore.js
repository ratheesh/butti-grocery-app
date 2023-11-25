import { ref, reactive } from 'vue'
import { defineStore } from 'pinia'

export const useCartStore = defineStore('cartStore', () => {
  const items = ref([])
  const orderinfo = reactive({
    name: '',
    address: '',
    phone: '',
    email: '',
    payment_method: '',
    upi_address: ''
  })

  return { items, orderinfo }
})
