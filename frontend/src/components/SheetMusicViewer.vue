<template>
    <div class="hello">
        <img :src="imageSrc" alt="Image description">
    </div>
</template>
  
<script>
    export default {
        name: 'SheetMusicViewer',
        props: {
            path: String
        },
        computed: {
            imageSrc() {
                return require('../assets/sheets/'+ this.path.path);
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