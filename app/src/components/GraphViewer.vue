<template>
    <div class="modal-overlay">
        <div class="modal">
            <h1 class="temp">HELOOOO</h1>
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
  export default {
    name: 'GraphViewer',
    methods: {
      close() {
        this.$emit('close');
      },
    },
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
  text-align: center;
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
</style>