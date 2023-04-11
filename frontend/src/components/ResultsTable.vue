<template>
    <v-table
      theme="dark"
      fixed-header
      height="300px"
      style="margin-left: 3%; margin-right: 3%;"
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
          <td>{{ score.score }}</td>
        </tr>
      </tbody>
    </v-table>
</template>

<script>
import Database from "tauri-plugin-sql-api";

export default {
    name: 'ResultsTable',
    data: () => ({
      scores: [
        {
          score: 69
        },
        {
          score: 89
        },
      ],
    }),
    props: {
       songid: String,
    },
    mounted() {
      this.getSongScores();
    },
    methods: {
      async getSongScores() {
        const db = await Database.load("sqlite:data.db");
        //db.execute("CREATE TABLE scores_table( song Varchar, score INTEGER );");
        //db.execute("INSERT INTO scores_table VALUES('So This Is Love', 42);");
        //db.execute("INSERT INTO scores_table VALUES('So This Is Love', 314159);");
        //db.execute("INSERT INTO scores_table VALUES('So This Is Love', 2718);");
        //db.execute("INSERT INTO scores_table VALUES('So This Is Love', 666);");
        //db.execute("INSERT INTO scores_table VALUES('So This Is Love', 0);");
        console.log(this.songid.songid);
        var q_result = db.select("SELECT score FROM scores_table WHERE song = '" + this.songid.songid + "';").then((response) => { this.scores=response; console.log(response)});
        console.log(q_result);

      }
    },
}
</script>
  
