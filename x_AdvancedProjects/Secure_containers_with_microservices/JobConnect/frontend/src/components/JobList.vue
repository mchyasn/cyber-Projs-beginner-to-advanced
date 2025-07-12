<template>
  <v-container class="mt-4">
    <div v-for="(job, index) in jobs" :key="index" class="mb-4">
      <v-card>
        <v-card-title>
          {{ job.title }}
        </v-card-title>
        <v-card-subtitle>
          Category: {{ job.categories.join(', ') }}
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="primary" @click="viewJobDetails(job)">
            View Details
          </v-btn>
          <v-btn
              v-if="auth.getUserEmail() == job.customerEmail"
              color="error"
              @click="confirmDelete(job)"
          >
            Delete
          </v-btn>
        </v-card-actions>
      </v-card>
    </div>

    <v-dialog v-model="deleteDialogVisible" max-width="500px">
      <v-card>
        <v-card-title class="text-h5">Delete Job?</v-card-title>
        <v-card-text>
          Are you sure you want to permanently delete this job? This action cannot be undone.
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="deleteDialogVisible = false">Cancel</v-btn>
          <v-btn color="error" @click="handleDelete">Delete</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="isJobDialogOpen" max-width="600px">
      <v-card>
        <v-card-title>
          Job Details
          <v-spacer/>
        </v-card-title>
        <v-card-text>
          <div v-if="selectedJob?.title"><strong>Title:</strong> {{ selectedJob?.title }}</div>
          <div v-if="selectedJob?.customerEmail"><strong>Customer email:</strong> {{ selectedJob?.customerEmail }}</div>
          <div v-if="selectedJob?.companyEmail"><strong>Assigned company email:</strong> {{ selectedJob?.companyEmail }}
          </div>
          <div v-if="selectedJob?.description"><strong>Description:</strong> {{ selectedJob?.description }}</div>
          <div v-if="selectedJob?.categories"><strong>Category:</strong> {{ selectedJob?.categories.join(', ') }}</div>
          <div v-if="selectedJob?.subcategories"><strong>Subcategories:</strong>
            {{ selectedJob?.subcategories.join(', ') }}
          </div>
          <div v-if="selectedJob?.budget"><strong>Budget:</strong> ${{ selectedJob?.budget }}</div>
          <div v-if="selectedJob?.images && selectedJob.images.length">
          </div>

          <!-- Display Images -->
          <div v-if="images.length">
            <strong>Job Images:</strong>
            <v-row>
              <v-col
                  v-for="(image, index) in images"
                  :key="index"
                  cols="12"
                  md="4"
                  sm="6"
              >
                <a :href="image" rel="noopener noreferrer" target="_blank">
                  <v-img
                      :src="image"
                      aspect-ratio="1"
                      class="grey lighten-2"
                  ></v-img>
                </a>
              </v-col>
            </v-row>
          </div>

          <v-btn v-if="canBeAssigned" @click="assignJob(selectedJob?._id ?? '')">
            ASSIGN
          </v-btn>
          <v-btn v-if="canBeunAssigned" @click="unassignJob(selectedJob?._id ?? '')">
            UNASSIGN
          </v-btn>

          <div v-if="canOpenChat">
            <div class="chat-container mt-4">
              <h4>Chat</h4>
              <div v-if="chatMessages.length" class="chat-messages">
                <div v-for="(msg, index) in chatMessages" :key="index" class="chat-message">
                  <strong>{{ msg.sender }}:</strong> {{ msg.message }}
                </div>
              </div>
              <div v-else>No messages yet.</div>
            </div>

            <!-- Chat Input -->
            <v-text-field
                v-model="currentMessage"
                class="mt-2"
                label="Type a message..."
                @keyup.enter="sendMessage"
            ></v-text-field>
            <v-btn color="primary" @click="sendMessage">
              Send
            </v-btn>
          </div>
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="isJobDialogOpen = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>


<script lang="ts" setup>
import {onUnmounted, ref, watch} from "vue";
import type {Job} from "@/model/Job";
import {useAuth} from "@/composables/useAuth";
import {useChatService} from "@/composables/useChatService";
import {useJobServiceStore} from "@/stores/job.store";

const props = defineProps({
  jobs: {
    type: Array as () => Array<Job>,
    required: true,
  },
  canBeAssigned: {
    type: Boolean,
    required: false,
    default: false,
  },
  canBeunAssigned: {
    type: Boolean,
    required: false,
    default: false,
  },
  canOpenChat: {
    type: Boolean,
    required: false,
    default: false,
  }
});

const emit = defineEmits(["refetch-jobs"]);
const deleteDialogVisible = ref(false);
const jobToDelete = ref<Job | null>(null);

const confirmDelete = (job: Job) => {
  jobToDelete.value = job;
  deleteDialogVisible.value = true;
};

const handleDelete = () => {
  if (jobToDelete.value?._id) {
    deleteJob(jobToDelete.value._id);
    deleteDialogVisible.value = false;
  }
};

const deleteJob = async (id: string) => {
  await jobService.deleteJob(id);
  emit("refetch-jobs");
}
const isJobDialogOpen = ref(false);
const selectedJob = ref<Job | null>(null);
const auth = useAuth();
const chatService = useChatService();
const images = ref<string[]>([]);
const chatMessages = ref<{ sender: string; message: string }[]>([]);
const currentMessage = ref("");
const jobService = useJobServiceStore();
const viewJobDetails = async (job: Job) => {
  selectedJob.value = job;
  if (selectedJob.value?._id) {
    loadImages(selectedJob.value._id);
  }
  isJobDialogOpen.value = true;

  if (selectedJob.value?._id) {
    if (props.canOpenChat) {
      chatService.init();
      chatService.joinRoom(selectedJob.value._id);
    }
    chatService.onMessage((data) => {
      if (chatService.getClientId() == data.sender) {
        data.sender = "ME";
      } else {
        data.sender = auth.getUserRoles()[0] == "CUSTOMER" ? "COMPANY" : "CUSTOMER";
      }
      chatMessages.value.push(data);
    });
  }
};

const loadImages = async (id: string) => {
  try {
    let imagesRemote = await jobService.getImages(id);
    images.value = imagesRemote;
  } catch (err) {
    console.log("No images found");
  }
}

const assignJob = async (id: string) => {
  if (id.length === 24) {
    await jobService.assignJob(id);
    emit("refetch-jobs");
    isJobDialogOpen.value = false;
  }
};


const unassignJob = async (id: string) => {
  if (id.length === 24) {
    await jobService.unassignJob(id);
    emit("refetch-jobs");
    isJobDialogOpen.value = false;
  }
};

const sendMessage = () => {
  if (currentMessage.value.trim() && selectedJob.value?._id) {
    chatService.sendMessage(selectedJob.value._id, currentMessage.value.trim());
    currentMessage.value = "";
  }
};


onUnmounted(() => {
  if (props.canOpenChat) {
    chatService.disconnect();
  }
});

watch(isJobDialogOpen, (isOpen) => {
  if (!isOpen) {
    chatMessages.value = [];
    chatService.disconnect();
  }
});
</script>
