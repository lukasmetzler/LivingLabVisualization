// src/stores/auth.js
import { defineStore } from "pinia";
import apiClient from "../plugins/axios";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: localStorage.getItem("token") || "",
    user: null,
  }),
  actions: {
    async login(email, password) {
      try {
        const response = await apiClient.post("/login", { email, password });
        this.token = response.data.token;
        localStorage.setItem("token", this.token);
        // Optionally, fetch user data here
      } catch (error) {
        throw new Error("Login fehlgeschlagen");
      }
    },
    logout() {
      this.token = "";
      this.user = null;
      localStorage.removeItem("token");
    },
    async fetchUser() {
      try {
        const response = await apiClient.get("/me"); // Endpoint zum Abrufen der Benutzerdaten
        this.user = response.data;
      } catch (error) {
        console.error("Fehler beim Abrufen der Benutzerdaten:", error);
      }
    },
  },
});
