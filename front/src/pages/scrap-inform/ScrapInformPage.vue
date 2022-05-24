<template>
    <ul class="layout">
        <li>SCRAP</li>
        <li @click="handleClick">DASHBOARD</li>
        <li @click="onClicked">MÁQUINAS</li>
    </ul>
    <div class="container">
        <table class="borde_tabla" v-show="displayMachine">
            <thead>
            Resultados
            </thead>
            <br>
            <tbody>
            <th class="id_machine">Código</th>
            <th>Marca</th>
            <th>Modelo</th>
            <th>Empleado</th>
            <th>Fecha</th>
            <th>Estado</th>
            <th></th>
            <tr v-for="item in reports" :key="item.id">

                <td class="id_machine">{{item.id_machine}}</td>
                <td>{{item.payload.brand}}</td>
                <td>{{item.payload.model}}</td>
                <td class="employee">{{item.employee}}</td>
                <td>{{item.timestamp}}</td>
                <td>{{item.event}}</td>
                <td >
                <button class="info" @click="moreInfo"> + Info</button>
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
    name:"ScrapInform",
    data() {
        return{
            reports:[],
            displayMachine: false,
        }
    },
    mounted(){
        this.loadData()
    },
    methods:{
        async loadData(){
            const response = await fetch ('http://localhost:5000/api/process/scrap_inform')
            this.reports= await response.json()
        },
        onClicked(){
            this.displayMachine = true

        }
    }

}

</script>

<style scoped>
.info{
    color:green;
}
.layout{
    display:flex;
    justify-content: flex-start;
}
li{
    margin:20px;
    list-style: none;
}
.container{
    width:100%;

}
table {
   width: 100%;
   border: 1px solid rgb(248, 238, 238);
   text-align: center;
   border-collapse: collapse;
   margin: fit-content;
   caption-side: top;
}
.employee {
    color: green;
}
button{
    border:solid 0.5px green;
  
    
}
th, td {
   border-bottom: 0.09px solid #999;
   }


</style>