
<template>
  <div class="home">
    <img src="@/assets/img/machine-icon.png" alt="">
    <h2>WELCOME</h2>
    <router-link to="/scrap-inform" class="btn">ACCEDER</router-link>
    
    
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
     
    }
  },

}
</script>

<style scoped>
.home{
  background-color: rgba(248,253,252);
  min-height: 100vh;
}
img{
  width: 30%;
  max-width: 250px;
  display: block;
  margin: 0 auto;
  padding: 3em 0 2em;}

.btn{
  padding: 1em 2.5em;
  border: 2px solid rgba(62,219,147);
  background-color: rgba(62,219,147);
  border-radius: 5px;
  color: rgba(248,253,252);
  font-weight: bold;
  margin: 3em auto;
  display: block;
  width: fit-content;
}
.btn:hover{
  color: rgba(62,219,147);
  background-color: rgba(248,253,252);
}
</style>