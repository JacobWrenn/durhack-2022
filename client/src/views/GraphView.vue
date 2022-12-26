<template>
    <img :src="require('../assets/durhack logo.png')" class="logo">
    <button class="button" @click="refresh">Refresh Data</button>
    <img :src="require('../assets/backbutton.png')" class="backbutton" @click="$router.push('/')">
    <img src="http://161.35.171.24:5000/co2graph" class="co2graph">
</template>

<script>
export default {
    name: "GraphView",
    methods: {
        async refresh() {
      await fetch("161.35.171.24:5000/refresh")
      window.location.reload()
        }
    }
}
</script>

<style scoped>
.button {
  left: 140px;
  bottom: 0px;
  position: fixed;
  font-size: 3em;
  transform: translateX(-50%);
}
.backbutton {
  left: 0%;
  top: 0%;
  display: block;
  margin: 1em;
  width: 5em;
  position: fixed;
  cursor: pointer;
}
.logo {
  right: 0%;
  top: 0%;
  display: block;
  width: 6em;
  position: fixed;
  }

.co2graph {
  margin: auto;
  display: block;
  width: 1000px;
}

</style>