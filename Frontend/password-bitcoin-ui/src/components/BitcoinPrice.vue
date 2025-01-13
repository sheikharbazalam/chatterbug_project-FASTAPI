<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center">
    <!-- Card Component -->
    <div class="bg-white shadow-lg rounded-lg p-6 w-full max-w-lg">
      <!-- Title -->
      <h2 class="text-2xl font-semibold text-center mb-4 text-gray-800">Bitcoin Price Tracker</h2>

      <!-- Fetch Button -->
      <button
        @click="fetchBitcoinPrice"
        class="w-full bg-blue-600 text-white py-3 rounded-md hover:bg-blue-700 transition duration-300 mb-4"
      >
        Get Latest Bitcoin Price
      </button>

      <!-- Loading Spinner -->
      <div v-if="loading" class="flex justify-center mb-4">
        <svg
          class="animate-spin h-8 w-8 text-blue-600"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
        >
          <circle
            class="opacity-25"
            cx="12"
            cy="12"
            r="10"
            stroke="currentColor"
            stroke-width="4"
          ></circle>
          <path
            class="opacity-75"
            fill="currentColor"
            d="M4 12a8 8 0 018-8v8z"
          ></path>
        </svg>
      </div>

      <!-- Current Price Display -->
      <div v-if="bitcoinPrice" class="bg-gray-50 p-4 rounded-md shadow-sm">
        <h3 class="text-lg font-medium text-gray-700">Current Bitcoin Price:</h3>
        <p class="text-gray-900 text-xl mt-2">${{ bitcoinPrice }}</p>
      </div>

      <!-- Error Message -->
      <div v-if="error" class="bg-red-50 p-4 rounded-md text-red-700 mt-4">
        <p>{{ error }}</p>
      </div>

      <!-- Bitcoin Price Chart -->
      <canvas
        id="bitcoinChart"
        v-if="bitcoinPrices.length > 0"
        class="mt-6"
      ></canvas>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

export default {
  name: "BitcoinPrice",
  data() {
    return {
      bitcoinPrice: null,
      bitcoinPrices: [],
      error: "",
      intervalId: null,
      chart: null,
      loading: false,
    };
  },
  mounted() {
    // Fetch Bitcoin price immediately when the component is mounted
    this.fetchBitcoinPrice();

    // Set up a timer to fetch the Bitcoin price every 60 seconds
    this.intervalId = setInterval(() => {
      this.fetchBitcoinPrice();
    }, 60000);
  },
  beforeUnmount() {
    // Clear the timer when the component is destroyed to prevent memory leaks
    clearInterval(this.intervalId);
  },
  methods: {
    // Fetch Bitcoin price method
    async fetchBitcoinPrice() {
      this.loading = true;
      try {
        const response = await axios.get("http://localhost:8000/bitcoin-price");
        if (response.data.bitcoin_price_usd) {
          const price = parseFloat(response.data.bitcoin_price_usd).toFixed(2);
          this.bitcoinPrice = price;
          this.error = "";
          this.updateChart(price);
        } else {
          this.error = "Error fetching Bitcoin price.";
        }
      } catch (err) {
        if (err.response && err.response.status === 429) {
          this.error = "Rate limit exceeded. Please try again later.";
          console.warn("Too many requests. Retrying in 1 minute...");
          setTimeout(() => {
            this.fetchBitcoinPrice();
          }, 60000);
        } else {
          this.error = "Error fetching Bitcoin price.";
          console.error(err);
        }
      } finally {
        this.loading = false;
      }
    },
    // Update the chart with the latest price
    updateChart(price) {
      this.bitcoinPrices.push(price);

      if (!this.chart) {
        // Initialize the chart
        const ctx = document.getElementById("bitcoinChart").getContext("2d");
        this.chart = new Chart(ctx, {
          type: "line",
          data: {
            labels: Array(this.bitcoinPrices.length).fill(""),
            datasets: [
              {
                label: "Bitcoin Price (USD)",
                data: this.bitcoinPrices,
                backgroundColor: "rgba(54, 162, 235, 0.2)",
                borderColor: "rgba(54, 162, 235, 1)",
                borderWidth: 2,
                tension: 0.4,
              },
            ],
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              x: {
                display: false,
              },
              y: {
                beginAtZero: false,
              },
            },
          },
        });
      } else {
        // Update existing chart
        this.chart.data.labels.push("");
        this.chart.data.datasets[0].data = this.bitcoinPrices;
        this.chart.update();
      }
    },
  },
};
</script>

<style scoped>
/* Tailwind utilities already handle most of the styling */
</style>
