<template>
  <v-app>
    <v-flex class="my-flex">
      <div class="text-center">
        <v-btn 
          color="primary"
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

<docs>
  Method: toggleTheme():
  On click function that toggles between custom light mode and dark mode.

  Settings page is the component that handles the change of themes within the app.

</docs>