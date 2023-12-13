<template>
  <div class="container-fluid">
    <h2 class="text-center mt-3">Dashboard</h2>
    <div class="row g-2">
      <div class="row col-12 justify-content-center m-auto g-2">
        <div class="col-4 d-flex g-3">
          <InfoPill :title="users.title" :icon="users.icon" :color="users.color" :data="users.data"/>
        </div>
        <div class="col-4 d-flex g-3">
          <InfoPill :title="categories.title" :icon="categories.icon" :color="categories.color" :data="categories.data"/>
        </div>
        <div class="col-4 d-flex g-3">
          <InfoPill :title="products.title" :icon="products.icon" :color="products.color" :data="products.data"/>
        </div>
      </div>
      <div class="row colo-6 mt-3">
        <div class="col-6">
          <div class="card card-body shadow-sm">
            <Bar :data="barChartData" :options="barChartOptions"/>
          </div>
        </div>
        <div class="col-6">
          <div class="card card-body shadow-sm" style="height:60vh;width:40vw">
            <Pie :data="pieChartData" :options="pieChartOptions"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Bar, Pie } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarController, CategoryScale, LinearScale, BarElement, ArcElement } from 'chart.js'
import InfoPill from '@/components/InfoPill.vue'

ChartJS.register(Title, Tooltip, Legend, BarController, CategoryScale, LinearScale, BarElement, ArcElement)
const barChartData = ref({
  labels: ['13/12', '12/12', '11/12', '10/12', '09/12', '08/12', '07/12'],
  datasets: [
    {
      label: 'Data One',
      backgroundColor: '#f87979',
      data: [35, 20, 12, 39, 10, 65, 39]
    }
  ]
})

const barChartOptions = ref({
  responsive: true,
  maintainAspectRatio: false
})

const pieChartData = ref({
  labels: ['Fruits', 'Vegetables', 'Meat', 'Fish'],
  datasets: [
    {
      backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
      data: [40, 20, 40, 10]
    }
  ]
})

const pieChartOptions = ref({
  responsive: true,
  maintainAspectRatio: false
})

const users = {
  title: 'Users',
  icon: 'account-multiple',
  color: 'text-primary',
  data: "20"
}

const categories = {
  title: 'Categories',
  icon: 'format-list-bulleted-type',
  color: 'text-secondary',
  data: "10"
}

const products = {
  title: 'Products',
  icon: 'format-list-bulleted-type',
  color: 'text-secondary',
  data: "30"
}
</script>

<style scoped lang="scss"></style>
