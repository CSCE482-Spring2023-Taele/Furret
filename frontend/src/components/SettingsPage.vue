<template>
    <v-app>
      <v-flex class="my-flex">
        <div class="text-center">
          <v-btn @click="toggleTheme">toggle theme</v-btn>
        </div>
      </v-flex>
    </v-app>
  </template>
  
  <style>
  .my-flex {
    margin-top: 20px;
  }
  </style>
  
  <script>
  import { useTheme } from 'vuetify'
  
  export default {
    setup () {
      const theme = useTheme()
  
      return {
        theme,
        toggleTheme: () => theme.global.name.value = theme.global.current.value.dark ? 'virtualosoTheme' : 'dark'
      }
    }
  }
  </script>