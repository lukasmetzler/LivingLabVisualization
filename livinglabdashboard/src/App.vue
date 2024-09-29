<template>
  <v-app>
    <v-app-bar app>
      <v-img
        src="/vite.svg"
        alt="Vite Logo"
        max-width="50"
        class="mr-2"
      ></v-img>
      <v-img
        src="./assets/vue.svg"
        alt="Vue Logo"
        max-width="50"
        class="mr-4"
      ></v-img>
      <v-toolbar-title>LivingLab Dashboard</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text to="/">Home</v-btn>
      <v-btn text to="/login">Login</v-btn>
      <v-btn text to="/dashboard">Dashboard</v-btn>
      <v-btn text @click="logout" v-if="isAuthenticated">Logout</v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { useAuthStore } from "./stores/auth";
import { useRouter } from "vue-router";
import { computed } from "vue";

const authStore = useAuthStore();
const router = useRouter();

const logout = () => {
  authStore.logout();
  router.push("/login");
};

const isAuthenticated = computed(() => !!authStore.token);
</script>

<style>
/* Optional globale Stile */
</style>
