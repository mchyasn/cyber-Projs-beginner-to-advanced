<script setup lang="ts">
import { onMounted, ref } from "vue";
import type { Job } from "@/model/Job";
import { useAuth } from "@/composables/useAuth";
import JobList from "@/components/JobList.vue";
import { useJobServiceStore } from "@/stores/job.store";

const jobs = ref<Array<Job>>([]);
const auth = useAuth();

onMounted(async () => {
  await fetchJobs();
});

const store = useJobServiceStore();
async function fetchJobs() {
  const response = await store.getMyJobs(auth.getUserRoles()[0].toLowerCase());
  jobs.value = response;
}

const showUnassign = auth.getUserRoles()[0] === "COMPANY";
</script>

<template>
  <JobList :jobs="jobs" :can-beun-assigned="showUnassign" :can-open-chat="true" @refetch-jobs="fetchJobs" />
</template>

<style scoped>
</style>
