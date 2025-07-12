import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// Import Vuetify and its styles
import { createVuetify } from 'vuetify'
import 'vuetify/styles'

const vuetify = createVuetify({
    theme: {
        defaultTheme: 'dark',
    },
})

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(vuetify)  // Add Vuetify to the app

app.mount('#app')
