<template>
   <Header />
   <div class="container">
      <div class="info-wrapper">
          <router-link to="/scrap-inform"><div class="pi pi-chevron-left"> </div> </router-link>
          <h3>Código ID: {{id}} | {{report[0].payload.brand}} | {{report[0].payload.model}} </h3>
          <div class="state-box">{{report[report.length - 1].event}}</div>
      </div>
         <div class="table-wrapper">
             <h4>HISTÓRICO</h4>
             <table>
                <thead>
                <th>Empleado asignado</th>
                <th>Fecha</th>
                <th>Estado</th>
                <th></th>
                </thead>
              
                <tbody>
                
                <tr v-for="item in report" :key="item.id">
                    <td class="employee">{{item.employee}}</td>
                    <td>{{item.timestamp}}</td>
                    <td>{{item.event}}</td>
                    <td><button class="info-btn"> + Info</button></td>
                </tr>
                </tbody>
             </table>
         </div>
      </div>
</template>

<script>
import Header from '@/components/Header.vue'
export default {
    name:'DetailPage',
    components: { Header },
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
  .container{
      min-height: 100vh;
      background-color: rgba(248,253,252);
  }
  .info-wrapper{
      color: black;
      display: flex;
      flex-direction: row;
      padding: 1.5em 1em;
      align-items: center;
  }
  .info-wrapper h3{
    font-size: 1.5em;
    font-weight: 200;
  }
  .pi-chevron-left{
      font-size: 1.8em;
      margin-right: 0.5em;
  }
  .state-box{
      background-color: black;
      color: white;
      font-size: 0.8em;
      padding: 0.8em 2em;
      border-radius: 5px;
      margin-left: 1em;
  }
  .table-wrapper{
      background-color: white;
      width: fit-content;
      border-radius: 7px;
      margin: 2em;
      padding: 1em;
  }
  .table-wrapper h4{
      text-align: left;
      padding: 0.8em;
      font-size: 0.8em;
  }
  .table-wrapper table{
      border-collapse: collapse;
      text-align: left;
      font-size: 0.8em;
  }
  .table-wrapper th{
      color: rgb(202, 199, 199);
      padding: 1em 0.8em;
      border-bottom: 1px solid #f0faf8;
      font-size: 0.8em;
      text-transform: uppercase;
  }
  .table-wrapper td{
      padding: 0.4em 0.8em;
      border-bottom: 1px solid #f0faf8;
  }
  .table-wrapper .info-btn{
    border: 1px solid rgba(62,219,147,255);
    background-color: white;
    color:rgba(62,219,147,255);
    padding: 0.3em 0.6em;
    border-radius: 5px;
}
   .table-wrapper .info-btn:hover{
    background-color: rgb(62,219,147);
    color:white;   
   }

</style>