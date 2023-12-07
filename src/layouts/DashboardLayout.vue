<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-2">
        <slot name="sidebar" />
      </div>
      <div class="col-10 m-0 p-0 pe-2">
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
import Header from "@/layouts/Header.vue";
import Footer from "@/layouts/Footer.vue";
// import UserManagement from "@/components/UserManagement.vue";
// import SideBar from "@/layouts/SideBar.vue";
</script>

<style lang="scss"></style>