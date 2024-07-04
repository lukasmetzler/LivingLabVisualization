import axios from "axios";

const API_URL = "http://85.215.59.47/auth";

export const register = async (email, password, first_name, last_name) => {
  return await axios.post(`${API_URL}/register`, {
    email,
    password,
    first_name,
    last_name,
  });
};

export const login = async (email, password) => {
  return await axios.post(`${API_URL}/login`, { email, password });
};

export const getProfile = async (token) => {
  return await axios.get(`${API_URL}/me`, {
    headers: { Authorization: token },
  });
};
