<template>
  <div class="hello">
    <h1 style="display: flex; justify-content: center;">{{songid.songid}}</h1>
    <v-flex class="my-flex">
        <div class="text-center">
          <v-card class="d-flex align-center justify-center" style="width: 100%;">
            <v-card-item>
              <div>
                <v-card-title>High Score</v-card-title>
                <div class="text-overline mb-1">
                  696969
                </div>
              </div>
            </v-card-item>
          </v-card>
        </div>
    </v-flex>
    <div class="row">
      <v-card-actions class="justify-center" style="margin-top: 1%;">
        <v-btn color="primary" v-on:click="playAudio">
          <v-icon>{{ button }}</v-icon>
        </v-btn>
      </v-card-actions>
      <v-card-actions class="justify-center" style="margin-top: 1%;">
        <v-btn color="primary" v-on:click="toggle">{{ button_name }}</v-btn>
      </v-card-actions>
    </div>
    <component :is="component" :songid="songid" :path="pathSong"/>
  </div>
</template>

<script>
import SheetMusicViewer from "./SheetMusicViewer.vue";
import ResultsTable from "./ResultsTable.vue";
import sound from '../assets/sample.mp3'

const mytrack = new Audio(sound);
mytrack.crossOrigin = 'anonymous';

export default {
  name: 'SongScreenComponent',
  props: {
     songid: String,
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
      button: "mdi-play"
    }
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
