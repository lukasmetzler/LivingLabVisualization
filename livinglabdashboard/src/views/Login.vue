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

<script>
import { useAuthStore } from "../stores/auth";
import { useRouter } from "vue-router";

export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();
    return { authStore, router };
  },
  methods: {
    async login() {
      try {
        await this.authStore.login(this.email, this.password);
        this.router.push("/dashboard");
      } catch (error) {
        console.error("Login fehlgeschlagen:", error);
        alert("Login fehlgeschlagen. Bitte überprüfen Sie Ihre Anmeldedaten.");
      }
    },
  },
};
</script>

<style scoped>
/* Optional: Styling */
</style>
