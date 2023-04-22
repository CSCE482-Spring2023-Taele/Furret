<template>
    <div class="modal-overlay">
        <div class="modal">
            <canvas id="myChart"></canvas>
        </div>
        <div class="close">
          <v-btn icon="mdi-close-circle"
            class="btn-close"
            @click="close"
            >      
          </v-btn>
        </div>
    </div>
</template>

<script>
  import output from "raw-loader!../assets/bruh.txt";
  import Chart from 'chart.js/auto';
  export default {
    name: 'GraphViewer',
    data() {
      return {
        userData: [],
        sheetData: [],
        notes: []
      }
    },
    methods: {
      close() {
        this.$emit('close');
      },
    },
    created() {
      console.log('created hook called');
      let user = false;
      let sheet = false;
      output.split('\n').forEach(element => {
        let val0 = element.split(' ')[0];
        let val1 = element.split(' ')[1];
        let val2 = element.split(' ')[2];
        if (val0 === "User") {
          user = true;
          sheet = false;
        }
        else if (val0 === "Sheet") {
          user = false;
          sheet = true;
        }
        if (user && !isNaN(val0) && !isNaN(val1)) {
          this.userData.push({x: [val0, val1], y: val2});
          if (this.notes.indexOf(val2) === -1) {
            this.notes.push(val2);
          }
        }
        if (sheet && !isNaN(val0) && !isNaN(val1)) {
          this.sheetData.push({x: [val0, val1], y: val2});
          if (this.notes.indexOf(val2) === -1) {
            this.notes.push(val2);
          }
        }
      });
      // console.log(this.userData);
    },
    mounted() {
      console.log('mounted hook called');
      const ctx = document.getElementById('myChart');
      const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: this.notes,
            datasets: [{
                label: 'Sheet Notes',
                data: this.sheetData,
                borderWidth: 1,
                barPercentage: 0.5,
            },
            {
                label: 'User Notes',
                data: this.userData,
                borderWidth: 1,
                barPercentage: 0.5,
            },
          ]
        },
        options: {
          indexAxis: 'y',
          scales: {
            x: {
              min: 0,
              title: {
                  display: true,
                  text: 'Time (s)'
                }
            },
            y: {
                title: {
                  display: true,
                  text: 'Notes'
                }
                
            }
          }
        }
    });
    myChart;
    }
  };
</script>

<style>
.modal-overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  background-color: #000000da;
}
.modal {
  background-color: white;
  height: 75%;
  width: 75%;
  padding: 60px 0;
  margin-top: 10%;
  margin-left: 20%;
}
.close {
  margin: 10% 0 0 10px;
  cursor: pointer;
}
.temp {
    color: blue;
}
.btn-close {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
#myChart {
  display: block;
  margin: 0 auto;
  width: 100%;
}
</style>