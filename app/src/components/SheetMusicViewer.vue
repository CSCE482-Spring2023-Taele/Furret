<template>
    <div class="hello">
        <img :src="imageSrc" alt="Image description">
    </div>
</template>
  
<script>
    export default {
        name: 'SheetMusicViewer',
        props: {
            /**
             * Receives the path of sheet music file from SongScreenComponent to display sheet music
             */
            path: String
        },
        computed: {
            imageSrc() {
                return require('../../src-tauri/resources/sheets/'+ this.path.path);
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
img {
    height:75%;
    width:75%;
    display: block;
    margin: 0 auto;
}
</style>

<docs>
SheetMusicViewer component handles display of sheet music on the song screen page.
</docs>