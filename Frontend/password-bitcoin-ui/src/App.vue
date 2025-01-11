<template>
  <div id="app">
    <h1>Password Generator & Bitcoin Price</h1>

    <!-- Password Generator -->
    <PasswordGenerator />

    <!-- Bitcoin Price -->
    <BitcoinPrice />

    <!-- Error Message (if needed) -->
    <ErrorMessage v-if="error" :message="error" />
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
    };
  },

  mounted() {
this.clearStorage();
  },
  methods: {
  clearStorage() {
   localStorage.clear();
   sessionStorage.clear();
   console.log("Storage cleared")
  },
}
};

</script>

<style scoped>
/* Add your styling here */
</style>
