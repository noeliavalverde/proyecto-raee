<template>
    <div>
        <ul class="layout">
            <li>MANAGER</li>
            <li @click="handleClick">DASHBOARD</li>
        </ul>
    </div>
    <br>
      <div class="home" v-show="displayCharts">
    <div class="search-input">report <InputText class="input_date" type="date" v-model="selectedChartsDate"/></div>
      <br>
      <br>
      <br>
  <div class="individual_chartline">
    <Chart type="line" id="chartline" :data="lineData" :options="AxisOptions"/>
    <Chart type="line" id="chartline" :data="secondLineData" :options="secondAxisOptions" />
    <Chart type="line" id="chartline" :data="thirdlineData" :options="thirdAxisOptions" />
    <Chart type="line" id="chartline" :data="forthLineData" :options="forthAxisOptions" />
  </div>
  <br><br><br>
   <div class="chart_doughnut_line">
     <Chart type="line" id="chart_line" :data="lineStylesData" :options="multiAxisOptions" />
     <Chart type="doughnut" id="doughnut" :data="doughnutData" :options="lightOptions" />
   </div>
   <footer class="footer">
    <div class="div_footer"> 2021 Scrap todos los derechos reservados </div>
  </footer>
  </div>
</template>
<script>
export default {
    name:"ManagerPage",
    data() {
        return{
            dataReport:'',
            reports:[],
            displayCharts: true,
            selectedChartsDate:'',
            lineStylesData: {
              labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
              datasets: [
                  {
                      label: 'First Dataset',
                      data: [65, 59, 80, 81, 56, 55, 40],
                      fill: false,
                      tension: .4,
                      borderColor: '#42A5F5'
                  },
                  {
                      label: 'Second Dataset',
                      data: [28, 48, 40, 19, 86, 27, 90],
                      fill: false,
                      borderDash: [5, 5],
                      tension: .4,
                      borderColor: '#66BB6A'
                  },
                  {
                      label: 'Third Dataset',
                      data: [12, 51, 62, 33, 21, 62, 45],
                      fill: false,
                      borderColor: '#FFA726',
                      tension: .4,
                      backgroundColor: 'rgba(255,167,38,0.2)'
                  }
              ]
          },
        multiAxisOptions:{
                stacked: false,
                plugins: {
                    legend: {
                        labels: {
                            color: '#495057'
                        }
                    }
                },
                scales: {
                    x: {
                        ticks: {
                            display: false
                        },
                        grid: {
                            display:false,
                            drawBorder: false
                        }
                    },
                    y: {
                        type: 'linear',
                        display: true,
                        position: 'left',
                        ticks: {
                            color: '#495057'
                        },
                        grid: {
                            display:false,
                            drawBorder: false
                        }
                    },
                    y1: {
                        type: 'linear',
                        display: true,
                        position: 'right',
                        ticks: {
                            display: false
                        },
                        grid: {
                            display:true,
                            color: '#f5f4f0',
                            drawBorder: false
                        }
                    }
              }
        },
        lineData: {
              labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
              datasets: [
                  {
                      label: 'first Dataset',
                      data: [12, 51, 62, 33, 21, 62, 45],
                      fill: true,
                      borderDash: [5, 5],
                      borderColor: '#FFA726',
                      tension: .4,
                      backgroundColor: 'rgba(255,167,38,0.2)'
                  }
                  
              ]
          },
        AxisOptions:{
                stacked: false,
                plugins: {
                    legend: {
                        labels: {
                            color: '#495057'
                        }
                    }
                },
                scales: {
                    x: {
                        ticks: {
                            display: false
                        },
                        grid: {
                            display:false,
                            drawBorder: false
                        }
                    },
                    y: {
                        type: 'linear',
                        display: true,
                        position: 'left',
                        ticks: {
                            display: false
                        },
                        grid: {
                            display:false,
                            drawBorder: false
                        }
                    },
                    y1: {
                        type: 'linear',
                        display: true,
                        position: 'right',
                        ticks: {
                            display: false
                        },
                        grid: {
                            display:false,
                            drawBorder: false
                        }
                    }
              }
        },
        secondLineData: {
              labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
              datasets: [
                 {
                      label: 'second Dataset',
                      data: [65, 59, 80, 81, 56, 55, 40],
                      fill: true,
                      tension: .4,
                      borderColor: '#42A5F5'
                  },
                  
              ]
          },
        secondAxisOptions:{
                stacked: false,
                plugins: {
                    legend: {
                        labels: {
                            color: '#495057'
                        }
                    }
                },
                scales: {
                    x: {
                        ticks: {
                            display: false
                        },
                        grid: {
                            display:false,
                            drawBorder: false
                        }
                    },
                    y: {
                        type: 'linear',
                        display: true,
                        position: 'left',
                        ticks: {
                            display: false
                        },
                        grid: {
                            display:false,
                            drawBorder: false
                        }
                    },
                    y1: {
                        type: 'linear',
                        display: true,
                        position: 'right',
                        ticks: {
                            display: false
                        },
                        grid: {
                            display:false,
                            drawBorder: false
                        }
                    }
              }
        },
        thirdlineData: {
              labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
              datasets: [
                  {
                      label: 'third Dataset',
                      data: [28, 48, 40, 19, 86, 27, 90],
                      fill: true,
                      borderDash: [5, 5],
                      tension: .4,
                      borderColor: '#66BB6A'
                  },
                  
              ]
          },
        thirdAxisOptions:{
                stacked: false,
                plugins: {
                    legend: {
                        labels: {
                            color: '#495057'
                        }
                    }
                },
                scales: {
                    x: {
                        ticks: {
                            display: false
                        },
                        grid: {
                            display:false,
                            drawBorder: false
                        }
                    },
                    y: {
                        type: 'linear',
                        display: true,
                        position: 'left',
                        ticks: {
                            display: false
                        },
                        grid: {
                            display:false,
                            drawBorder: false
                        }
                    },
                    y1: {
                        type: 'linear',
                        display: true,
                        position: 'right',
                        ticks: {
                            display: false
                        },
                        grid: {
                            display:false,
                            drawBorder: false
                        }
                    }
              }
        },
        forthLineData: {
              labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
              datasets: [
                  {
                      label: 'Third Dataset',
                      data: [12, 51, 10, 33, 21, 9, 45],
                      fill: true,
                      borderColor: '#033363',
                      tension: .4,
                      backgroundColor: '#f0ca24'
                  }
                  
              ]
          },
        forthAxisOptions:{
                stacked: false,
                plugins: {
                    legend: {
                        labels: {
                            color: '#495057'
                        }
                    }
                },
                scales: {
                    x: {
                        ticks: {
                            display: false
                        },
                        grid: {
                            display:false,
                            drawBorder: false
                        }
                    },
                    y: {
                        type: 'linear',
                        display: true,
                        position: 'left',
                        ticks: {
                            display: false
                        },
                        grid: {
                            display:false,
                            drawBorder: false
                        }
                    },
                    y1: {
                        type: 'linear',
                        display: true,
                        position: 'right',
                        ticks: {
                            display: false
                        },
                        grid: {
                            display:false,
                            drawBorder: false
                        }
                    }
              }
        },
        doughnutData: {
                labels: this.data,
                datasets: [
                    {
                        label: 'porcentajes',
                        data: this.data,
                        backgroundColor: ["#FF6384","#36A2EB","#FFCE56"],
                        hoverBackgroundColor: ["#FF6384","#36A2EB","#FFCE56"]
                    }
                ]
            },
			lightOptions: {
				plugins: {
                    legend: {
                        labels: {
                            color: '#495057'
                        }
                    }
                }
			},
              
        }
    },
    mounted(){
        this.loadData()
    },
 
    methods:{
        async loadData(){
            const response = await fetch ('http://localhost:5000/api/analysis/number_of_machines_in_each_event')
            this.data= await response.json()
            this.dataReport= Object.values(this.data)
            console.log(this.dataReport)
        },
        handleClick(){
            this.displayCharts= true
            this.displayMachine = false
        },
        onClicked(){
            this.displayCharts= false
            this.displayMachine = true
        },
        counter_timestamp(){
          
            const mapMonthDay= this.reports.map((x)=>{
                return new Date(x.timestamp).getMonth()
            })
            const sumPerMonth= mapMonthDay.reduce(function (count, x){
                //console.log(count ,x)
                //count[x]= count[x] === undefined ? 1 :  count[x] + 1
                if (count[x] === undefined) {
                    count[x] = 1
                } else {
                    count[x] = count[x] + 1
                }
                return count
            }, {})
            console.log(sumPerMonth)
            console.log(Object.values(sumPerMonth))
            
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
/* *{
  background-color: rgb(192, 245, 245);
} */
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