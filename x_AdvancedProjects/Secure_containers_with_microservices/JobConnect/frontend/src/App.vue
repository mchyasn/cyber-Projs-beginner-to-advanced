<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import {useAuth} from "@/composables/useAuth";
import {computed, onMounted, ref} from "vue";
import config from "@/config";

let loading = ref(true)

const auth = useAuth()

onMounted(async () => {
  await auth.init()
  loading.value = false
})

const filteredLinks = computed(() => {
  return [
    { to: '/', title: 'Home', show: true },
    { href: `${config.backendUrl}/api-docs`, title: 'API', show: true }, // Changed to 'href'
    {
      to: '/add',
      title: 'New Job',
      show: auth.getUserRoles()[0] === 'CUSTOMER'
    },
    {
      to: '/myjobs',
      title: 'My Jobs',
      show: auth.getUserRoles().length > 0
    },
    {
      to: '/alljobs',
      title: 'All Jobs',
      show: auth.getUserRoles()[0] === 'COMPANY'
    }
  ].filter(link => link.show);
});
</script>

<template>
  <v-app>
    <v-app-bar app flat color="background">
      <v-toolbar-title class="text-h6">JobConnect</v-toolbar-title>

      <v-spacer></v-spacer>

      <nav class="d-flex align-center">
        <v-btn
            v-for="link in filteredLinks"
            :key="link.to || link.href"
        :to="link.to"
        :href="link.href"
        variant="text"
        class="mx-1"
        exact
        >
        {{ link.title }}
        </v-btn>
      </nav>

      <v-spacer></v-spacer>

      <div class="d-flex align-center">
        <v-chip v-if="auth.state.authenticated" variant="outlined" class="mr-2">
          {{ auth.getUsername() }} ({{ auth.getUserRoles()[0] }})
        </v-chip>
        <v-btn
            :prepend-icon="auth.state.authenticated ? 'mdi-logout' : 'mdi-login'"
            variant="flat"
            @click="auth.state.authenticated ? auth.logout() : auth.login()"
        >
          {{ auth.state.authenticated ? 'Logout' : 'Login' }}
        </v-btn>
      </div>
    </v-app-bar>

    <v-main>
      <v-container>
        <router-view v-if="!loading" />
        <v-progress-circular v-else indeterminate></v-progress-circular>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped>
</style>