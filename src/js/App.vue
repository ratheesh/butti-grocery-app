<template>
  <div class="container-fluid vh-90 mb-5 px-0">
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView } from "vue-router";
</script>

<style lang="scss">
  @import "@/assets/sass/main.scss";
</style>