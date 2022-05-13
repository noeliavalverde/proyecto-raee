<template>
  <h1>Alta lavadora</h1>


  <label for="id_machine">ID: </label>
  <input type="text" id="id_machine" v-model="washing_machine.id_machine">

  <label for="brand">Marca: </label>
  <input type="text" id="brand" v-model="washing_machine.observations.brand">

  <label for="model">Modelo: </label>
  <input type="text" id="model" v-model="washing_machine.observations.model">

  <label for="timestamp">Fecha: </label>
  <input type="date" id="timestamp" v-model="washing_machine.timestamp">

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
            washing_machine:{
                id_machine: "",
                employee: "",
                timestamp:"",
                event: "",
                observations: {
                    model:"",
                    brand:"",
                }
            }

        }
    },
    methods:{
        async addMachine(){
            this.washing_machine.event = "register"
            const settings={
                method:"POST",
                body:JSON.stringify(this.washing_machine),
                headers:{
                    "Content-Type":"application/json"
                },

            };
            
            await fetch("http://localhost:5000/api/process/register", settings);
            
            

        }
    },
}
</script>

<style>

</style>
