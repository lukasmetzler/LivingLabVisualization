// src/services/auth.js
import axios from "axios";

const API_URL = "http://localhost:5000/auth";

export const register = async (email, password) => {
  return await axios.post(`${API_URL}/register`, { email, password });
};

export const login = async (email, password) => {
  return await axios.post(`${API_URL}/login`, { email, password });
};

export const getProfile = async (token) => {
  return await axios.get(`${API_URL}/me`, {
    headers: { Authorization: token },
  });
};
