<template>
  <div class="card" style="width: 20rem;">
  <div class="card-body">
    <h5 class="card-title text-center">{{ props.category.name }}</h5>
    <div class="d-flex justify-content-around">
        <button class="btn btn-sm btn-outline-success">Manage</button>
        <button class="btn btn-sm btn-outline-info">Edit</button>
        <button class="btn btn-sm btn-outline-danger">Delete</button>
    </div>
  </div>
</div> 
</template>

<script setup>
const props = defineProps({
  category: {
    name: {
        type: String,
        required: true,
    },
    id: {
        type: Number,
        required: true,
    },
    created_timestamp: {
        type: String,
        required: true,
    },
  },
  edit: {
    type: Boolean,
    default: false,
  }
})
</script>

<style scoped></style>