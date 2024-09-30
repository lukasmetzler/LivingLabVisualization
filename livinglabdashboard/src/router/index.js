import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Home from "../views/Home.vue";
import { useAuthStore } from "../stores/auth";

const routes = [
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/home",
    name: "Home",
    component: Home,
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore();
      if (!authStore.token) {
        next("/login");
      } else {
        next();
      }
    },
  },
  {
    path: "/:pathMatch(.*)*",
    redirect: "/login",
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
