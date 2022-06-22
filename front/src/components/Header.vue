<template>
  <div id="nav">
    <router-link to="/" class="btn logo">SCRAP</router-link>
    <router-link to="/scrap-inform" class="btn">MÁQUINAS</router-link>
    <router-link to="/manager-inform" class="btn">DASHBOARD</router-link>
  </div>
</template>


<script>


export default {
  name: "Header",

}
</script>

<style scoped>
#nav {
  padding: 30px 30px 0 3em;
  display: flex;
  flex-direction: row;
  font-size: 0.8em;
  
}
#nav a {
  
  color: black;
  margin-right: 2em;
  padding-bottom: 1em;
}

#nav a.router-link-exact-active {
  color: rgba(62,219,147,255);
  border-bottom: 2px solid rgba(62,219,147,255);

}
.logo{
  width: 20%;
  text-align: left;
}


</style>