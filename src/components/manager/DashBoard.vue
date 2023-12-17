<template>
  <div class="container-fluid">
    <!-- <h2 class="text-center mt-3">Dashboard</h2> -->
    <div class="row justify-content-end">
      <div class="row d-flex justify-content-center" v-if="errorinfo.show">
        <div class="col-8 text-center">
          <div
            v-if="errorinfo.error"
            class="alert alert-danger alert-dismissible fade show"
            role="alert"
          >
            {{ errorinfo.msg }}
          </div>
          <div v-else class="alert alert-success alert-dismissible fade show" role="alert">
            {{ errorinfo.msg }}
          </div>
        </div>
      </div>
      <div class="col-auto me-5">
        <button class="btn btn-rosy-brown mx-2" @click="sendCSVReport">
          <span
            v-if="report_loading"
            class="spinner-border spinner-border-sm text-light"
            size="16"
          ></span>
          <span v-else> <mdicon name="email" size="20" /> </span>
          <span class="mx-2">Send Report</span>
        </button>
        <button class="btn btn-primary mx-2" @click="fetchData">
          <mdicon name="refresh" size="20" />
          <span class="mx-2">Refresh</span>
        </button>
      </div>
    </div>
    <div v-if="loading" class="row justify-content-center mt-5">
      <loading-indicator />
    </div>
    <div v-else class="row g-2">
      <div class="row col-12 justify-content-left m-auto g-2">
        <div class="col-2 d-flex g-3">
          <InfoPill :data="categories" />
        </div>
        <div class="col-2 d-flex g-3">
          <InfoPill :data="products" />
        </div>
        <div class="col-2 d-flex g-3">
          <InfoPill :data="orders_today" />
        </div>
        <div class="col-2 d-flex g-3">
          <InfoPill :data="revenue_today" />
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
import { useAuthStore } from '@/stores/authstore'
import InfoPill from '@/components/InfoPill.vue'
import LoadingIndicator from '@/components/LoadingIndicator.vue'
import PieChart from '@/components/charts/PieChart.vue'
import BarChart from '@/components/charts/BarChart.vue'

const data = ref({})
const loading = ref(false)
const report_loading = ref(false)
const errorinfo = reactive({
  show: false,
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

const orders_today = reactive({
  title: 'Orders Today',
  icon: 'format-list-bulleted-type',
  color: 'text-secondary',
  count: 0
})

const revenue_today = reactive({
  title: 'Revenue Today',
  icon: 'format-list-bulleted-type',
  color: 'text-secondary',
  count: 0
})

const auth = useAuthStore()
const sendCSVReport = async () => {
  errorinfo.show = false
  errorinfo.error = false
  errorinfo.msg = ''
  report_loading.value = true
  try {
    const formData = new FormData()
    if (auth.user) formData.append('username', auth.user.username)
    else {
      errorinfo.show = true
      errorinfo.error = true
      errorinfo.msg = 'User not logged in!'
      return
    }
    const resp = await axiosClient.post('/sendreport', formData)
    console.log(resp.data)
    errorinfo.show = true
    errorinfo.error = false
    errorinfo.msg = 'Report request sent successfully!'
  } catch (err) {
    console.log(err)
    errorinfo.show = true
    errorinfo.error = true
    errorinfo.msg = err.response
  } finally {
    report_loading.value = false
  }
}

const fetchData = async () => {
  errorinfo.show = false
  errorinfo.error = false
  errorinfo.msg = ''
  loading.value = true
  try {
    const resp = await axiosClient.get('/manager')
    data.value = resp.data
    console.log(data.value)

    categories.count = data.value.category
    products.count = data.value.products
    orders_today.count = data.value.orders_today
    revenue_today.count = '₹' + (data.value.revenue_today ? data.value.revenue_today : '0') + '/-'

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
    errorinfo.show = true
    if (err.response) {
      errorinfo.error = true
      errorinfo.msg = err.response.data
    } else {
      errorinfo.error = true
      errorinfo.msg = err.message
    }
  } finally {
    loading.value = false
  }
}

await fetchData()
</script>

<style scoped lang="scss"></style>
