<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer">
      <!--  -->
      <v-sheet
        color="grey-lighten-3"
        class="pa-4"
      >
        <v-list>
          <v-list-item
            prepend-avatar="http://cdn.shopify.com/s/files/1/1419/7120/products/Lycoris_Red_Radiata.SHUT.jpg?v=1571439604"
            title="Not Senhe"
            subtitle="senhehao@senhehao.com"
          ></v-list-item>
        </v-list>
      </v-sheet>
      <v-list>
        <v-list-group v-for="folder in folders" :key="folder.name" :value="folder.name">
          <template v-slot:activator="{ props }">
            <v-list-item
              v-bind="props"
            >{{folder.name}}</v-list-item>
          </template> 
          <v-list-item v-for="(song, i) in folder.songs" :key="i" link>
              <v-list-item-title v-text="song"></v-list-item-title>
          </v-list-item>
        </v-list-group>
      </v-list>
      <div class="my-button-container">
        <v-btn 
            color="primary" 
            rounded 
            dark 
            :loading="isSelecting" 
            @click="handleFileImport"
        >
            Upload Sheet Music
        </v-btn>

        <input 
            ref="uploader" 
            class="d-none" 
            type="file" 
            @change="onFileChanged"
        >
      </div>
    </v-navigation-drawer>

    <v-app-bar
      color="primary"
    >
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>{{title}}</v-toolbar-title>
      
      <v-btn @click="toggleComponent('HelloWorld')" icon>
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <v-btn @click="toggleComponent('Settings')" icon>
        <v-icon>mdi-cog</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <!--  -->
      <component v-if="activeComponent" :is="activeComponent"></component>
    </v-main>
  </v-app>
</template>

<style>
.nav-btns {
    float: left !important;
}
.my-button-container {
  position: fixed;
  bottom: 5px;
  left: 0;
  width: 100%;
  text-align: center;
}
</style>

<script>
import HelloWorld from './HelloWorld.vue'
import Settings from './SettingsPage.vue'

export default {
  components: {
    Settings,
    HelloWorld,
  },
  data: () => ({ 
    drawer: null, 
    title: "Home",
    folders: [
      { 
        name: 'Favorites',
        songs: ['Donkey Serenade', 'Never Gonna Give You Up', 'We Are Number One']  
      },
      { 
        name: 'Bangers',
        songs: ['Shooting Stars', 'Into the Night', 'Take On Me', 'Roundabout', 'Megalovania']
      },
      { 
        name: 'Classical',
        songs: ['Moonlight Sonata', 'Turkish March', 'Croatian Rhapsody']
      },
      { 
        name: 'Akash\'s Genshin Stash',
        songs: ['Rex Incognito', 'Swirls of the Stream', 'A Memorable Fancy', 'Moon Like Smile']
      },
    ],
    activeComponent: 'HelloWorld',
    isSelecting: false,
    selectedFile: null
  }),
  methods: {
    toggleComponent(componentName) {
      this.activeComponent = componentName;
    },
    handleFileImport() {
      this.isSelecting = true;

      // After obtaining the focus when closing the FilePicker, return the button state to normal
      window.addEventListener('focus', () => {
          this.isSelecting = false
      }, { once: true });
      
      // Trigger click on the FileInput
      this.$refs.uploader.click();
    },
    onFileChanged(e) {
        this.selectedFile = e.target.files[0];

        // Do whatever you need with the file, like reading it with FileReader
    },
  },
}
</script>
