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
    >
    <button @click="generatePassword">
      Generate Password
    </button>
  
    <div v-if="generatedPassword">
      <h3>Generated Password:</h3>
      <p>{{ generatedPassword }}
        <button @click="copyToClipboard" class="copy-btn" >
          &#128203;
        </button>
      </p>
      <div v-if="copied" class="copied-message"></div>
      Copied to clipboard
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
        localStorage.clear();
        sessionStorage.clear();
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
          if(err.message === 'QUOTA_BYTES quota exceeded'){
            localStorage.clear();
            sessionStorage.clear();
            this.error = "Storage quiat exceeded, Cleared storage";
          } else {
            this.error = "Error generating password.";
            console.error(err);
          }
       
        }
      },
      // Copy password to clipboard logic
      copyToClipboard(){
        navigator.clipboard.writeText(this.generatedPassword)
        .then(() => {
          this.copied = true;
          setTimeout(() => {
            this.copied = false;
          }, 2000);
      })
      .catch(err =>{
        this.error ="Failed to copy password to clipboard";
        console.error("Error copying to clipboard",err);
      })
      }
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
  
  .copy-btn {
  background: none;
  border: none;
  font-size: 18px;
  cursor: pointer;
  margin-left: 10px;
}

.copy-btn:hover {
  color: #007bff;
}

.error {
  color: red;
  font-weight: bold;
  margin-top: 20px;
}

.copied-message {
  color: green;
  font-weight: bold;
  margin-top: 10px;
}
  </style>
  