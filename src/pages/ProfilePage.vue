<template>
  <main-layout>
      <div class="container">
          <div v-if="loading">
            <loading-indicator></loading-indicator>
          </div>
          <div v-else>
              <div class="text-center mt-3">
                  <img :src="`data:image/png;base64, ${user.image}`" alt="User Profile Image" style="width:150px;height:150px;border:1px solid #808080;border-radius:50%" >
              </div>
              <div class="row my-3">
                  <div class="col-8 border rounded-2 p-0 m-auto">
                      <h2 class="text-center mt-3">{{ user.name }}'s Profile</h2>
                      <hr class="m-0">
                      <table class="table table-borderless">
                          <tr>
                              <td class="text-end fw-bolder"> Name </td>
                              <td class="mx-3"> {{ user.name }} </td>
                          </tr>
                          <tr>
                              <td class="text-end fw-bolder"> User Name </td>
                              <td> {{ user.username }} </td>
                          </tr>
                          <tr>
                              <td class="text-end fw-bolder"> E-Mail </td>
                              <td> {{ user.email }} </td>
                          </tr>
                          <tr>
                              <td class="text-end fw-bolder"> Role </td>
                              <td> {{ user.role }} </td>
                          </tr>
                          <tr>
                              <td class="text-end fw-bolder"> Status </td>
                              <td> {{ accountStatus(user.approved) }} </td>
                          </tr>
                          <tr>
                              <td class="text-end fw-bolder "> Created on </td>
                              <td> {{ user.created_timestamp }} </td>
                          </tr>
                          <tr>
                              <td class="text-end fw-bolder"> Last updated on </td>
                              <td> {{ user.updated_timestamp }} </td>
                          </tr>
                      </table>
                      <hr class="m-0">
                      <div class="text-center my-3">
                        <button class="btn btn-sm btn-primary mx-2 d-inline-flex align-items-center ">
                          <b><mdicon name="shape-square-rounded-plus" class="text-white" :size="18"/></b>
                          <span>Edit</span>
                        </button>
                        <button class="btn btn-sm btn-secondary mx-2" @click="router.push('/')">
                          <b><mdicon name="home" class="text-black" :size="18"/></b>
                          Go Home
                          </button>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </main-layout>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import router from '@/router'
import axiosClient from '@/js/axios.js'
import { useAuthStore } from '@/stores/authstore'
import MainLayout from '@/layouts/MainLayout.vue'
import LoadingIndicator from '@/components/LoadingIndicator.vue'

const auth = useAuthStore()
const loading = ref(true)
const user = ref({})

onMounted(async() => {
    if (auth.authenticated === false) {
        console.warn('User not authenticated')
        router.push({ name: 'login' })
    }
})

const fetchUser = async() => {
    if (auth.user) {
        loading.value = true
        try {
            const resp = await axiosClient.get(`/api/user/${auth.user.username}`)
            console.log(resp)
            user.value = resp.data
        } catch(err) {
            console.log(err)
        } finally {
            loading.value = false
        }
    }
}

const accountStatus = (status) => {
  if (status === true) {
    return 'Approved'
  } else {
    return 'Pending'
  }
}

fetchUser()
</script>

<style scoped>
table{
    table-layout: fixed;
}

td {
    padding: 0.75em;
}
</style>