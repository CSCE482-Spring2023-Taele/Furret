<template>
  <div class="table-container">
    <v-table
      class="table"
      theme="dark"
      height="700px"
    >
      <thead>
        <tr>
          <th class="text-center" style="color: white;">
            Past Results
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(score, i) in scores"
          :key="i"
        >
          <td class="text-center" variant="tonal" @click="showModal(score.scorefile)">{{ score.score }}</td>
        </tr>
      </tbody>
    </v-table>
    <GraphViewer
      :key="graphKey"
      v-show="isModalVisible"
      :outputFilePath="outputFilePath"
      @close="closeModal"
    />
  </div>
</template>

<script>
import Database from "tauri-plugin-sql-api";
import GraphViewer from "./GraphViewer.vue";

export default {
    name: 'ResultsTable',
    components: {
      GraphViewer,
    },
    data: () => ({
      scores: [],
      isModalVisible: false,
      graphKey: 0,
      outputFilePath: ""
    }),
    props: {
      /**
       * Receives song ID from SongScreenComponent to fetch song scores and render them
       */
       songid: Number,
    },
    mounted() {
      this.getSongScores();
    },
    methods: {
      /**
       * Fetches song scores from database using song ID
       * @public This is a public method
       */
      async getSongScores() {
        const db = await Database.load("sqlite:data.db");
        //db.select("SELECT * FROM scores_table;").then((response) => console.log(response));
        //db.execute("CREATE TABLE scores_table( scoreid INTEGER primary key, song INTEGER, score INTEGER, scorefile Varchar );");
        //db.execute("INSERT INTO scores_table VALUES(1, 314159);");
        //db.execute("INSERT INTO scores_table VALUES(1, 2718);");
        //db.execute("INSERT INTO scores_table VALUES(1, 666);");
        //db.execute("INSERT INTO scores_table VALUES(1, 0);");
        console.log(this.songid.songid);
        var q_result = db.select("SELECT score, scorefile FROM scores_table WHERE song = '" + this.songid.songid + "';").then((response) => { this.scores=response; console.log(response)});
        console.log(q_result);

      },
      /**
       * On click function that renders GraphViewer through a modal by passing it the file name of output.txt
       * @param {string} ofilename
       * @public This is a public method
       */
      showModal(ofilename) {
        console.log(this.scores);
        console.log(ofilename); 
        this.isModalVisible = true;
        this.graphKey++;
        this.outputFilePath = ofilename; // change this to pull from database
      },
      /**
       * On click function to close modal
       * @public This is a public method
       */
      closeModal() {
        this.isModalVisible = false;
      }
    },
}
</script>

<style>
.table-container {
  margin-left: 3%; 
  margin-right: 3%;
  margin-bottom: 10px;
}
td {
  cursor: pointer;
  background-color: #2A2A2A;
  color: white;
  text-align: center;
  padding: 12px 24px;
  transition: all 0.3s ease;
}
td:hover {
  background-color: #555756;
}
</style>

<docs>
  ResultsTable is the component that renders the table with all song scores of a specific sheet music in SongScreenComponent.
  It takes in song ID from SongScreenComponent, fetches the song ID from database, and displays it in a table. 

</docs>