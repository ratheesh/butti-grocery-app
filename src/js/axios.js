import axios from 'axios'
// import { useRouter } from 'vue-router'
import router from '@/router/index.js'

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

// const router = useRouter()

// Response interceptor
axiosClient.interceptors.response.use(
  (response) => {
    // Handle the response here
    // console.log('hello in response')
    // console.log(response)
    return response
  },
  (error) => {
    // Handle errors here
    // console.log('hello in error')
    // console.error(error)
    if (error.response.status === 401) {
      console.log('invalid/expired token')
      router.push('/login')
    }
    return Promise.reject(error)
  }
)

export default axiosClient
