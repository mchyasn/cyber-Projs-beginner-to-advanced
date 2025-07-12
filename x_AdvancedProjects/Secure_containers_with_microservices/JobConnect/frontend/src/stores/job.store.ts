import {defineStore} from "pinia";
import {ref} from "vue";
import {useAuth} from "@/composables/useAuth";
import config from "@/config";
import type {Job} from "@/model/Job";


export const useJobServiceStore = defineStore('job', () => {
    const isLoading = ref(true);
    const auth = useAuth();
    const baseUrl = `${config.backendUrl}/jobs`;

    // Fetch all jobs
    async function getAllJobs() {
        return auth.authorizedRequest(`${baseUrl}/`, "GET");
    }

    // Post a new job
    async function postJob(job: Job) {
        return auth.authorizedRequest(`${baseUrl}/`, "POST", { data: job });
    }
    async function assignJob(id: string) {
        return await auth.authorizedRequest(`${config.backendUrl}/jobs/assign/${id}`, "PUT");
    }

    async function unassignJob(id: string) {
        return await auth.authorizedRequest(`${config.backendUrl}/jobs/unassign/${id}`, "PUT");
    }

    async function search(searchText: string, selectedFields: string[]) {
        return await auth.authorizedRequest(`${config.backendUrl}/jobs/search`, "POST", {data: {text: searchText, fields: selectedFields}});

    }

    async function deleteJob(id: string) {
        return await auth.authorizedRequest(`${config.backendUrl}/jobs/${id}`, "DELETE");
    }

    // Post images to job
    async function postImages(jobId: string, images: FormData) {
        const newFormData = new FormData();
        newFormData.append('jobId', jobId);

        for (let [key, value] of images.entries()) {
            if (key !== 'jobId') {
                newFormData.append(key, value);
            }
        }

        const response = auth.authorizedRequest(`${config.imagesUrl}/image`, "POST",{
            data: newFormData
        });

        return response;
    }


    async function getImages(jobId: string){
        return await auth.authorizedRequest(`${config.imagesUrl}/image/${jobId}`, "GET");
    }

    // Fetch jobs based on a specific role
    async function getMyJobs(role: string) {
        return auth.authorizedRequest(`${baseUrl}/${role.toLowerCase()}`, "GET");
    }

    return { isLoading, getAllJobs, postJob, getMyJobs,postImages,getImages,assignJob,unassignJob,search,deleteJob };
});
