<template>
  <h2 class="text-center my-3">Product Page</h2>
  <p>Passed parameter: {{ props.id }}</p>
</template>

<script setup>
const props = defineProps({
  id: {
    type: String,
    required: true,
  },
});
</script>

<style scoped></style>
