<template>
  <div class="hello">
    <h1 style="display: flex; justify-content: center;">Welcome to Virtualoso!</h1>
    <v-flex class="my-flex">
        <div class="text-center">
          <v-card class="d-flex align-center justify-center" color="info" style="width: 100%;">
            <v-card-item>
              <div>
                <v-card-title>Last Played</v-card-title>
                <div class="text-overline mb-1">
                  {{latestSong}}
                </div>
              </div>
            </v-card-item>
          </v-card>
        </div>
    </v-flex>
  </div>
</template>

<script>
  import Chart from 'chart.js/auto';
import Database from "tauri-plugin-sql-api";

  export default {
    name: 'HomeComponent',
    data() {
      return {
        latestSong: "",
        scoreList: [],
        yRange: [],
        x: []
      }
    },
    created() {
//      this.latestSong = "Glimpse of Us";
//      this.scoreList = []; // get this from database where songname == this.latestSong
//      for (let i = 1; i <= this.scoreList.length; i++) {
//        this.x.push(i);
      this.updatelatestplay();
    },
    mounted() {
    },
    methods: {
      async updatelatestplay() {
        this.scoreList = [];
        this.x = [];
        const db = await Database.load("sqlite:data.db");
        await db.select("SELECT song, scoreid FROM scores_table ORDER BY scoreid DESC LIMIT 1;").then((response) => { 
          console.log(response);
          console.log(response[0].song);
          db.select("SELECT name FROM songs_table WHERE song_id = " + response[0].song + ";").then((response2) => { console.log(response2); this.latestSong = response2[0].name });
          db.select("SELECT * FROM scores_table WHERE song = " + response[0].song + ";").then((response2) => {
            console.log(response2);
            response2.forEach((x) => {console.log(x.score); this.scoreList.push(x.score);
            });
            for (let i = 1; i <= this.scoreList.length; i++) {
              console.log(i);
              this.x.push(i);
            }
          });
        });
      }
    },
    computed: {
      chartData() {
        return {
          labels: this.x,
          datasets: [
            {
              label: 'Scores over time',
              data: this.scoreList,
              borderWidth: 1,
              fill: true,
            },
          ]
        }
      }
    },
    watch: {
      chartData: function () {
        const ctx = document.getElementById('myChart');
        const myChart = new Chart(ctx, {
          type: 'line',
          data: this.chartData,
          options: {
            indexAxis: 'x',
            scales: {
              x: {
                title: {
                  display: true,
                  text: 'Attempt',
                  font: {
                    size: 15,
                  },
                },
                ticks: {
                  font: {
                    weight: 'bold',
                    size: 15
                  }
                },
                grid: {
                  color: '#b8b0b0',
                  lineWidth: 0.2
                }
              },
              y: {
                beginAtZero: true,
                title: {
                  display: true,
                  text: 'Score',
                  font: {
                    size: 15,
                  } 
                },
                ticks: {
                  font: {
                    weight: 'bold',
                    size: 15
                  }
                },
                grid: {
                  color: '#b8b0b0',
                  lineWidth: 0.2
                }
              },
            },
            plugins: {
              legend: {
                  labels: {
                      font: {
                          style: 'bold',
                          weight: '600',
                      }
                  }
              }
            }
          }
      });
      myChart;
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
#myChart {
  display: block;
  margin: 0 auto;
  width: 100%;
}
</style>
