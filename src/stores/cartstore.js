import { ref, onMounted } from 'vue'
import { defineStore } from 'pinia'

export const useCartStore = defineStore('cartStore', () => {
  const items = ref([])
  const delivery_info = ref({
    name: '',
    address: '',
    phone: '',
    delivery_date: ''
  })

  onMounted(() => {
    items.value = JSON.parse(localStorage.getItem('cart') || '[]')
  })

  const updateItems = () => {
    console.log('updating items...')
    localStorage.setItem('cart', JSON.stringify(items.value))
  }

  return { items, delivery_info, updateItems }
})
