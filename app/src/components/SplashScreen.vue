<template>
    <div :class="{ loader: true, fadeout: !isLoading }">
        <img src="../assets/logo.jpeg" 
        height="300"
        width="450"
        style="position: relative; justify-content: center;"/>
        <div class="bottom-div">
            <h3>Virtualoso</h3>
            <p style="font-style: italic; font-size: 20px;">{{musicFact[randomNum]}}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "LoadingScreen",
        
        props: {
            /**
             * Determines when to fade out the loading screen
             */
            isLoading: Boolean,
        },
        data() {
            return {
                musicFact: [],
                randomNum: 0
            }
        },
        created() {
            this.musicFact = [
                "If you can play it slowly, you can play it quickly",
                "Did you know that violins have strings?", 
                "Viola = big violin", 
                "Keyboard is not the same as Piano!", 
                "Charlie Puth has perfect pitch apparently.",
                "You need to practice 10,000 hours to master your instrument",
                "Geniuses are born, not created.",
                "-S A C R I L E G I O U S-",
                "I don’t want to BeReal, I want to BePracticing",
            ];
            let min = Math.ceil(0);
            let max = Math.floor(this.musicFact.length);
            this.randomNum = Math.floor(Math.random() * (max - min + 1)) + min;
            // console.log(this.musicFact.length);
        }
    };
</script>

<style>
.loader {
background-color: white;
bottom: 0;
color: rgb(102, 63, 168);
display: block;
font-size: 32px;
left: 0;
overflow: hidden;
padding-top: 10vh;
position: fixed;
right: 0;
text-align: center;
top: 0;
font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}

.fadeout {
  animation: fadeout 2s forwards;
}

@keyframes fadeout {
to {
    opacity: 0;
    visibility: hidden;
}
}

.bottom-div {
    position: fixed;
    bottom: 15%;
    width: 100%;
}
</style>

<docs>
LoadingScreen is the component that handles the loading screen that is seen initially when you load Virtualoso.
It contains the Virtualoso logo, the app name, and a music fun fact.
</docs>