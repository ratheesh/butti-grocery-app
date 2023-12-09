<template>
  <div class="container-fluid m-0 p-0" >
    <!-- <Header/> -->
    <main class="content d-flex align-items-center" style="margin-bottom=5%">
      <slot />
    </main>
    <!-- <Footer/> -->
  </div>
</template>

<script setup>
// import Header from '@/layouts/HeaderBar.vue'
// import Footer from '@/layouts/FooterBar.vue'
</script>

<style scoped>
.content {
    min-height: 90vh;
}

.footer {
  min-height: 5vh;
}
</style>