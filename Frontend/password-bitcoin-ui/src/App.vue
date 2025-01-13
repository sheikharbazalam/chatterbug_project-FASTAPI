<template>
  <div id="app" class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div class="bg-white shadow-lg rounded-lg p-6 w-full max-w-lg">
      <h1 class="text-2xl font-bold text-center mb-6">Welcome to Chatterburg</h1>

      <div v-if="!activeComponent" class="grid grid-cols-1 gap-4">
        <button
          @click="navigateTo('password')"
          class="bg-blue-500 text-white py-3 px-5 rounded-lg shadow-md hover:bg-blue-600"
        >
          Password Generator
        </button>

        <button
          @click="navigateTo('bitcoin')"
          class="bg-yellow-500 text-white py-3 px-5 rounded-lg shadow-md hover:bg-yellow-600"
        >
          Bitcoin Price
        </button>
      </div>

      <!-- Render the selected component -->
      <div v-if="activeComponent === 'password'">
        <PasswordGenerator />
        <button @click="activeComponent = null" class="mt-4 text-blue-500">Back</button>
      </div>

      <div v-if="activeComponent === 'bitcoin'">
        <BitcoinPrice />
        <button @click="activeComponent = null" class="mt-4 text-yellow-500">Back</button>
      </div>

      <ErrorMessage v-if="error" :message="error" />
    </div>
  </div>
</template>

<script>
import PasswordGenerator from "./components/PasswordGenerator.vue";
import BitcoinPrice from "./components/BitcoinPrice.vue";
import ErrorMessage from "./components/ErrorMessage.vue";

export default {
  name: "App",
  components: {
    PasswordGenerator,
    BitcoinPrice,
    ErrorMessage,
  },
  data() {
    return {
      error: "",
      activeComponent: null,
    };
  },
  methods: {
    navigateTo(component) {
      this.activeComponent = component;
    },
  },
};
</script>

<style scoped>
/* Add additional styling here if needed */
</style>
