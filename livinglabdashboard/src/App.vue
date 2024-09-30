<script setup>
import { useAuthStore } from "./stores/auth";
import { useRouter } from "vue-router";
import { ref, computed } from "vue";

const authStore = useAuthStore();
const router = useRouter();

// Berechne, ob der Benutzer eingeloggt ist
const isLoggedIn = computed(() => authStore.token !== "");

// Logout Funktion
const logout = () => {
  authStore.logout();
  router.push("/login");
};
</script>

<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>LivingLab Dashboard</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn v-if="isLoggedIn" @click="logout" color="error">Logout</v-btn>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<style scoped>
/* Styling kann hier hinzugefügt werden */
</style>
