<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-auto">
        <slot name="sidebar" />
      </div>
      <div class="col-10">
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