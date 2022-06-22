<template>
    <div>
        <ul class="layout">
            <li>SCRAP</li>
            <li @click="handleClick">DASHBOARD</li>
            <li @click="onClicked">MÁQUINAS</li>
        </ul>
    </div>
    <br>
    <section v-show="displayMachine">
        <div class="BUSQUEDA_Y_FILTRADO_div">
            <h6 class="BUSQUEDA_Y_FILTRADO">BUSQUEDA Y FILTRADO</h6>
        </div>
        <br>
        <span class="p-input-icon-left">
                <i class="pi pi-search" />
                <InputText type="text" v-model="filteredText" placeholder="Search" />
        </span>
        <span class="p-input">Busque una marca, modelo o codigo de maquina</span>
        <Dropdown class="selected_event" v-model="selectedEvent" :options="events" optionLabel="name" placeholder="Select event" :filter="false">
                <template>
                    <div v-for="item in events" :key="item.name" :value="item.name">{{item.name}}</div>
                </template>
        </Dropdown>
        <span class="selected_option">Selecciona el estado de la maquina</span>
        <span class="p-input-icon-right">
                <InputText type="date" v-model="selectedDate" placeholder="Search" />
        </span>
       
        <span class="selected_date">Selecciona la ultima fecha de actualizacion</span>
        <br><br><br><br>
        <div class="container">
            <table class="borde_tabla">
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
                <tr v-for="item in filteredReports" :key="item.id_machine">
                    <td class="id_machine">{{item.id_machine}}</td>
                    <td>{{item.brand}}</td>
                    <td>{{item.model}}</td>
                    <td class="employee">{{item.employee}}</td>
                    <td>{{item.timestamp}}</td>
                    <td>{{item.event}}</td>
                    <td >
                    <button class="info" @click="this.$router.push({name: 'EventDetail', params:{id:item.id_machine}})"> + Info</button>
                    </td>
                </tr>
       
                </tbody>
                <tfoot class="foot">
                </tfoot>
            </table>
          </div>
    </section>

  <footer class="footer">
    <div class="div_footer"> 2021 Scrap todos los derechos reservados </div>
  </footer>
  
</template>
<script>
export default {
    name:"ScrapInform",
    data() {
        return{
            reports:[],
            displayMachine: true,
            filteredText: '',
            selectedEvent:'',
            selectedDate:'',
            events:[
              {'name': 'all'},
              {'name': 'register'},
              {'name': 'diagnostic_in'},
              {'name': 'repair_in'},
              {'name': 'test_in'},
              {'name': 'register'},
              {'name': 'despiece'},
              {'name': 'finished'},
            ],
        }
    },
    
    mounted(){
        this.loadData()
    },
    computed:{
       filteredReports(){
        let result = this.reports.filter((item)=> this.isFilteredByText(item))
                                 .filter((item)=> item.timestamp.startsWith(this.selectedDate))
                                 .filter((item) => this.isFilteredByEvent(item))
        return result
       }
        
    },
    methods:{
        isFilteredByText(item) {
            return item.employee.toLowerCase().includes(this.filteredText.toLowerCase())||
                    item.id_machine.toLowerCase().includes(this.filteredText.toLowerCase())||
                    item.brand.toLowerCase().includes(this.filteredText.toLowerCase())||
                    item.model.toLowerCase().includes(this.filteredText.toLowerCase())
        },

        isFilteredByEvent(item) {
            if (this.selectedEvent == ""){ 
                return true
            }
            if (this.selectedEvent['name'].includes("all")){ 
                return true
            } else{
                
                return this.selectedEvent['name'].includes(item.event)
            }
        },
        
        filterReportsByDate(reports){
            let result= []
            for (const item of reports){
                if(item.timestamp.startsWith(this.selectedDate)){
                    result.push(item)
                }
            }
            return result
        },

        async loadData(){
            const response = await fetch ('http://localhost:5000/api/analysis/supply_line_current_state')
            this.reports= await response.json()
            
        },
        handleClick(){
            this.displayMachine = false
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

#chart_line{
  width: 75%;
  border: solid transparent;
  background-color: white;
}
#chartline{
  width: 24%;
  background-color: rgba(255, 255, 255, 0.932);
}
.individual_chartline{
  display: flex;
  justify-content: space-between;
}
.chart_doughnut_line{
  display: flex;
  justify-content:space-between;
}
#doughnut{
  margin-left: 2em;
  border: solid transparent;
  background-color: white;
  padding: 1em;
  width: 25%;
}

.div_footer{
  display: flex;
  justify-content: left;
  border: solid white;
}
.search-input{
  text-align: right;
}
.p-input-icon-left{
    position: absolute;
    top: auto;
    left: 1em;
}
.selected_event{
    position: absolute;
    top: auto;
    left: 18em;
}
.p-input-icon-right{
    position: absolute;
    top: auto;
    left: 28em;
}
.p-input{
    position: absolute;
    top: 17em;
    left: 2em;
    font-size:10px;
}
.selected_option{
    position: absolute;
    top: 17em;
    left: 28em;
    font-size:10px;
}
.selected_date{
    position: absolute;
    top: 17em;
    left: 45em;
    font-size:10px;
}
.BUSQUEDA_Y_FILTRADO{
    position: absolute;
    top: 8em;
    left: 2em;
}
</style>