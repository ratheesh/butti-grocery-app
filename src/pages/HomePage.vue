<template>
  <main-layout>
  <div class="main text-center m-auto">
    <div class="container">
      <!-- <h1 class="text-center my-3">Products</h1> -->
      <div
        class="row row-cols-1 row-cols-sm-2 row-cols-md-3 rows-cols-lg-3 rows-cols-xl-4 row-cols-xxl-4 g-1"
      >
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
        <div class="col">
          <ProductCard />
        </div>
      </div>
    </div>
  </div>
  </main-layout>
</template>

<script setup>
import MainLayout from "@/layouts/MainLayout.vue";
import ProductCard from "@/components/ProductCard.vue";
</script>
