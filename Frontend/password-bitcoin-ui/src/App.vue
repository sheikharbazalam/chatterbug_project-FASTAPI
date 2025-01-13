<template>
  <div id="app" class="min-h-screen bg-gradient-to-br from-gray-100 to-gray-200">
    <!-- Navigation Tabs -->
    <div class="bg-white shadow-md p-1 fixed top-0  left-0 w-full flex items-center justify-between">
  
      <div class="flex items-center space-x-4">
        <img class="h-max w-40 rounded-full cursor-pointer" :src="user.imageUrl" alt="User Profile"
        @click="activeTab = 'gotToHome'"
        :class="tabClass('gotToHome')"
         />
  
      </div>

      <div class="flex space-x-4 ">
        <div class="inline-flex items-center rounded-md  px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"> 
        <button 
          @click="activeTab = 'password'"
          :class="tabClass('password')"
        >
          Password Generator
        </button>
      </div>
      <div class="inline-flex items-center rounded-md  px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 hover:text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white-600">
        <button
          @click="activeTab = 'bitcoin'"
          :class="tabClass('bitcoin')"
        >
          Bitcoin Price
        </button>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="container mx-auto pt-20">
 
      <div v-if="activeTab === 'password'">
        <PasswordGenerator />
      </div>
      <div v-if="activeTab === 'bitcoin'">
        <BitcoinPrice />
      </div>

      <div v-if="activeTab === 'gotToHome'">
        <HomePage />
      </div>
    </div>

    <!-- Error Message (if needed) -->
    <ErrorMessage v-if="error" :message="error" />
  </div>
</template>

<script>
import PasswordGenerator from "./components/PasswordGenerator.vue";
import BitcoinPrice from "./components/BitcoinPrice.vue";
import ErrorMessage from "./components/ErrorMessage.vue";
import { useRouter } from "vue-router";
import HomePage from "./components/HomePage.vue";

export default {
  name: "App",
  components: {
    PasswordGenerator,
    BitcoinPrice,
    ErrorMessage,
    HomePage
  },
  data() {
    return {
      activeTab: "password", // Default to Password Generator tab
      error: "",
      user: {
       
        imageUrl:
          "data:image/png;base64,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",
      },
    };
  },
  setup(){
    const router = useRouter();
    const gotToHome = () =>{
      router.push({name:"HomePage"});

    };
    return {
      gotToHome,
      
    };
  },
  methods: {
    tabClass(tab) {
      return this.activeTab === tab
        ? "text-blue-600 border-b-4 border-blue-600 pb-1"
        : "text-gray-600 hover:text-blue-600";
    },
  },
  gotToHome(){
    this.$router.push({name:"HomePage"});
  }
};
</script>

<style scoped>
/* Additional styling for buttons and layout if needed */
button {
  font-size: 16px;
  padding: 8px 16px;
  border: none;
  background: none;
  cursor: pointer;
  transition: color 0.2s;
}
button:focus {
  outline: none;
}
</style>
