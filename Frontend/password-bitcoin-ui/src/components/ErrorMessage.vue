<template>
    <div v-if="message" class="error">
      <p>{{ message }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: "ErrorMessage",
    props: {
      message: {
        type: String,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  .error {
    color: red;
    font-weight: bold;
    margin-top: 20px;
  }
  </style>
  