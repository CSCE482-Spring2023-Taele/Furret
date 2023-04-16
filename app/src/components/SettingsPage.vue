<template>
  <v-app>
    <v-flex class="my-flex">
      <div class="text-center">
        <v-btn 
          color="#43236a"
          style="color: white;" 
          @click="toggleTheme"
        >
          toggle theme
        </v-btn>
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
      toggleTheme() {
        console.log(theme.global.current);
        theme.global.name.value = theme.global.current.value.dark ? 'virtualosoTheme' : 'virtualosoDark'
      }
    }
  }
}
</script>