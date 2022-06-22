<template>
<Header></Header>


    <section class="search-area">
        <h6>BÚSQUEDA Y FILTRADO</h6>

        <div class="search-input">
                
                <InputText type="text" v-model="filteredText" placeholder="Search" />
                <p>Busque una marca, modelo o codigo de maquina</p>
        </div>
        
        <div class="search-input">
            <Dropdown class="selected_event" v-model="selectedEvent" :options="events" optionLabel="name" placeholder="Select event" :filter="false">
                    <!-- <template>
                        <div v-for="item in events" :key="item.name" :value="item.name">{{item.name}}</div>
                    </template> -->
            </Dropdown>
            <p>Selecciona el estado de la maquina</p>
        </div>
        <div class="search-input">
                <InputText type="date" v-model="selectedDate" placeholder="Search" />
                <p>Selecciona la ultima fecha de actualizacion</p>
        </div>
       
        
    </section>
         
        <main class="main-container">
            <div class="table-wrapper">
                <h4>RESULTADOS</h4>
                <table>
                    <thead>
                    <th class="id_machine">Código</th>
                    <th>Marca</th>
                    <th>Modelo</th>
                    <th>Empleado</th>
                    <th>Fecha</th>
                    <th>Estado</th>
                    <th></th>
                    </thead>
                
                    <tbody>
                
                    <tr v-for="item in filteredReports" :key="item.id_machine">
                        <td class="id_machine">{{item.id_machine}}</td>
                        <td>{{item.brand}}</td>
                        <td>{{item.model}}</td>
                        <td class="employee">{{item.employee}}</td>
                        <td>{{item.timestamp}}</td>
                        <td>{{item.event}}</td>
                        <td >
                        <button class="btn" @click="this.$router.push({name: 'EventDetail', params:{id:item.id_machine}})"> + Info</button>
                        </td>
                    </tr>
                    </tbody>
                
                </table>
            </div>
         </main>
   

  <footer class="footer">
    <div class="div_footer"> © 2021 <span>Scrap</span>. Todos los derechos reservados </div>
  </footer>
  
</template>
<script>
import Header from '@/components/Header.vue'

export default {
    name:"ScrapInform",
    components: { Header },
    data() {
        return{
            reports:[],
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
       
    }
}

</script>

<style scoped>
.app{
    background-color: rgba(62,219,147,255);
}
.search-area{
    background-color: #f0faf8;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    padding: 3em;
    align-items: end;
    text-align: left;
    
}
.search-area h6{
    width: 100%;
    font-weight: bold;
    margin: 1.5em;
}

.search-area .search-input{
    
    font-size: 0.6em;
    margin-right: 2em;
    
}
.search-area p{
    
    margin-top: 1em;
}
.search-area input{
    border: 1px solid rgba(62,219,147,255);
}

.p-dropdown {
    border: 1px solid rgba(62,219,147,255);
}
.main-container{
    background-color: #f0faf8;
    padding-bottom: 3em;
}

.table-wrapper{
    background-color: white;
    width: 90%;
    margin: 0 auto;
    border-radius: 5px;
    padding: 1em;
    text-align: left;
}
.table-wrapper h4{
    margin-bottom: 2em;
}
.table-wrapper table{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.8em;
}

.table-wrapper td, th{
    padding: 0.6em 0;
    border-bottom: 1px solid #f0faf8;
}
.table-wrapper .employee{
    color: rgba(62,219,147,255);
    font-weight: bold;
}
.table-wrapper .btn{
    border: 1px solid rgba(62,219,147,255);
    background-color: white;
    color:rgba(62,219,147,255);
    padding: 0.3em 0.6em;
    border-radius: 5px;
}
footer{
    color: rgba(107,177,145,255);
    padding: 2.5em;
    text-align: left;
    font-size: 0.8em;
    background-color: rgba(248,253,252,255);
}

footer span{
    font-weight: bold;
}



</style>