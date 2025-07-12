import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import viteVuetify from 'vite-plugin-vuetify' // Import the correct Vuetify plugin
import vueDevTools from 'vite-plugin-vue-devtools'
import { fileURLToPath, URL } from 'node:url'

export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
    viteVuetify(),  // Use the new Vuetify plugin
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})
