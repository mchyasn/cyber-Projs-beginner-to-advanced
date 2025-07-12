<template>
  <v-container class="fill-height">
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-card class="pa-6">
          <v-card-title class="text-h5 mb-4">Authentication Status</v-card-title>


          <v-alert
              v-if="auth.state.authenticated"
              type="success"
              variant="tonal"
              class="mb-4"
          >
            Welcome back, {{ auth.getUsername() }}!
          </v-alert>

          <v-btn
              block
              color="primary"
              to="/"
              prepend-icon="mdi-home"
          >
            Return to Homepage
          </v-btn>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { useAuth } from '@/composables/useAuth';
import { onMounted } from 'vue';

const auth = useAuth();

onMounted(async () => {
  const currentUrl = window.location.href;
  await auth.handleCallback(currentUrl);
});
</script>
