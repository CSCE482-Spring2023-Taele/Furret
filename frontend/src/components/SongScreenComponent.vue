<template>
  <div class="hello">
    <h1 style="display: flex; justify-content: center;">{{songid}}</h1>
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
        <v-btn icon="mdi-play" color="primary"></v-btn>
      </v-card-actions>
      <v-card-actions class="justify-center" style="margin-top: 1%;">
        <v-btn color="primary">View Sheet Music</v-btn>
      </v-card-actions>
    </div>
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
          v-for="item in desserts"
          :key="item.name"
        >
          <td>{{ item.name }}</td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>

<script>
export default {
  name: 'SongScreenComponent',
  props: ['songid'],
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
