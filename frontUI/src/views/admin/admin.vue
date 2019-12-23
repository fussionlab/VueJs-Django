<template>
    <div class="wrapper">
        <SideBar  id="sidebar" :class="isActive?'active':''" ></SideBar>
            <div class="flex flex-holder">
            <button type="button" id="sidebarCollapse" :class="isActive?'navbar-btn border-0 active':'navbar-btn border-0'" @click="sideBarCollapse()">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <svg width="40px"><path fill="#0a505b" d="M40,0H0v40C0,17.9,17.9,0,40,0z"/></svg>
            <span class="curve" @click="switchVisibleControl()"><i :class="switchVisible===true?'fa fa-angle-down text-center p-md-2 m-1':'fa fa-angle-up text-center p-md-2 m-1'"></i></span>
            <div class="switch" v-if="switchVisible">
                <span :class="'fadeIn bg-color-'+v" v-for="v in val" :key="v" @click="colorChanger(v)"></span>
            </div>
            </div>
        <div id="content" class="pt-5 pr-5 mr-5 ml-5">
         <h2 :class="'color-'+colorChange">Collapsible Sidebar Using Bootstrap 4</h2>
            <div class="row">
                <div class="col-md-8 mb-5 mb-xl-0">
                    <div  class="card bg-dark">
                        <div slot="header" class="row align-items-center m-2">
                            <div class="col">
                                <h6 class="text-light text-uppercase ls-1 mb-1">Overview</h6>
                                <h5 class="h3 text-white mb-0">Total Posts</h5>
                            </div>
                            <div class="col">
                                <ul class="nav nav-pills justify-content-end">
                                    <li class="nav-item mr-2 mr-md-0">
                                        <a class="nav-link py-2 px-3"
                                           href="#"
                                           :class="{active: bigLineChart.activeIndex === 0}"
                                           @click.prevent="initBigChart(0)">
                                            <span class="d-none d-md-block text-light">Month</span>
                                            <span class="d-md-none">M</span>
                                        </a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link py-2 px-3"
                                           href="#"
                                           :class="{active: bigLineChart.activeIndex === 1}"
                                           @click.prevent="initBigChart(1)">
                                            <span class="d-none d-md-block text-light">Week</span>
                                            <span class="d-md-none">W</span>
                                        </a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <line-chart :height="350" ref="bigChart" :chart-data="bigLineChart.chartData" :extra-options="bigLineChart.extraOptions">
                        </line-chart>

                    </div>
                </div>
                <div class="col-md-4">
                    <ul>Recent Posts
                        <li></li>
                    </ul>
                    
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import SideBar from '@/components/sideBar'
import * as chartConfigs from '@/components/Charts/config';
import LineChart from '@/components/Charts/LineChart';
export default {
    name:'Admin',
    components:{
        SideBar,
        LineChart,
    },
    data(){

    return{
        isActive:false,
        switchVisible:false,
        val:4,
        colorChange:0,
        bigLineChart: {
          allData: [
            [0, 20, 10, 30, 15, 40, 20, 60, 60],
            [0, 20, 5, 25, 10, 30, 15, 40, 40]
          ],
          activeIndex: 0,
          chartData: {
            datasets: [],
            labels: [],
          },
          extraOptions: chartConfigs.blueChartOptions,
        },
        
    }
    },
    mounted() {
      this.initBigChart(0);
    },
    computed:{

    },
    methods:{
        sideBarCollapse:function(){
            let active = this.isActive
            if(active)
              this.isActive = false
            else if(active===false)
              this.isActive = true
        },
        switchVisibleControl:function(){
            let active = this.switchVisible
            if(active)
              this.switchVisible = false
            else 
              this.switchVisible = true
        },
        colorChanger:function(vals){
            //alert(vals);
            return this.colorChange = vals;
        },
        initBigChart(index) {
        let chartData = {
          datasets: [
            {
              label: 'Performance',
              data: this.bigLineChart.allData[index]
            }
          ],
          labels: ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        };
        this.bigLineChart.chartData = chartData;
        this.bigLineChart.activeIndex = index;
      }
    }
}
</script>
<style lang="scss">

     .wrapper {
        display: flex;
        align-items: stretch;
         a, a:hover, a:focus {
            color: inherit;
            text-decoration: none;
            transition: all 0.3s;
        }
        #sidebar {
            min-width: 250px;
            max-width: 250px;
            height:100vh;
        }

        #sidebar.active {
            margin-left: -250px;
        }
        #sidebarCollapse {
            width: 40px;
            height: 40px;
            background: #0a505b;
            
        }

        #sidebarCollapse span {
            width: 80%;
            height: 2px;
            margin: 0 auto;
            display: block;
            background: #ffffff;
            transition: all 0.8s cubic-bezier(0.810, -0.330, 0.345, 1.375);
        }
        #sidebarCollapse span:first-of-type {
            /* rotate first one */
            transform: rotate(45deg) translate(2px, 2px);
        }
        #sidebarCollapse span:nth-of-type(2) {
            /* second one is not visible */
            opacity: 0;
        }
        #sidebarCollapse span:last-of-type {
            /* rotate third one */
            transform: rotate(-45deg) translate(1px, -1px);
        }
        #sidebarCollapse.active span {
            /* no rotation */
            transform: none;
            /* all bars are visible */
            opacity: 1;
            margin: 5px auto;
        }
        .flex-holder{
            width:40px !important;
        }
        .curve {
            width: 40px;
            height: 40px;
            display: block;
            background:#0a505b;
            color: #ffffff;
        }
        .switch{
            display:grid;
            width:40px !important;
            background-color: #0a505b;
            span{
                width:40px !important;
                height:40px;
            }
            
        }
        #content{
            margin: 10px;
           
        } 
    }
     
</style>