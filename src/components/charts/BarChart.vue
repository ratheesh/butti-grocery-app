<template>
    <div class="card shodow-sm">
        <div class="card-header">
            <h4 class="card-title text-center">{{ title }}</h4>
        </div>
        <div class="card-body">
            <div class="row">
                <Bar class="m-auto" :data="barChartData" :options="barChartOptions" />
            </div>
        </div>  
        <!-- <pre>{{ props }}</pre> -->
    </div>
</template>

<script setup>
import { toRefs, ref } from 'vue'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarController, CategoryScale, LinearScale, BarElement, ArcElement } from 'chart.js'

ChartJS.register( Title, Tooltip, Legend, BarController, CategoryScale, LinearScale, BarElement, ArcElement)

const props = defineProps({
    title: {
        type: String,
        required: true
    },
    labels: {
        type: Array,
        required: true
    },
    data: {
        type: Array,
        required: true
    }
})
const { title, labels, data } = toRefs(props)

const barChartData = ref({
  labels: labels.value,
  datasets: [
    {
      label: 'Data One',
      backgroundColor: '#f87979',
      data: data.value
    }
  ]
})

const barChartOptions = ref({
  responsive: true,
  maintainAspectRatio: false
})

</script>

<style scoped></style>