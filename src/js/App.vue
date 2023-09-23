<template>
  <Header />
  <RouterView />
  <Footer />
</template>

<script setup>
import Header from "@/layouts/Header.vue";
import Footer from "@/layouts/Footer.vue";
import { RouterView } from "vue-router";
</script>

<style scoped></style>
