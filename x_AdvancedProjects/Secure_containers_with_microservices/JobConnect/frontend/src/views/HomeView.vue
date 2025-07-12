<script setup lang="ts">
import {useAuth} from "@/composables/useAuth";
import {useRouter} from "vue-router";

const auth = useAuth();
const router = useRouter()

function handleClick() {
  if (!auth.state.authenticated) {
    auth.login();
    return;
  }

  const roles = auth.getUserRoles();
  if (roles[0] === "CUSTOMER") {
    router.push("/add");
  } else if (roles[0] === "COMPANY") {
    router.push("/alljobs");
  }
}

</script>

<template>
  <v-container class="pa-6">
    <v-row class="text-center mb-12">
      <v-col cols="12">
        <h1 class="text-h3 font-weight-bold primary--text mb-4">
          JobConnect Platform
        </h1>
        <p class="text-h6 text-secondary">
          Connecting Ordinary People with Skilled Professionals
        </p>
      </v-col>
    </v-row>

    <v-row class="mb-12">
      <v-col cols="12" md="6" class="d-flex align-center">
        <div>
          <h2 class="text-h4 mb-4">About Our Service</h2>
          <p class="text-body-1">
            JobConnect is a professional platform that bridges the gap between customers needing services
            and qualified companies. Our system provides seamless job posting, intelligent matching,
            and secure communication tools.
          </p>
        </div>
      </v-col>
      <v-col cols="12" md="6">
        <v-img
            src="@/assets/connected-world.svg"
            height="300"
            contain
            class="rounded-lg"
        />
      </v-col>
    </v-row>

    <v-row class="mb-12">
      <v-col cols="12">
        <h2 class="text-h4 text-center mb-6">Key Features</h2>
        <v-row>
          <v-col cols="12" md="4">
            <v-card class="pa-4" elevation="2">
              <v-icon color="primary" size="64" class="mb-4">mdi-briefcase-upload</v-icon>
              <h3 class="text-h6 mb-2">Job Management</h3>
              <p class="text-body-2">
                Create, track, and manage job postings with dynamic categories and subcategories
              </p>
            </v-card>
          </v-col>

          <v-col cols="12" md="4">
            <v-card class="pa-4" elevation="2">
              <v-icon color="primary" size="64" class="mb-4">mdi-shield-account</v-icon>
              <h3 class="text-h6 mb-2">Secure Matching</h3>
              <p class="text-body-2">
                Role-based access control ensures proper job assignments and communications
              </p>
            </v-card>
          </v-col>

          <v-col cols="12" md="4">
            <v-card class="pa-4" elevation="2">
              <v-icon color="primary" size="64" class="mb-4">mdi-message-processing</v-icon>
              <h3 class="text-h6 mb-2">Real-time Chat</h3>
              <p class="text-body-2">
                Integrated chat system for direct communication between parties
              </p>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <v-row class="mb-12">
      <v-col cols="12">
        <div class="text-center py-12 primary lighten-5 rounded-lg">
          <h2 class="text-h4 mb-4">How It Works</h2>
          <v-row class="justify-center">
            <v-col cols="12" md="3" v-for="(step, i) in [1, 2, 3]" :key="step">
              <v-avatar size="64" color="primary" class="mb-4">
                <span class="text-h4 white--text">{{ step }}</span>
              </v-avatar>
              <p class="text-body-1" v-if="step === 1">
                Post your job with details and requirements
              </p>
              <p class="text-body-1" v-if="step === 2">
                Companies review and claim suitable jobs
              </p>
              <p class="text-body-1" v-if="step === 3">
                Collaborate and complete through our platform
              </p>
            </v-col>
          </v-row>
        </div>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" class="text-center">
        <v-btn
            color="primary"
            size="x-large"
            class="mb-4"
            @click="handleClick"
        >
          Get Started
        </v-btn>
        <p class="text-caption text-secondary">
          Join hundreds of satisfied customers and professionals
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.v-avatar {
  transition: transform 0.3s ease;
}

.v-avatar:hover {
  transform: scale(1.1);
}

.v-card {
  transition: all 0.3s ease;
  min-height: 250px;
}

.v-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15) !important;
}
</style>