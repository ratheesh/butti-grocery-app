import { ref, computed, onMounted } from 'vue'
import { defineStore } from 'pinia'

export const useCartStore = defineStore('cartStore', () => {
  const items = ref([])
  const total_amount = ref(0)

  onMounted(() => {
    items.value = JSON.parse(localStorage.getItem('cart') || '[]')
  })

  const updateItems = () => {
    console.log('updating items...')
    localStorage.setItem('cart', JSON.stringify(items.value))
    total_amount.value = computed(() =>
      items.value.reduce((y, x) => (y += x.quantity * x.unit_price), 0)
    )
  }

  return { items, updateItems, total_amount }
})
