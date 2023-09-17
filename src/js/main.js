import '@/assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from '@/js/App.vue'
import router from '@/router'
import 'bootstrap/dist/css/bootstrap.css'

const app = createApp(App)

app.use(createPinia()).use(router).mount('#app')
