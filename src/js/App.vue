<template>
  <div class="container-fluid vh-90 mb-5 px-0">
    <RouterView :key="$route.path"/>
  </div>
</template>

<script setup>
// import { onErrorCaptured } from 'vue';
import { RouterView } from "vue-router";

// onErrorCaptured ((e, instance, info) => {
//   console.log(e, instance, info)
// })
</script>

<style lang="scss">
  @import "@/assets/sass/main.scss";
</style>