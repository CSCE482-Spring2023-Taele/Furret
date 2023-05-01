<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer">
      <!--  -->
      <v-sheet
        color="info"
        class="pa-4"
      >
        <v-list>
          <v-list-item
            prepend-avatar="http://cdn.shopify.com/s/files/1/1419/7120/products/Lycoris_Red_Radiata.SHUT.jpg?v=1571439604"
            title="Virtualoso"
          ></v-list-item>
        </v-list>
      </v-sheet>
      <v-divider />
      <v-list>
        <v-list-item prepend-icon="mdi-home" title="Home" :key="-1" :value="Home" @click="goHome()" link></v-list-item>
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
        <v-list-item v-for="(song, i) in songs" :key="i" @click="setSongId(song.song_id, song.name, song.path)" active-color='#673AB7'>
            <v-list-item-title v-text="song.name"></v-list-item-title>
        </v-list-item>
      </v-list>
      <template v-slot:append>
        <v-divider />
        <div class="pa-2">
          <v-btn block
            color="primary"
            style="color: white;"
            prepend-icon="mdi-cloud-upload"
            :loading="isSelecting" 
            @click="handleSheetMusicImport"
          >
            Sheet Music Upload
          </v-btn>
          <v-divider />
          <v-btn block
            color="primary"
            style="color: white;"
            prepend-icon="mdi-cloud-upload"
            :loading="isSelecting" 
            @click="handleMusicXMLImport"
          >
            MusicXML Upload
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

      <v-toolbar-title></v-toolbar-title>
      
      <v-btn icon @click="swapPage('settings')">
        <v-icon>mdi-cog</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <!--  -->
      <component :is="currentView" :songid="songid" :songname="songname" :path="pathMainScreen" :key="component_reload"/>
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
import{ open } from '@tauri-apps/api/dialog';
import { copyFile, BaseDirectory } from '@tauri-apps/api/fs';

const routes = {
  '/': HomeComponent,
  '/song': SongScreenComponent,
  '/settings': Settings,
}


export default {
  name: 'MainScreen',
  components: {
    HomeComponent,
    SongScreenComponent,
    Settings,
  },
  data: () => ({
    currentPath: window.location.hash,
    drawer: null, 
    songid: null,
    songname: "Default",
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
        song_id: 1,
        name: 'blah 1',
        path: 'Cinderella-SO-THIS-IS-LOVE-01.gif'
      },
      {
        song_id: 2,
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
      this.songname = { songname: null }
      window.location.href = '#/' + pagename
      this.pathMainScreen = {path: null}
    },
    setSongId: function(sid, sname, pathSongScreen) {
      this.songid = { songid: sid }
      this.songname = { songname: sname}
      window.location.href = '#/song'
      this.pathMainScreen = {path: pathSongScreen}
      this.component_reload++;
    },
    goHome() {
      this.songid = { songid: null }
      this.songname = { songname: null }
      window.location.href = '#/'
      this.pathMainScreen = {path: null}
    },
    async handleSheetMusicImport() {
      /*
      this.isSelecting = true;

      // After obtaining the focus when closing the FilePicker, return the button state to normal
      window.addEventListener('focus', () => {
          this.isSelecting = false
      }, { once: true });
      
      // Trigger click on the FileInput
      this.$refs.uploader.click();
      */
      const selected = await open({
        multiple: true,
        filters: [{
          name: 'Image',
          extensions: ['png', 'jpeg', 'jpg']
        }]
      });
      if (Array.isArray(selected)) {
        // user selected multiple files
        console.log("multiple");
        console.log(selected);
        for(let i = 0; i < selected.length; i++) {
          let newSong = selected.at(i);
          console.log(newSong);
          let newName = newSong.split(/(\\|\/)/g).pop().replace(/\.[^/.]+$/, "");
          console.log(newName);
          //const contents = await readBinaryFile(newSong);
          //await writeBinaryFile('$APP/public/assets/sheets/'+newSong.split(/(\\|\/)/g).pop(), contents);
          //await writeBinaryFile(newSong.split(/(\\|\/)/g).pop(), contents, {dir: BaseDirectory});
          let targetDir = "resources/sheets/"+newSong.split(/(\\|\/)/g).pop();
          await copyFile(newSong, targetDir, {dir: BaseDirectory.appLocalDataDir});
          this.uploadNewSong(newName, newSong.split(/(\\|\/)/g).pop());
          //this.getSongData();
        }
      } else if (selected === null) {
        // user cancelled the selection
        console.log("cancelled");
      } else {
        // user selected a single file
        console.log("single");
      }
    },
    async handleMusicXMLImport() {},
    async getSongData() {
      console.log("testing testing");
      const db = await Database.load("sqlite:data.db");
      //db.execute("CREATE TABLE songs_table( song_id integer primary key, name Varchar, path Varchar );");
      //db.execute("INSERT INTO songs_table (name, path) VALUES('So This Is Love', 'Cinderella-SO-THIS-IS-LOVE-01.gif');");
      //db.execute("INSERT INTO songs_table (name, path) VALUES('Dreidel', 'Dreidel-sheet-music-with-chords.jpg');");
      //db.execute("INSERT INTO songs_table (name, path) VALUES('Glimpse of Us', 'Glimpse_of_us_jpg-1.jpg');");
      //db.execute("INSERT INTO songs_table (name, path) VALUES('Albedo Cutscene', 'Albedo.jpg');");
      //db.execute("INSERT INTO songs_table (name, path) VALUES('Dragonspine', 'dragonspine.jpg');");
      //db.execute("INSERT INTO songs_table (name, path) VALUES('Eternal Oasis', 'Genshin.jpg');");
      var q_result = db.select("SELECT * FROM songs_table;").then((response) => {this.songs = response; console.log(response)});
      console.log(q_result);
      return "";
    },
    async uploadNewSong(newSongName, newSongPath) {
      const db = await Database.load("sqlite:data.db");
      console.log(newSongPath);
      db.execute("INSERT INTO songs_table (name, path) VALUES('" + newSongName + "', '" + newSongPath + "');");
      //db.execute("INSERT INTO songs_table VALUES('Kashmirga', 'Genshin.jpg');");
    },
  },
}
</script>
