<template>
   <div>
        <ul class="layout">
            <li>SCRAP</li>
            <li @click="handleClick">DASHBOARD</li>
            <li @click="onClicked">MÁQUINAS</li>
        </ul>
    </div>
  <span>
      <h1 class="pi pi-chevron-left"> Código ID: {{id}} | {{report[0].payload.brand}} | {{report[0].payload.model}} <span class="state_span">{{report[report.length - 1].event}}</span></h1>

  </span>
  <div class="container">
        <table class="borde_tabla">
            <thead>
            </thead>
            <br>
            <tbody>
            <th>Empleado asignado</th>
            <th>Fecha</th>
            <th>Estado</th>
            <th></th>
            <tr v-for="item in report" :key="item.id">
                <td class="employee">{{item.employee}}</td>
                <td>{{item.timestamp}}</td>
                <td>{{item.event}}</td>
                <td><button class="info"> + Info</button></td>   
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
            report: {},
            

        }
    },
    created(){
        this.loadData()
    },
    methods:{
        async loadData(){
            const response = await fetch ('http://localhost:5000/api/process/' + this.id)
            this.report= await response.json()
            console.log(this.report)
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
h1{
    font-size:x-large;
    font-weight: 500;
    color:black;
}
.state_span{
    height: 20px;
    background-color: black;
    font-size: 1em;
    color:white;
    padding:0.5em;
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
   margin:auto;
   caption-side: top;
}
.employee {
    color: green;
}
th, td {
   border-bottom: 0.09px solid #999;
   }
</style>