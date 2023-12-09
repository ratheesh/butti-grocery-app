import axios from 'axios'
// import { useRouter } from 'vue-router'
import router from '@/router/index.js'
import { useAuthStore } from '@/stores/authstore.js'

const axiosClient = axios.create({
  baseURL: 'http://localhost:5000',
  withcredentials: true,
  headers: {
    common: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.getItem('access_token')}`
    }
  }
})

// Response interceptor
axiosClient.interceptors.response.use(
  (response) => {
    // console.log(response)
    return response
  },
  (error) => {
    // console.error(error)
    if (error.response.status === 401) {
      const auth = useAuthStore()
      console.log('invalid/expired token')
      auth.clearAuth()
      router.push('/login')
      return error
    }
    return Promise.reject(error)
  }
)

export default axiosClient
