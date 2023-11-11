<template>
  <div class="container-fluid" >
  <Header />
  <main class="content">
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

<style scoped lang="scss">
$footer_height:5vh;
.content {
    min-height : calc(100vh - $footer_height);
}

.footer {
  min-height: $footer_height;
}
</style>