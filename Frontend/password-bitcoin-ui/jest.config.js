export default {
  preset: "@vue/cli-plugin-unit-jest",
  "^.+\\.vue$": "vue-jest", // Use vue-jest to transform .vue files
  "^.+\\.js$": "babel-jest", // Use babel-jest to transform JavaScript files
};
