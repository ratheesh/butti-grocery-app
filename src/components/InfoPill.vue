<template>
  <div class="row col-8 justify-content-center align-items-baseline">
    <div
      class="card card-body border border-top-0 border-bottom-0 border-end-0 border-success-subtle border-5 m-0 p-0 py-3"
      style="width: 10rem"
    >
      <div class="row d-flex justify-content-center">
        <div class="row d-flex align-items-center">
          <mdicon class="col-auto" :name="props.data.icon" :size="25" :color="props.data.color" />
          <span class="col-auto fw-bold fs-6 p-0">{{ props.data.title }}</span>
          <span class="col-auto ms-2 fs-6 text-center">{{ props.data.count }}</span>
        </div>
      </div>
    </div>
  </div>
  <!-- <pre>{{ props }}</pre> -->
</template>

<script setup>
// import { toRef } from 'vue'

const props = defineProps({
  data: {
    type: Object,
    required: true
  }
})

// const { data } = toRef(props)
</script>
