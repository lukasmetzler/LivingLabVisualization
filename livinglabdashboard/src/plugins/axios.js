import axios from "axios";
import { useRouter } from "vue-router";

const apiClient = axios.create({
  baseURL: "http://your-backend-api", // Ersetzen Sie dies durch die URL Ihres Backends
  headers: {
    "Content-Type": "application/json",
  },
});

// Füge den JWT-Token zu jeder Anfrage hinzu
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default apiClient;
