<template>
  <div class="container-fluid" >
  <Header />
  <main class="content d-flex align-items-center" style="margin-bottom=5%">
  <slot />
  </main>
  <div class="footer">
  <Footer/>
  </div>
  </div>
</template>

<script setup>
import Header from '@/layouts/Header.vue'
import Footer from '@/layouts/Footer.vue'

</script>

<style scoped>
.content {
    min-height: 90vh;
}

.footer {
  min-height: 5vh;
}
</style>