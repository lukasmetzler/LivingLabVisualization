import axios from "axios";

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_BACKEND_URL || "http://localhost:3001", // Ersetze dies mit der URL deines Backends
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
