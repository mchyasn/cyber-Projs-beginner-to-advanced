import { createRouter, createWebHistory } from 'vue-router'
import LoginCallbackView from '../views/LoginCallbackView.vue'
import AddJobView from "@/views/AddJobView.vue";
import ListOfMyJobsView from "@/views/ListOfMyJobsView.vue";
import ListOfAllJobsView from "@/views/ListOfAllJobsView.vue";
import HomeView from "@/views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      component: HomeView,
    },
    {
      path: '/add',
      name: 'addjob',
      component: AddJobView,
    },
    {
      path: '/myjobs',
      name: 'myjobs',
      component: ListOfMyJobsView,
    },
    {
      path: '/alljobs',
      name: 'alljobs',
      component: ListOfAllJobsView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/login-callback',
      name: 'login-callback',
      component: LoginCallbackView,
    }
  ],
})

export default router
