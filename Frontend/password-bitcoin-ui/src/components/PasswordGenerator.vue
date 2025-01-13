<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-100">
    <!-- Card Component -->
    <div class="bg-white shadow-lg rounded-lg p-6 w-full max-w-md">
      <h2 class="text-2xl font-semibold text-center mb-4 text-gray-800">Generate a Password</h2>

      <!-- Input Field -->
      <div class="mb-4">
        <label for="passwordLength" class="block text-gray-600 font-medium mb-2">
          Enter Password Length (8-32):
        </label>
        <input
          id="passwordLength"
          v-model="passwordLength"
          type="number"
          :min="8"
          :max="32"
          class="w-full p-3 border rounded-md text-gray-800 focus:ring-2 focus:ring-blue-500"
          placeholder="Enter password length"
        />
      </div>

      <!-- Checkbox Options -->
      <div class="mb-4">
        <label class="block text-gray-600 font-medium mb-2">Password Options:</label>
        <div class="flex items-center mb-2">
          <input
            type="checkbox"
            id="includeNumbers"
            v-model="includeNumbers"
            class="mr-2"
          />
          <label for="includeNumbers" class="text-gray-700">Include Numbers</label>
        </div>
        <div class="flex items-center">
          <input
            type="checkbox"
            id="includeSpecialChars"
            v-model="includeSpecialChars"
            class="mr-2"
          />
          <label for="includeSpecialChars" class="text-gray-700">Include Special Characters</label>
        </div>
      </div>

      <!-- Generate Button -->
      <button
        @click="generatePassword"
        class="w-full bg-blue-600 text-white py-3 rounded-md hover:bg-blue-700 transition duration-300"
      >
        Generate Password
      </button>

      <!-- Generated Password Display -->
      <div v-if="generatedPassword" class="mt-6 bg-gray-50 p-4 rounded-md shadow-sm">
        <h3 class="text-lg font-medium text-gray-700">Generated Password:</h3>
        <div class="flex items-center justify-between mt-2">
          <p class="text-gray-900 break-all">{{ generatedPassword }}</p>
          <button
            @click="copyToClipboard"
            class="text-blue-600 hover:text-blue-800"
          >
            &#128203;
          </button>
        </div>
        <div v-if="copied" class="text-green-600 font-medium mt-2">Copied to clipboard!</div>
      </div>

      <!-- Error Message -->
      <p v-if="error" class="text-red-600 font-medium mt-4">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PasswordGenerator",
  data() {
    return {
      passwordLength: 12,
      includeNumbers: true,
      includeSpecialChars: true,
      generatedPassword: "",
      error: "",
      copied: false,
    };
  },
  methods: {
    async generatePassword() {
      localStorage.clear();
      sessionStorage.clear();
      try {
        const response = await axios.post(`http://localhost:8000/generate-password`, {
          length: this.passwordLength,
          includeNumbers: this.includeNumbers,
          includeSpecialChars: this.includeSpecialChars,
        });
        if (response.data.password) {
          this.generatedPassword = response.data.password;
          this.error = "";
        } else {
          this.error = response.data.error;
        }
      } catch (err) {
        if (err.message === "QUOTA_BYTES quota exceeded") {
          localStorage.clear();
          sessionStorage.clear();
          this.error = "Storage quota exceeded. Cleared storage.";
        } else {
          this.error = "Error generating password.";
          console.error(err);
        }
      }
    },
    copyToClipboard() {
      navigator.clipboard
        .writeText(this.generatedPassword)
        .then(() => {
          this.copied = true;
          setTimeout(() => {
            this.copied = false;
          }, 2000);
        })
        .catch((err) => {
          this.error = "Failed to copy password to clipboard.";
          console.error("Error copying to clipboard", err);
        });
    },
  },
};
</script>

<style scoped>
/* Tailwind utilities already handle most of the styling */
</style>
