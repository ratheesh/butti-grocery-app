import { ref, computed, onMounted } from 'vue'
import { defineStore } from 'pinia'

export const useCartStore = defineStore('cartStore', () => {
  const items = ref([])
  const total = ref(0)

  onMounted(() => {
    items.value = JSON.parse(localStorage.getItem('cart') || '[]')
    total.value = computed(() => items.value.reduce((y, x) => (y += x.quantity * x.unit_price), 0))
  })

  function clear() {
    items.value = []
    total.value = 0
    localStorage.setItem('cart', JSON.stringify(items.value))
  }

  function update() {
    // console.log('updating items...')
    localStorage.setItem('cart', JSON.stringify(items.value))
    // console.log('total:', total.value)
  }

  const totalAmount = computed(() =>
    items.value.reduce((y, x) => (y += x.quantity * x.unit_price), 0)
  )

  return { items, update, clear, totalAmount }
})
