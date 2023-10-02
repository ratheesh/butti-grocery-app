<template>
  <div class="container-fluid vh-90 mb-5">
    <Header />
    <RouterView />
    <Footer />
  </div>
</template>

<script setup>
import Header from "@/layouts/Header.vue";
import Footer from "@/layouts/Footer.vue";
import { RouterView } from "vue-router";
</script>

<style scoped></style>
