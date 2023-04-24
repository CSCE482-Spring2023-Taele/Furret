<template>
  <div class="hello">
    <h1 style="display: flex; justify-content: center;">{{songname.songname}}</h1>
    <v-flex class="my-flex">
        <div class="text-center">
          <v-card class="d-flex align-center justify-center" color="info" style="width: 100%;">
            <v-card-item>
              <div>
                <v-card-title>High Score</v-card-title>
                <div class="text-overline mb-1">
                  {{this.highscore}}
                </div>
              </div>
            </v-card-item>
          </v-card>
        </div>
    </v-flex>
    <div class="row">
      <v-card-actions class="justify-center" style="margin-top: 1%;">
        <v-btn color="warning" v-on:click="uploadResult()">
          <v-icon>{{ button }}</v-icon>
        </v-btn>
      </v-card-actions>
      <v-card-actions class="justify-center" style="margin-top: 1%;">
        <v-btn color="warning" v-on:click="toggle">{{ button_name }}</v-btn>
      </v-card-actions>
      <v-dialog
      v-model="dialog"
      persistent
      width="1024"
      >
        <template v-slot:activator="{ props }">
        <v-card-actions class="justify-center" v-bind="props" style="margin-top: 1%;">
          <v-btn color="warning">Rename</v-btn>
        </v-card-actions>
        </template>
        <v-card>
          <v-card-title>
            <span class="text-h5">Song Name</span>
          </v-card-title>
          <v-card-text>
            <v-container>
            <v-text-field
              v-model="sname"
              clearable
              hide-details="auto"
              label="Song Name"
            ></v-text-field>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="warning"
              variant="text"
              @click="dialog = false"
            >
              Close
            </v-btn>
            <v-btn
              color="warning"
              variant="text"
              @click="rename()"
            >
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-dialog
      v-model="d2"
      persistent
      width="auto"
      >
        <template v-slot:activator="{ props }">
        <v-card-actions class="justify-center" v-bind="props" style="margin-top: 1%;">
          <v-btn color="warning">Delete</v-btn>
        </v-card-actions>
        </template>
        <v-card>
          <v-card-title>
            <span class="text-h5">Are You Sure?</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-btn
                color="warning"
                variant="text"
                @click="remove()"
              >
                Yes
              </v-btn>
              <v-btn
                color="warning"
                variant="text"
                @click="d2 = false"
              >
                No
              </v-btn>
            </v-container>
          </v-card-text>
        </v-card>
      </v-dialog>
    </div>
    <component :is="component" :songid="songid" :songname="songname" :path="pathSong"/>
  </div>
</template>

<script>
import SheetMusicViewer from "./SheetMusicViewer.vue";
import ResultsTable from "./ResultsTable.vue";
import sound from '../assets/sample.mp3'
import Database from "tauri-plugin-sql-api";
import { open } from '@tauri-apps/api/dialog';
import { invoke } from '@tauri-apps/api/tauri';

const mytrack = new Audio(sound);
// const invoke = window.__TAURI__.invoke;
mytrack.crossOrigin = 'anonymous';

export default {
  name: 'SongScreenComponent',
  props: {
     songid: Number,
     songname: String,
     path: String
  },
  components: {
    SheetMusicViewer,
    ResultsTable
  },
  data (){
    return {
      component: ResultsTable,
      button_name: "View Sheet Music",
      pathSong: null,
      audio_var: false,
      button: "mdi-upload",
      highscore: 0,
      dialog: false,
      d2: false,
      sname: "default",
    }
  },
  mounted() {
    this.setHighScore();
    this.sname = this.songname.songname;
  },
  methods: {
    toggle(){
      if (this.component.name === "SheetMusicViewer") {
        this.component = ResultsTable;
        this.button_name = "View Sheet Music";
        this.pathSong = null;
      } else {
        this.component = SheetMusicViewer;
        this.button_name = "See Results";
        this.pathSong = this.path;
      }
    },
    /*
    playAudio() {
      if (this.audio_var == false) {
        mytrack.play();
        this.button = "mdi-pause"
        this.audio_var = true;
      } else {
        mytrack.pause()
        this.button = "mdi-play"
        mytrack.currentTime = 0;
        this.audio_var = false;
      }
    },
    */
    async uploadResult() {
      const selected = await open({
        multiple: true,
        filters: [{
          name: 'Audio',
          extensions: ['wav', 'mp3']
        }]
      });
      if (Array.isArray(selected)) {
        // user selected multiple files
        const db = await Database.load("sqlite:data.db");
        let filename = "error.txt"
        invoke('upload_processor', { inputAudio: selected[0], inputImage: this.path.path}).then((message) => {filename = message+".txt"; db.execute("INSERT INTO scores_table VALUES(" + this.songid.songid + ", 420, '" + filename + "');")});
        console.log("multiple");
      } else if (selected === null) {
        // user cancelled the selection
        console.log("cancelled");
      } else {
        // user selected a single file
        console.log("single");
      }
    },
    async setHighScore() {
      const db = await Database.load("sqlite:data.db");
      db.select("SELECT MAX(score) FROM scores_table WHERE song = '" + this.songid.songid + "';").then((response) => {
        if(response[0]["MAX(score)"] != null) { 
          this.highscore=response[0]["MAX(score)"]; 
        } 
        console.log(response)
      });
    },
    async rename() {
      let newName = this.sname;
      console.log(newName);
      this.dialog = false;
      const db = await Database.load("sqlite:data.db");
      db.execute("UPDATE songs_table SET name = '" + newName + "' WHERE song_id = '" + this.songid.songid + "'");
      window.location.href = '#/';
      location.reload();
    },
    async remove() {
      const db = await Database.load("sqlite:data.db");
      db.execute("DELETE FROM songs_table WHERE song_id = '" + this.songid.songid + "'");
      window.location.href = '#/';
      location.reload();
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.my-flex {
  display: flex;
  justify-content: center;
}
.row {
  display: flex;
  flex-direction: row;
  justify-content: center;
}
</style>
