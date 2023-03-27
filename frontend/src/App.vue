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
