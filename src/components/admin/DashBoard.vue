<template>
  <div class="container-fluid">
    <h2 class="text-center mt-3">Dashboard</h2>
    <div class="row justify-content-end">
      <div class="col-auto me-5">
        <button class="btn btn-warning" @click="fetchData">
          <mdicon name="refresh" size="20" />
          Refresh
        </button>
      </div>
    </div>
    <div v-if="loading" class="row justify-content-center mt-5">
      <loading-indicator />
    </div>
    <div v-else class="row g-2">
      <div class="row col-12 justify-content-left m-auto g-2">
        <div class="col-2 d-flex g-3">
          <InfoPill :data="managers" />
        </div>
        <div class="col-2 d-flex g-3">
          <InfoPill :data="users" />
        </div>
        <div class="col-2 d-flex g-3">
          <InfoPill :data="categories" />
        </div>
        <div class="col-2 d-flex g-3">
          <InfoPill :data="products" />
        </div>
        <div class="col-2 d-flex g-3">
          <InfoPill :data="orders_total" />
        </div>
        <div class="col-2 d-flex g-3">
          <InfoPill :data="revenue_total" />
        </div>
      </div>
      <div class="row col-12 mt-3">
        <div class="col-4">
          <BarChart
            :title="ordersBarChartTitle"
            :labels="ordersBarChartLabels"
            :data="ordersBarChartData"
          />
        </div>
        <div class="col-4">
          <PieChart
            :title="categoryPieChartTitle"
            :labels="categoryPieChartLabels"
            :data="categoryPieChartData"
          />
        </div>
        <div class="col-4">
          <BarChart
            :title="revenueBarChartTitle"
            :labels="revenueBarChartLabels"
            :data="revenueBarChartData"
          />
        </div>
      </div>
    </div>
    <!-- <pre> data: {{ data }}</pre> -->
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import axiosClient from '@/js/axios.js'
import InfoPill from '@/components/InfoPill.vue'
import LoadingIndicator from '@/components/LoadingIndicator.vue'
import PieChart from '@/components/charts/PieChart.vue'
import BarChart from '@/components/charts/BarChart.vue'

const data = ref({})
const loading = ref(false)
const errorinfo = reactive({
  error: false,
  msg: ''
})

const ordersBarChartTitle = ref('')
const ordersBarChartLabels = ref([])
const ordersBarChartData = ref([])

const categoryPieChartTitle = ref('')
const categoryPieChartLabels = ref([])
const categoryPieChartData = ref([])

const revenueBarChartTitle = ref('')
const revenueBarChartLabels = ref([])
const revenueBarChartData = ref([])

const managers = {
  title: 'Managers',
  icon: 'account-multiple',
  color: 'text-primary',
  count: 0
}

const users = {
  title: 'Users',
  icon: 'account-multiple',
  color: 'text-primary',
  count: 0
}

const categories = reactive({
  title: 'Categories',
  icon: 'format-list-bulleted-type',
  color: 'text-secondary',
  count: 0
})

const products = reactive({
  title: 'Products',
  icon: 'format-list-bulleted-type',
  color: 'text-secondary',
  count: 0
})

const orders_total = reactive({
  title: 'Orders',
  icon: 'format-list-bulleted-type',
  color: 'text-secondary',
  count: 0
})

const revenue_total = reactive({
  title: 'Revenue',
  icon: 'format-list-bulleted-type',
  color: 'text-secondary',
  count: 0
})

const fetchData = async () => {
  loading.value = true
  try {
    const resp = await axiosClient.get('/admin')
    data.value = resp.data
    console.log(data.value)

    managers.count = data.value.managers
    users.count = data.value.users
    categories.count = data.value.category
    products.count = data.value.products
    orders_total.count = data.value.orders_total
    revenue_total.count = '₹' + (data.value.revenue_total ? data.value.revenue_total : '0') + '/-'

    // pie chart data for categories
    categoryPieChartTitle.value = 'Categories'
    categoryPieChartLabels.value = data.value.categories.map(function (el) {
      return el.name
    })
    categoryPieChartData.value = data.value.categories.map(function (el) {
      return el.count
    })

    // bar chart data for Orders
    ordersBarChartTitle.value = 'Orders'
    ordersBarChartLabels.value = data.value.orders.map(function (el) {
      return el.date
    })
    ordersBarChartData.value = data.value.orders.map(function (el) {
      return el.count
    })

    // bar chart data for revenue
    revenueBarChartTitle.value = 'Revenue'
    revenueBarChartLabels.value = data.value.revenue.map(function (el) {
      return el.date
    })
    revenueBarChartData.value = data.value.revenue.map(function (el) {
      return el.total
    })
  } catch (err) {
    console.log(err)
    if (err.response) {
      errorinfo.error = true
      errorinfo.msg = err.response.data
    } else {
      errorinfo.error = true
      errorinfo.msg = err.message
    }
  } finally {
    errorinfo.error = false
    errorinfo.msg = ''
    loading.value = false
  }
}

await fetchData()
</script>

<style scoped lang="scss"></style>
