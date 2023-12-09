<template>
  <div class="container-fluid">
    <div class="row col-6 m-auto justify-content-center ">
      <div class="col-md-10">
        <h1 class="text-center fs-1 mt-5 ">Oops</h1>
        <h3 class="text-center"><b>You are not authorized to access this Page</b></h3>
        <div class="col-md-10">
          <div class="row justify-content-end ">
            <div class="col-auto"><a href="javascript:void(0)" class="btn btn-sm btn-primary mx-1" @click="goHome">Go Home</a></div>
            <div class="col-auto"><a href="javascript:void(0)" class="btn btn-sm btn-secondary mx-1" @click="logout">Logout</a></div>
          </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import router from '../router/index.js'
import { useAuthStore } from '../stores/authstore';

const auth = useAuthStore()

const goHome = () => {
  router.push('/')
}

const logout = () => {
  auth.logout()
}

</script>

<style scoped></style>