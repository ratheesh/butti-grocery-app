<template>
  <div class="container-fluid m-0 p-0" >
  <Header />
  <main class="content">
  <slot />
  </main>
  <Footer/>
  </div>
</template>

<script setup>
import Header from '@/layouts/HeaderBar.vue'
import Footer from '@/layouts/FooterBar.vue'

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