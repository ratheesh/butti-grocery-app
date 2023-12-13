
<template>
    <div class="container">
        <div class="row col-8 justify-content-center align-items-baseline">
            <div class="card card-body border border-top-0 border-bottom-0 border-end-0 border-success-subtle border-5 m-0 p-0 py-3"
            style="width:10rem">
                <div class="row d-flex justify-content-center">
                    <div class="row d-flex align-items-center">
                        <mdicon class="col-auto" :name="icon" :size="30" :color="color" />
                        <span class="col-auto fw-bold fs-5 p-0">{{ title }}</span>
                        <span class="col-auto ms-2 fs-6 text-center">{{ data }}</span>
                    </div>
                </div>
            </div>
        </div>
        </div>
</template>

<script setup>
import { toRefs } from 'vue'

const props = defineProps({
    title: {
        type: String,
        required: true
    },
    icon: {
        type: String,
        required: true
    },
    color: {
        type: String,
        required: true
    },
    data: {
        type: String,
        required: true
    }
})

const { title, icon, color, data } = toRefs(props)
</script>