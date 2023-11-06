import '@/assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from '@/js/App.vue'
import router from '@/router'
// import 'bootstrap/dist/css/bootstrap.min.css'
// import 'bootstrap/dist/js/bootstrap.min.js'
// import 'bootstrap'

import mdiVue from 'mdi-vue/v3'
import * as mdijs from '@mdi/js'

const app = createApp(App)
app.use(createPinia()).use(router).use(mdiVue, { icons: mdijs }).mount('#app')
