<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-title>Login</v-card-title>
          <v-card-text>
            <v-form @submit.prevent="login">
              <v-text-field
                v-model="email"
                label="Email"
                required
              ></v-text-field>
              <v-text-field
                v-model="password"
                label="Passwort"
                type="password"
                required
              ></v-text-field>
              <v-btn type="submit" color="primary">Einloggen</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { useAuthStore } from "../stores/auth";
import { useRouter } from "vue-router";
import { ref } from "vue";

const authStore = useAuthStore();
const router = useRouter();

const email = ref("");
const password = ref("");

const login = async () => {
  try {
    await authStore.login(email.value, password.value);
    router.push("/home");
  } catch (error) {
    console.error("Login fehlgeschlagen:", error);
    alert("Login fehlgeschlagen. Bitte überprüfen Sie Ihre Anmeldedaten.");
  }
};
</script>

<style scoped>
/* Optional: Styling */
</style>
