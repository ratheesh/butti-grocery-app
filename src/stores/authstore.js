import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import axiosClient from '../js/axios'

export const useAuthStore = defineStore('authStore', () => {
  const authenticated = ref(localStorage.getItem('access_token'))
  const user = ref(localStorage.getItem('user'))

  function setUser(_user) {
    console.log(_user)
    if (_user) {
      authenticated.value = true
      user.value = _user
    } else {
      authenticated.value = false
      user.value = {}
    }
  }

  const getUser = computed(() => user.value)

  const fetchUser = async (username) => {
    try {
      const res = await axiosClient.post(`/api/user/${username}`)
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
        localStorage.setItem('user', res.data.user)
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
    localStorage.removeItem('access_token')
    localStorage.removeItem('user')
    console.log('logged out')
    authenticated.value = false
  }

  async function signup(user_data) {
    try {
      const res = await axiosClient.post('/api/user', {
        name: user_data.name,
        username: user_data.username,
        email: user_data.email,
        role: user_data.role,
        password: user_data.password,
        image_name: 'default.png',
        image: null
      })
      console.log(res)
      if (res.data.status === 201) console.log(`user ${user_data.username} signed up!`)

      return res
    } catch (err) {
      console.log(err)
      return err
    }
  }
  return { authenticated, user, setUser, getUser, login, logout, signup, fetchUser }
})
