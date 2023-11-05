<template>
<main-layout>
    <div class="container">
        <div class="row my-5">
            <div class="col-10 border rounded-2 p-0">
                <!-- <img :src="`${backend_base_url}/${auth.user.img_file}`" alt="User Profile Image" \> -->
                <h2 class="text-center mt-3">{{  auth.user.name }}'s Page</h2>
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
                    <button class="btn btn-primary">Edit</button>
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <button class="btn btn-secondary" @click="router.push('/')">Go Home</button>
                </div>
            </div>
        </div> 
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