<template></template>

<script setup>
import { useAuthStore } from "@/stores/authstore.js";

const auth = useAuthStore();

const logout = async () => {
  try {
    const res = auth.logout();
    console.log(res);
    console.log("Logged Out");
  } catch (err) {
    console.log(err);
  }
};
</script>
