<template>
  <div class="container-fluid" >
  <Header />
  <main class="align-items-center" style="margin-bottom=5%">
  <slot />
  </main>
  <Footer/>
  </div>
</template>

<script setup>
import Header from '@/layouts/Header.vue'
import Footer from '@/layouts/Footer.vue'

</script>

<style scoped></style>