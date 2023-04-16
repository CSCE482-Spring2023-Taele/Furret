<template>
  <div class="hello">
    <h1 style="display: flex; justify-content: center;">Welcome to Virtualoso!</h1>
    <v-flex class="my-flex">
        <div class="text-center">
          <v-card class="d-flex align-center justify-center" style="width: 100%;">
            <v-card-item>
              <div>
                <v-card-title>Last Played</v-card-title>
                <div class="text-overline mb-1">
                  Donkey Seranade
                </div>
              </div>
            </v-card-item>
          </v-card>
        </div>
    </v-flex>
  </div>
</template>

<script>
export default {
  name: 'HomeComponent',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.my-flex {
  display: flex;
  justify-content: center;
}
</style>
