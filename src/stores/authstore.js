import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import axiosClient from '../js/axios';

export const useAuthStore = defineStore('authStore', () => {
  const authenticated = ref(false)
  const role = ref('user')
  const user = ref({})

  function setUser(_user) {
    console.log(_user)
    if (_user) {
      authenticated.value = true
      role.value = _user.role
      user.value = _user
    } else {
      authenticated.value = false;
      role.value = 'user'
      user.value = {}
    }
  }

  const getUser = computed(() => user.value)

  async function login(username, password) {
    try {
      const res = await axiosClient.post('/login', { username, password })
      console.log(res)
      if (res.data.error === 200) {
        authenticated.value = true
        role.value = res.data.user.role
        user.value = res.data.user
        console.log('Logged in!')
        return res
      } else {
        return res
      }
    } catch (err) {
      // console.log(err.response.status)
      // console.log(err.response.data)

      return err.response
      // console.log(err.response.data.error)
    }
  }

  async function logout() {
    try {
      const res = await axiosClient.post('/logout')
      console.log(res)
      authenticated.value = false
      role.value = 'user'
      user.value = {}
      console.log('logged out')
    } catch (err) {
      console.log(err)
    }
  }

  return { authenticated, role, user, setUser, getUser, login, logout }
})
