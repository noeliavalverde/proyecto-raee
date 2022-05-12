<template>
  <h1>Alta lavadora</h1>


  <label for="id_machine">ID: </label>
  <input type="text" id="id_machine" v-model="washing_machine.id_machine">

  <label for="brand">Marca: </label>
  <input type="text" id="brand" v-model="washing_machine.brand">

  <label for="model">Modelo: </label>
  <input type="text" id="model" v-model="washing_machine.model">

  <label for="register_date">Fecha: </label>
  <input type="date" id="register_date" v-model="washing_machine.register_date">

  <label for="employee">Operario: </label>
  <input type="text" id="employee" v-model="washing_machine.employee">
<!--   
    <select v-model="selectedUser">
        <option :value="null" disabled>Selecciona un operario: </option>
        <option>
        operario 1
        </option>
        <option>
        operario 2
        </option>
    </select> -->
    <button id="addButton" @click="addMachine">Registrar</button>
    

</template>

<script>
export default {
    data(){
        return{
            washing_machine:{}

        }
    },
    methods:{
        async addMachine(){
            const settings={
                method:"POST",
                body:JSON.stringify(this.washing_machine),
                headers:{
                    "Content-Type":"application/json"
                },

            };
            console.log("clickAddMachine", JSON.stringify(this.washing_machine))
            await fetch("http://localhost:5000/api/process/register", settings);
            
            

        }
    },
}
</script>

<style>

</style>
