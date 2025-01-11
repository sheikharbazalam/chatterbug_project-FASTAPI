const axios = require("axios");

const API_BASE_URL = "http://localhost:8000";

export const generatePassword = async (length) => {
  const response = await axios.get(
    `${API_BASE_URL}/generate-password?length=${length}`
  );
  return response.data;
};

export const fetchBitcoinPrice = async () => {
  const response = await axios.get(`${API_BASE_URL}/bitcoin-price`);
  return response.data;
};
