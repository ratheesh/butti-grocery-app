<template>
  <div class="text-center my-5">
    <h1>Oops! You landed No where!</h1>
    <p>The page/resource that you ar looking is not present with us!</p>
    <router-link to="/"
      ><button class="btn btn-info" @click="gotoHome">Home Page</button></router-link
    >
  </div>
</template>

<script setup>
import router from "@/router";

const gotoHome = () => {
  router.push("/");
};
</script>

<style scoped></style>
