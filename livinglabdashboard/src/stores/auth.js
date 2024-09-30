import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: localStorage.getItem("token") || "",
    user: null,
  }),
  actions: {
    async login(email, password) {
      try {
        const response = await axios.post("/login", { email, password });
        this.token = response.data.token;
        localStorage.setItem("token", this.token);
        await this.fetchUser();
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
        const response = await axios.get("/me");
        this.user = response.data;
      } catch (error) {
        console.error("Fehler beim Abrufen der Benutzerdaten:", error);
      }
    },
  },
});
