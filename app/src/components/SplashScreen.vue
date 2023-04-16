<template>
    <div :class="{ loader: true, fadeout: !isLoading }">
        <img src="../assets/logo.jpeg" 
        height="300"
        width="450"
        style="position: relative; justify-content: center;"/>
        <div class="bottom-div">
            <h3>Virtualoso</h3>
            <p style="font-style: italic; font-size: 20px;">Did you know that violins have strings?</p>
        </div>
    </div>
</template>

<script>
export default {
name: "LoadingScreen",
props: ["isLoading"]
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
