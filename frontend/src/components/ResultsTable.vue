<template>
  <div class="table-container">
    <v-table
      class="table"
      theme="dark"
      height="700px"
    >
      <thead>
        <tr>
          <th class="text-left">
            Past Results
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(score, i) in scores"
          :key="i"
        >
          <v-btn variant="tonal" @click="showModal">{{ score.score }}</v-btn>
        </tr>
      </tbody>
    </v-table>
    <GraphViewer
      v-show="isModalVisible"
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
    }),
    props: {
       songid: Number,
    },
    mounted() {
      this.getSongScores();
    },
    methods: {
      async getSongScores() {
        const db = await Database.load("sqlite:data.db");
        //db.execute("CREATE TABLE scores_table( song INTEGER, score INTEGER );");
        db.execute("INSERT INTO scores_table VALUES(1, 42);");
        db.execute("INSERT INTO scores_table VALUES(1, 314159);");
        db.execute("INSERT INTO scores_table VALUES(1, 2718);");
        db.execute("INSERT INTO scores_table VALUES(1, 666);");
        db.execute("INSERT INTO scores_table VALUES(1, 0);");
        console.log(this.songid.songid);
        var q_result = db.select("SELECT score FROM scores_table WHERE song = '" + this.songid.songid + "';").then((response) => { this.scores=response; console.log(response)});
        console.log(q_result);

      },
      showModal() {
        this.isModalVisible = true;
      },
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
</style>
