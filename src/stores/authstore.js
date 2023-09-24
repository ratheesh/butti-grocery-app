import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('authStore', () => {
  const isAuthenticated = ref(0)
  const userRole = ref('user')

  async function login (username, password) {
    
  }

  return { isAuthenticated, userRole, login }
})
