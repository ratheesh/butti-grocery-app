<template>
<main-layout>
    <div class="container">
        <div class="text-center mt-3">
            <img :src="`${backend_base_url}/images/users/${auth.user.image_name}`" alt="User Profile Image" style="width:150px;height:150px;border:1px solid #808080;border-radius:50%" >
        </div>
        <div class="row my-3">
            <div class="col-8 border rounded-2 p-0 m-auto">
                <h2 class="text-center mt-3">{{  auth.user.name }}'s Profile</h2>
                <hr class="m-0">
                <table class="table table-borderless">
                    <tr>
                        <td class="text-end">
                            Name:
                        </td>
                        <td class="mx-3">
                            {{ auth.user.name }}
                        </td>
                    </tr>
                    <tr>
                        <td class="text-end">
                            User Name:
                        </td>
                        <td>
                            {{ auth.user.username }}
                        </td>
                    </tr>
                    <tr>
                        <td class="text-end">
                            E-Mail:
                        </td>
                        <td>
                            {{  auth.user.email }}
                        </td>
                    </tr>
                    <tr>
                        <td class="text-end">
                            Role:
                        </td>
                        <td>
                            {{ auth.user.role }}
                        </td>
                    </tr>
                    <tr>
                        <td class="text-end">
                            Status:
                        </td>
                        <td>
                            {{ auth.user.approved }}
                        </td>
                    </tr>
                    <tr>
                        <td class="text-end">
                            Created on:
                        </td>
                        <td>
                            {{ auth.user.created_timestamp }}
                        </td>
                    </tr>
                    <tr>
                        <td class="text-end">
                            Last updated on:
                        </td>
                        <td>
                            {{ auth.user.updated_timestamp }}
                        </td>
                    </tr>
                </table>
                <hr class="m-0">
                <div class="text-center my-3">
                  <button class="btn btn-sm btn-primary mx-2 align-center">
                    <b><mdicon name="shape-square-rounded-plus" class="text-white" :size="18"/></b>
                    Edit
                  </button>
                  <button class="btn btn-sm btn-secondary mx-2" @click="router.push('/')">
                    <b><mdicon name="home" class="text-black" :size="18"/></b>
                    Go Home
                    </button>
                </div>
            </div>
        </div> 
        <!-- <pre>{{ auth }}</pre> -->
    </div>
</main-layout>
</template>

<script setup>
import { onMounted } from 'vue';
import router from '@/router'
import { useAuthStore } from '@/stores/authstore'
import MainLayout from '@/layouts/MainLayout.vue'

const backend_base_url="http://localhost:5000"
const auth = useAuthStore()

onMounted(() => {
    if (auth.authenticated === false) {
        console.warn('User not authenticated')
        router.push({ name: 'login' })
    } else {
        console.log(auth.user)
    }
})

</script>

<style scoped>
table{
    table-layout: fixed;
}
</style>