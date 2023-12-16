import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axiosClient from '../js/axios'

export const useAuthStore = defineStore('authStore', () => {
  axiosClient.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem(
    'access_token'
  )}`

  const router = useRouter()

  // variables
  const authenticated = ref(!!localStorage.getItem('access_token'))
  // const user = ref(JSON.parse(localStorage.getItem('user')) || defaultUser)
  const user = ref({})

  // functions
  function setUser(_user) {
    if (_user) {
      user.value = _user
    } else {
      user.value = {}
    }
  }

  const clearAuth = () => {
    user.value = {}
    authenticated.value = false
    localStorage.removeItem('user')
    localStorage.removeItem('access_token')
    axiosClient.defaults.headers.common['Authorization'] = `Bearer None`
  }

  const getUser = computed(() => user.value)

  const fetchUser = async (username) => {
    console.log('fetching user')
    try {
      const res = await axiosClient.get(`/api/user/${username}`)
      if (res.status === 200) {
        authenticated.value = true
        user.value = res.data.user
        return res
      } else {
        return res
      }
    } catch (err) {
      return err.response
    }
  }

  async function login(username, password) {
    try {
      const res = await axiosClient.post('/login', { username, password })
      // console.log(res)
      if (res.status === 200) {
        authenticated.value = true
        user.value = res.data.user
        localStorage.setItem('access_token', res.data.access_token)
        localStorage.setItem('user', JSON.stringify(res.data.user))
        // setUser('user', user.value)
        axiosClient.defaults.headers.common['Authorization'] = `Bearer ${res.data.access_token}`
        // console.log('Logged in!')
        return res
      } else {
        return res
      }
    } catch (err) {
      return err.response
    }
  }

  async function logout() {
    clearAuth()
    console.log('logged out')
    router.push('/login')
  }

  return { authenticated, user, setUser, getUser, login, logout, fetchUser, clearAuth }
})
