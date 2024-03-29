import { createApp } from 'vue'
import App from './App.vue'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// import colors from 'vuetify/lib/util/colors'

const virtualosoTheme = {
  dark: false,
  colors: {
    background: '#FFFFFF',
    surface: '#FFFFFF',
    primary: '#673AB7',
    'primary-darken-1': '#3700B3',
    secondary: '#03DAC5',
    'secondary-darken-1': '#018786',
    error: 'black',
    info: '#fcfcfc',
    success: 'white',
    warning: '#120233',
  }
}

const virtualosoDark = {
  dark: true,
  colors: {
    background: '#00040a',
    surface: '#120233',
    primary: '#120233',
    'primary-darken-1': '#3700B3',
    secondary: '#c9b30a',
    'secondary-darken-1': '#018786',
    error: "#ffffff",
    info: '#320f61',
    success: '#130924',
    warning: '#954ee6',
  }
}

const vuetify = createVuetify({
  theme: {
    defaultTheme: 'virtualosoTheme',
    themes: {
      virtualosoTheme,
      virtualosoDark
    },
  },
  components,
  directives,
})


createApp(App).use(vuetify).mount('#app')
