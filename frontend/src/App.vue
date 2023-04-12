<template>
  <div id="app">
    <SplashScreen :isLoading="isLoading" />
    <main v-if="!isLoading">
      <MainScreen />
    </main>
  </div>
</template>

<script>
import MainScreen from './components/MainScreen.vue'
import SplashScreen from './components/SplashScreen.vue';
import Database from "tauri-plugin-sql-api";

export default {
  name: "App",
  components: {
    MainScreen,
    SplashScreen
  },
  data() {
    return { isLoading: true };
  },
  mounted() {
    setTimeout(() => {
      this.isLoading = false;
    }, 3000);
    async () => {    
      const db = await Database.load("sqlite:data.db");
      db.execute("CREATE TABLE IF NOT EXISTS scores_table( song Varchar, score INTEGER );");
      db.execute("CREATE TABLE IF NOT EXISTS songs_table( name Varchar, path Varchar );");
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
