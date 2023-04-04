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
          v-for="item in desserts"
          :key="item.name"
        >
          <td>{{ item.name }}</td>
        </tr>
      </tbody>
    </v-table>
</template>

<script>
    export default {
        name: 'ResultsTable',
    }
</script>
  