<template>
<div class="row plain-element">
  <RowHeader/>
  <div class="row banner">
    <div class="col-xs-0 col-sm-0 col-md-3 col-lg-2 text-left plain-element">
      <img src="https://springboard-analytics.s3-eu-west-1.amazonaws.com/static/img/statistics-banner.jpg" class="img responsive img-banner" >
    </div>
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-6 plain-element">
      <div class="row summary">
        <div class="box">
          <h5>Course Data Statistics</h5>
          <h6>Get a statistical insights derived through the analysis of the scraped Springboardcourses.ie data,
            Dashboard vizualizations are built with chart.js module.</h6>
        </div>

      </div>
    </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-cards">
      <div class="col-md-6 plain-element text-center">
        <div class="card pyplot">
              <providers-chart  :chart-data="providersChartData" :styles="chartStyles"></providers-chart>
        </div>
      </div>
      <div class="col-md-6 plain-element text-center">
        <div class="card pyplot">
              <nfq-chart  :chart-data="nfqChartData" :styles="chartStyles"></nfq-chart>
        </div>
      </div>
    </div>
    <div class="row row-cards">
      <div class="col-md-3 plain-element text-left">
        <div class="card pyplot">
            <ects-chart  :chart-data="ectsChartData" :styles="chartStyles"></ects-chart>
        </div>
      </div>
      <div class="col-md-6 plain-element text-center">
        <div class="card pyplot">
            <category-chart  :chart-data="categoryChartData" :styles="chartStyles"></category-chart>
        </div>
      </div>
      <div class="col-md-3 plain-element text-center">
        <div class="card pyplot">
            <mode-chart  :chart-data="modeChartData" :styles="chartStyles"></mode-chart>
        </div>
      </div>
    </div>
  </div>
</div>


</template>


<script>
import { apiService } from "@/common/api.service.js";
import RowHeader from "@/components/RowHeader.vue";
import EctsChart from "@/common/EctsChart.js";
import ModeChart from "@/common/ModeChart.js";
import NfqChart from "@/common/NfqChart.js";
import ProvidersChart from "@/common/ProvidersChart.js";
import CategoryChart from "@/common/CategoryChart.js";

let endpoint = "api/course-statistics";
export default {
  name: "CourseStatistics",
  components: {
    RowHeader,
    EctsChart,
    ModeChart,
    NfqChart,
    ProvidersChart,
    CategoryChart,
  },
  data() {
    return {
      top_providers_dict: {},
      lt50_dict: {},
      nfq_dict: {},
      mode_dict: {},
      category_dict: {},
      ectsChartData: {},
      modeChartData: {},
      nfqChartData: {},
      providersChartData: {},
      categoryChartData: {},
    }
  },
  methods: {
    getStatisticData() {
      apiService(endpoint)
        .then(data =>{
          this.top_providers_dict = data.top_providers_dict;
          this.lt50_dict = data.lt50_dict;
          this.nfq_dict = data.nfq_dict;
          this.mode_dict = data.mode_dict;
          this.category_dict = data.category_dict;
          this.fillEctsChart();
          this.fillModeChart();
          this.fillNfqChart();
          this.fillProvidersChart();
          this.fillCategoryChart();

        })
    },
    fillEctsChart() {
      var dataset = this.lt50_dict
      var dataLabels = Object.keys(dataset)
      var dataValues = Object.values(dataset)
      this.ectsChartData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#4e79a7", "#f28e2b"],
            data: dataValues
          }
        ]
      }
    },
    fillModeChart() {
      var dataset = this.mode_dict
      var dataLabels = Object.keys(dataset)
      var dataValues = Object.values(dataset)
      this.modeChartData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#4e79a7", "#f28e2b"],
            data: dataValues
          }
        ]
      }
    },
    fillNfqChart() {
      var dataset = this.nfq_dict
      var dataLabels = Object.keys(dataset)
      var dataValues = Object.values(dataset)
      this.nfqChartData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ['#3e6085', '#7193b8','#94aeca','#c9d6e4','#c9d6e4','#c9d6e4' ],
            data: dataValues
          }
        ]
      }
    },
    fillProvidersChart() {
      var dataset = this.top_providers_dict
      var dataLabels = Object.keys(dataset)
      var dataValues = Object.values(dataset)
      this.providersChartData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#4e79a7", '#f28e2b', '#e15759','#76b7b2','#59a14f','#b07aa1' ],
            data: dataValues
          }
        ]
      }
    },
    fillCategoryChart() {
      var dataset = this.category_dict
      var dataLabels = Object.keys(dataset)
      var dataValues = Object.values(dataset)
      this.categoryChartData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#4e79a7", '#f28e2b', '#e15759','#76b7b2','#59a14f','#b07aa1'],
            data: dataValues
          }
        ]
      }
    },
  },
  computed: {
    chartStyles () {
      return {
        height: `100%`,
        position: "relative"
      }
    }
  },
  created() {
    this.getStatisticData();
    document.title = "Springboard Courses statistics";
  }

}
</script>