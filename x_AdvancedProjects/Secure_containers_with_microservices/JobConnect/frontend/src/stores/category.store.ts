import {defineStore} from "pinia";
import {useAuth} from "@/composables/useAuth";
import config from "@/config";
import type {Job} from "@/model/Job";

export const useCategoryService = defineStore('category', () => {
    const auth = useAuth();
    const baseUrl = `${config.backendUrl}/categories`;

    async function getCategories() {
        return  await auth.authorizedRequest(`${baseUrl}`, "GET");
    }

    async function getSubcategories(selectedCategoryIds: string[]) {
        return  await auth.authorizedRequest(`${config.backendUrl}/categories`, "POST", {
            data: { categories: selectedCategoryIds },
        });
    }

    return {getCategories, getSubcategories};
})
  