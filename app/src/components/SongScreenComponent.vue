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
//import { open } from '@tauri-apps/api/dialog';
//import { invoke } from '@tauri-apps/api/tauri';

const mytrack = new Audio(sound);
//const invoke = window.__TAURI__.invoke;
mytrack.crossOrigin = 'anonymous';

export default {
  name: 'SongScreenComponent',
  props: {
    /**
     * Receives song ID from MainScreen
     */
     songid: Number,
     /**
     * Receives song name from MainScreen
     */
     songname: String,
     /**
     * Receives path of sheet music file from MainScreen
     */
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
      score: 0
    }
  },
  mounted() {
    this.setHighScore();
    this.sname = this.songname.songname;
  },
  methods: {
    /**
     * On click function that toggles between a view of song score results and sheet music file
     * @public This is a public method
     */
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
   /**
     * Asynchronous function that uploads song name, score, and score file into database
     * @public This is a public method
     */
    async uploadResult() {
      /*
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
        invoke('upload_processor', { inputAudio: selected[0], inputImage: this.path.path}).then((message) => {
          let fname = message.split("\n").at(-2).replace(/(\r\n|\n|\r)/gm, "");
          filename = fname+".txt"; 
          import('raw-loader!../../src-tauri/resources/outputs/' + filename).then(module => {
            return module.default;
          }).then(fileContent => {
           fileContent.split('\n').forEach(element => {
               let val0 = element.split(' ')[0];
               let score = element.split(' ')[3];
               if (val0 === "Similarity") {
                  this.score = Math.round(score * 1000);    
                  db.execute("INSERT INTO scores_table (song, score, scorefile) VALUES(" + this.songid.songid + ", " + this.score + ", '" + filename + "');"); 
               }
            }) 
          });
        db.execute("INSERT INTO scores_table (song, score, scorefile) VALUES(" + this.songid.songid + ", " + this.score + ", '" + filename + "');"); 
        });
        console.log("multiple");
      } else if (selected === null) {
        // user cancelled the selection
        console.log("cancelled");
        const db = await Database.load("sqlite:data.db");
        console.log(db.select("SELECT * FROM scores_table;"));
      } else {
        // user selected a single file
        console.log("single");
      }
      */
      let filename = "1682912737.txt";
        const db = await Database.load("sqlite:data.db");
        console.log(db.select("SELECT * FROM scores_table;"));
          import('raw-loader!../../src-tauri/resources/outputs/' + filename).then(module => {
            return module.default;
          }).then(fileContent => {
           fileContent.split('\n').forEach(element => {
               let val0 = element.split(' ')[0];
               let score = element.split(' ')[3];
               if (val0 === "Similarity") {
                  this.score = Math.round(score * 1000);    
                  db.execute("INSERT INTO scores_table (song, score, scorefile) VALUES(" + this.songid.songid + ", " + this.score + ", '" + filename + "');"); 
               }
            }) 
          });
        //const db = await Database.load("sqlite:data.db");
        console.log(db.select("SELECT * FROM scores_table;"))

    },
    /**
     * Asynchronous function that sets highest score of this sheet music and renders it on SongScreenComponent
     * @public This is a public method
     */
    async setHighScore() {
      const db = await Database.load("sqlite:data.db");
      db.select("SELECT MAX(score) FROM scores_table WHERE song = '" + this.songid.songid + "';").then((response) => {
        if(response[0]["MAX(score)"] != null) { 
          this.highscore=response[0]["MAX(score)"]; 
        } 
        console.log(response)
      });
    },
    /**
     * Asynchronous function that updates name of song in database and re-renders name change on SongScreenComponent
     * @public This is a public method
     */
    async rename() {
      let newName = this.sname;
      console.log(newName);
      this.dialog = false;
      const db = await Database.load("sqlite:data.db");
      db.execute("UPDATE songs_table SET name = '" + newName + "' WHERE song_id = '" + this.songid.songid + "'");
      window.location.href = '#/';
      location.reload();
    },
    /**
     * Asynchronous function that deletes this song from database
     * @public This is a public method
     */
    async remove() {
      const db = await Database.load("sqlite:data.db");
      db.execute("DELETE FROM songs_table WHERE song_id = '" + this.songid.songid + "'");
      db.execute("DELETE FROM scores_table WHERE song = '" + this.songid.songid + "'");
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

<docs>
  SongScreenComponent is the component rendered for each song. It is accessible via the song names on the left side bar
  and shows a view of the Song name, highest score for this song based on previous audio recording uploads, has a button for
  audio upload, a button to toggle between sheet music viewer and result viewer components, and handles rename and deletion of song.
  This component is the overarching component for all actions related to a specific song, including audio upload, sheet music viewer, results viewer, and rename and deletion.

</docs>