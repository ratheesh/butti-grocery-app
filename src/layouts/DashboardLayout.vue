<template>
  <div class="container-fluid m-0 p-0">
    <div class="row">
      <div v-if="user.approved" class="col-auto">
        <slot name="sidebar" />
      </div>
      <div class="col m-0 p-0 pe-2">
        <Header />
        <main class="content">
          <slot name="default" />
        </main>
        <Footer />
      </div>
    </div>
  </div>
</template>

<script setup>
import { storeToRefs } from 'pinia'
import Header from '@/layouts/HeaderBar.vue'
import Footer from '@/layouts/FooterBar.vue'
import { useAuthStore } from '../stores/authstore'

const auth = useAuthStore()
const { user } = storeToRefs(auth) || { approved: false }
</script>

<style lang="scss"></style>
