<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center">
    <!-- Card Container -->
    <div class="bg-white shadow-lg rounded-lg flex flex-col md:flex-row w-full max-w-4xl h-[80vh]">
      
      <!-- Left Section: Bitcoin Price Info -->
      <div class="p-6 w-full md:w-1/2 flex flex-col justify-between bg-blue-50">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4">Bitcoin Price Tracker</h2>
        
        <!-- Current Price -->
        <div v-if="bitcoinPrice" class="bg-gray-50 p-4 rounded-md shadow-sm">
          <h3 class="text-lg font-medium text-gray-700">Current Bitcoin Price:</h3>
          <p class="text-gray-900 text-3xl mt-2">${{ bitcoinPrice }}</p>
        </div>

        <!-- Error Message -->
        <div v-if="error" class="bg-red-40 p-4 rounded-md text-red-700 mt-4">
          <p>{{ error }}</p>
        </div>

        <!-- Fetch Button -->
        <button
          @click="fetchBitcoinPrice"
          class="bg-blue-600 text-white py-3 rounded-md hover:bg-blue-700 transition duration-300 mt-4"
        >
          Get Latest Bitcoin Price
        </button>
      </div>

      <!-- Right Section: Real-Time Zigzag Chart -->
      <div class="w-full md:w-1/2 bg-white p-6 flex items-center justify-center">
        <canvas id="bitcoinChart" class="w-full h-full"></canvas>
      </div>

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
    this.fetchBitcoinPrice();
    this.intervalId = setInterval(() => {
      this.fetchBitcoinPrice();
    }, 60000);
  },
  beforeUnmount() {
    clearInterval(this.intervalId);
  },
  methods: {
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
          setTimeout(() => {
            this.fetchBitcoinPrice();
          }, 60000);
        } else {
          this.error = "Error fetching Bitcoin price.";
        }
      } finally {
        this.loading = false;
      }
    },
    updateChart(price) {
      this.bitcoinPrices.push(price);

      if (!this.chart) {
        const ctx = document.getElementById("bitcoinChart").getContext("2d");
        this.chart = new Chart(ctx, {
          type: "line",
          data: {
            labels: Array(this.bitcoinPrices.length).fill(""),
            datasets: [
              {
                label: "Bitcoin Price (USD)",
                data: this.bitcoinPrices,
        
                lineTension: 0.1, // Adjust this for a zigzag effect
                backgroundColor: "rgba(54, 162, 235, 0.2)",
                borderColor: "rgba(54, 162, 235, 1)",
                borderWidth: 2,
                tension: 0.3, // Adjust this for a zigzag effect
                pointStyle: "circle",
                pointRadius: 5,
                pointHoverRadius: 7,
     
              },
            ],
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              x: { display: false },
              y: { beginAtZero: false },
            },
            plugins: {
              tooltip: {
                callbacks: {
                  label: function (context) {
                    return ` $${context.raw}`;
                  },
                },
              },
            },
          },
        });
      } else {
        this.chart.data.labels.push("");
        this.chart.data.datasets[0].data = this.bitcoinPrices;
        this.chart.update();
      }
    },
  },
};
</script>

<style scoped>
/* Custom styling is mostly handled by Tailwind CSS */
</style>
