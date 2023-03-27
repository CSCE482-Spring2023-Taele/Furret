<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer">
      <!--  -->
      <v-sheet
        color="grey-lighten-4"
        class="pa-4"
      >
        <v-list>
          <v-list-item
            prepend-avatar="http://cdn.shopify.com/s/files/1/1419/7120/products/Lycoris_Red_Radiata.SHUT.jpg?v=1571439604"
            title="Not Senhe"
            subtitle="senhehao@senhehao.com"
          ></v-list-item>
        </v-list>
      </v-sheet>
      <v-divider />
      <v-list>
        <v-list-item prepend-icon="mdi-home" title="Home" v-bind="props" @click="goHome()" link></v-list-item>
        <v-list-group v-for="folder in folders" :key="folder.name" :value="folder.name">
          <template v-slot:activator="{ props }">
            <v-list-item
              v-bind="props"
            >{{folder.name}}</v-list-item>
          </template> 
          <v-list-item v-for="(song, i) in folder.songs" :key="i" @click="setSongId(song[0])" link>
              <v-list-item-title v-text="song[0]"></v-list-item-title>
          </v-list-item>
        </v-list-group>
      </v-list>
      <template v-slot:append>
        <v-divider />
        <div class="pa-2">
          <v-btn block
          color="#BB86FC"
          prepend-icon="mdi-cloud-upload"
          :loading="isSelecting" 
          @click="handleFileImport"
          >
            Upload
          </v-btn>
          <input 
            ref="uploader" 
            class="d-none" 
            type="file" 
            @change="onFileChanged"
          >
        </div>
      </template>
    </v-navigation-drawer>

    <v-app-bar
      color="primary"
    >
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>{{title}}</v-toolbar-title>
      
      <v-btn icon @click="swapPage('settings')">
        <v-icon>mdi-cog</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <!--  -->
      <component :is="currentView" v-bind="songid" />
    </v-main>
  </v-app>
</template>

<style>
.nav-btns {
    float: left !important;
  }
</style>

<script>
import HelloWorld from './HelloWorld.vue';
import HomeComponent from './HomeComponent.vue';
import SongScreenComponent from './SongScreenComponent.vue';
import Settings from './SettingsPage.vue'

const routes = {
  '/': HomeComponent,
  '/helloworld': HelloWorld,
  '/song': SongScreenComponent,
  '/settings': Settings,
}


export default {
  components: {
    HelloWorld,
    HomeComponent,
    SongScreenComponent,
    Settings,
  },
  data: () => ({ 
    currentPath: window.location.hash,
    drawer: null, 
    title: "Home",
    songid: null,
    folders: [
      { 
        name: 'Favorites',
        songs: [['So This Is Love', 'Cinderella-SO-THIS-IS-LOVE-01.gif'], ['Dreidel', 'Dreidel-sheet-music-with-chords.jpg']]
      },
      { 
        name: 'Bangers',
        songs: [['Glimpse of Us', 'Glimpse_of_us_jpg-1.jpg']]
      },
      { 
        name: 'Akash\'s Genshin Stash',
        songs: [['Albedo Cutscene', 'Albedo.jpg'], ['Dragonspine', 'dragonspine.jpg'], ['Eternal Oasis', 'Genshin.jpg']]
      },
    ],
    isSelecting: false,
    selectedFile: null,
  }),
  computed: {
    currentView() {
      return routes[this.currentPath.slice(1) || '/']
    }
  },
  mounted() {
    window.addEventListener('hashchange', () => {
      this.currentPath = window.location.hash
		})
  },
  methods: {
    swapPage: function(pagename) {
      this.songid = { songid: null }
      window.location.href = '#/' + pagename
      this.title = "Settings"
    },
    setSongId: function(sid) {
      this.songid = { songid: sid }
      window.location.href = '#/song'
      this.title = sid
    },
    goHome() {
      this.songid = { songid: null }
      window.location.href = '#/'
      this.title = "Home"
    },
    handleFileImport() {
      this.isSelecting = true;

      // After obtaining the focus when closing the FilePicker, return the button state to normal
      window.addEventListener('focus', () => {
          this.isSelecting = false
      }, { once: true });
      
      // Trigger click on the FileInput
      this.$refs.uploader.click();
    },
  },
}
</script>
