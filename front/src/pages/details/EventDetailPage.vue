<template>
  <span class="pi ">
      <h1> Código: {{id}}</h1>
  </span>
  <div class="container">
        <table class="borde_tabla">
            <thead>
            Histórico
            </thead>
            <br>
            <tbody>
            <th class="id_machine">Código</th>
            <th>Proceso</th>
            <th>Empleado asignado</th>
            <th>Fecha</th>
            <th>Estado</th>
            <th></th>
            <tr>
                <td class="id_machine">{{event.id_machine}}</td>
                <td>{{event?.payload?.brand}}</td>
                <td>{{event?.payload?.model}}</td>
                <td class="employee">{{event.employee}}</td>
                <td>{{event.timestamp}}</td>
                <td>{{event.event}}</td>
                <td >
                <button class="info"> + Info</button>
                </td>
          </tr>
            
            </tbody>
            <tfoot class="foot">
            </tfoot>
        </table>
      </div>
</template>

<script>
export default {
    name:'DetailPage',
    props:['id'],
    data(){
        return{
            event: undefined

        }
    },
    created(){
        this.loadData()
    },
    methods:{
        async loadData(){
            const response = await fetch ('http://localhost:5000/api/process/' + this.id)
            this.event= await response.json()
            console.log(this.event)
        }
    }


}
</script>

<style>

</style>