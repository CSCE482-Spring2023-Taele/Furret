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
      <!--
        <v-list-group v-for="folder in folders" :key="folder.name" :value="folder.name">
          <template v-slot:activator="{ props }">
            <v-list-item
              v-bind="props"
            >{{folder.name}}</v-list-item>
          </template> 
          <v-list-item v-for="(song, i) in folder.songs" :key="i" @click="setSongId(song[0], song[1])" link>
              <v-list-item-title v-text="song[0]"></v-list-item-title>
          </v-list-item>
        </v-list-group>
        -->
        <v-list-item v-for="(song, i) in songs" :key="i" @click="setSongId(song.name, song.path)" link>
            <v-list-item-title v-text="song.name"></v-list-item-title>
        </v-list-item>
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
      <component :is="currentView" :songid="songid" :path="pathMainScreen" :key="component_reload"/>
    </v-main>
  </v-app>
</template>

<style>
.nav-btns {
    float: left !important;
  }
</style>

<script>
import HomeComponent from './HomeComponent.vue';
import SongScreenComponent from './SongScreenComponent.vue';
import Settings from './SettingsPage.vue'
import Database from "tauri-plugin-sql-api";

const routes = {
  '/': HomeComponent,
  '/song': SongScreenComponent,
  '/settings': Settings,
}


export default {
  components: {
    HomeComponent,
    SongScreenComponent,
    Settings,
  },
  data: () => ({
    currentPath: window.location.hash,
    drawer: null, 
    title: "Home",
    songid: null,
    pathMainScreen: null,
    component_reload: 0,
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
    songs: [
      {
        name: 'blah 1',
        path: 'Cinderella-SO-THIS-IS-LOVE-01.gif'
      },
      {
        name: 'blah 2',
        path: 'Glimpse_of_us_jpg-1.jpg'
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
    this.getSongData();
  },
  methods: {
    swapPage: function(pagename) {
      this.songid = { songid: null }
      window.location.href = '#/' + pagename
      this.title = "Settings"
      this.pathMainScreen = {path: null}
    },
    setSongId: function(sid, pathSongScreen) {
      this.songid = { songid: sid }
      window.location.href = '#/song'
      this.title = sid
      this.pathMainScreen = {path: pathSongScreen}
      this.component_reload++;
    },
    goHome() {
      this.songid = { songid: null }
      window.location.href = '#/'
      this.title = "Home"
      this.pathMainScreen = {path: null}
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
    async getSongData() {
      console.log("testing testing");
      const db = await Database.load("sqlite:data.db");
      //db.execute("CREATE TABLE songs_table( name Varchar, path Varchar );");
      //db.execute("INSERT INTO songs_table VALUES('So This Is Love', 'Cinderella-SO-THIS-IS-LOVE-01.gif');");
      //db.execute("INSERT INTO songs_table VALUES('Dreidel', 'Dreidel-sheet-music-with-chords.jpg');");
      //db.execute("INSERT INTO songs_table VALUES('Glimpse of Us', 'Glimpse_of_us_jpg-1.jpg');");
      //db.execute("INSERT INTO songs_table VALUES('Albedo Cutscene', 'Albedo.jpg');");
      //db.execute("INSERT INTO songs_table VALUES('Dragonspine', 'dragonspine.jpg');");
      //db.execute("INSERT INTO songs_table VALUES('Eternal Oasis', 'Genshin.jpg');");
      var q_result = db.select("SELECT * FROM songs_table;").then((response) => {this.songs = response; console.log(response)});
      console.log(q_result);
      return "";
    },
  },
}
</script>
