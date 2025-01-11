<!-- src/components/PasswordGenerator.vue -->
<template>
    <div class="password-generator">
      <h2>Generate a Password</h2>
      <input
        v-model="passwordLength"
        type="number"
        :min="8"
        :max="32"
        placeholder="Enter password length (min 8)"
      />
      <button @click="generatePassword">Generate Password</button>
  
      <div v-if="generatedPassword">
        <h3>Generated Password:</h3>
        <p>{{ generatedPassword }}</p>
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
        generatedPassword: "",
        error: "",
      };
    },
    methods: {
      // Generate password method (using POST)
      async generatePassword() {
        try {
          const response = await axios.post(
            `http://localhost:8000/generate-password`,  // POST request
            { length: this.passwordLength }           // Send password length in the body
          );
          if (response.data.password) {
            this.generatedPassword = response.data.password;
            this.error = "";
          } else {
            this.error = response.data.error;
          }
        } catch (err) {
          this.error = "Error generating password.";
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .password-generator {
    text-align: center;
    margin-bottom: 30px;
  }
  
  input {
    padding: 10px;
    font-size: 16px;
    margin-bottom: 20px;
  }
  
  button {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  h2 {
    font-size: 24px;
  }
  
  h3 {
    margin-top: 20px;
    font-size: 20px;
  }
  
  .error {
    color: red;
    font-weight: bold;
    margin-top: 20px;
  }
  </style>
  