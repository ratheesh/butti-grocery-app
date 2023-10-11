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
      // console.log(res)
      if (res.status === 200) {
        authenticated.value = true
        role.value = res.data.user.role
        user.value = res.data.user
        localStorage.setItem('access_token', JSON.stringify(res.data.access_token))
        console.log('Logged in!')
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
    console.log('logged out')
    authenticated.value = false
    // try {
    //   const res = await axiosClient.post('/logout')
    //   console.log(res)
    //   authenticated.value = false
    //   role.value = 'user'
    //   user.value = {}
    //   console.log('logged out')
    // } catch (err) {
    //   console.log(err)
    // }
  }

  async function signup(user_data) {
    try {
      const res = await axiosClient.post('/api/user',{
        name: user_data.name,
        username: user_data.username,
        email: user_data.email,
        role: user_data.role,
        password: user_data.password,
        image : user_data.image
      })
      console.log(res)
      if (res.data.status === 201)
        console.log(`user ${user_data.username} signed up!`)

      return res
    } catch (err) {
      console.log(err)
      return err
    }
  }
  return { authenticated, role, user, setUser, getUser, login, logout, signup }
})
