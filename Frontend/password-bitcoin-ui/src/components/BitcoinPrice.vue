<!-- src/components/BitcoinPrice.vue -->
<template>
  <div class="bitcoin-price">
    <h2>Bitcoin Price</h2>
    <button @click="fetchBitcoinPrice">
      Get Bitcoin Price
    </button>
  
    <div v-if="bitcoinPrice">
      <h3>Current Bitcoin Price:</h3>
      <p>${{ bitcoinPrice }}</p>
    </div>
  
    <div
      v-if="error"
      class="error"
    >
      <p>{{ error }}</p>
    </div>
  </div>
</template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "BitcoinPrice",
    data() {
      return {
        bitcoinPrice: null,
        error: "",
        intervalId:null,
      };
    },
    mounted(){
        //here we fetching the Bitcoin price immediately when the compoennt is mounted
        this.fetchBitcoinPrice();

        //here we set up a timer to fetch the Bitcoin price every 10 seconds
        this.intervalId = setInterval(() => {
          this.fetchBitcoinPrice();
        }, 60000);
      
    },
    beforeUnmount(){
        //here we clear the timer when the component is destroyed to prevent memory leaks
        clearInterval(this.intervalId);
    },
   
    methods: {
      // Fetch Bitcoin price method
      async fetchBitcoinPrice() {
        try {
          const response = await axios.get("http://localhost:8000/bitcoin-price");
          if (response.data.bitcoin_price_usd) {
            this.bitcoinPrice = parseFloat(response.data.bitcoin_price_usd).toFixed(2);
            this.error = "";
          } else {
            this.error = "Error fetching Bitcoin price.";
          }
        } catch (err) {
            if(err.response && err.response.status === 429){
                this.error = "Rate limit exceeded. Please try again later.";
                console.warn("Too many request , Retrying in 1 minute..");
                setTimeout(() => {
                    this.fetchBitcoinPrice();
                }, 600000); 
            } else if (err.message === "QUOTA_BYTES quota exceed"){
              localStorage.clear();
              sessionStorage.clear();
              this.error = "Session data cleared due to exceeding quota. Please try again later.";
            } 
            else {
                this.error = "Error fetching Bitcoin price.";
                console.error(err);
            }
         
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .bitcoin-price {
    text-align: center;
    margin-bottom: 30px;
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
  