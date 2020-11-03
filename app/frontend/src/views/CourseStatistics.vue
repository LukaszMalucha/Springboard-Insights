<template>
<div class="row plain-element">
  <MessageComponent/>
  <div class="row top-menu">
      <ul>
        <li>
          <router-link :to="{name: 'online-courses'}">Get Online Degree</router-link>
        </li>
       <li>
          <router-link :to="{name: 'fastest-diploma'}">The Fastest Diploma</router-link>
        </li>
        <li>
          <router-link :to="{name: 'fastest-bsc'}">The Fastest Bachelor</router-link>
        </li>
        <li>
          <router-link class="active" :to="{name: 'course-statistics'}">Course Statistics</router-link>
        </li>
        <li>
          <router-link :to="{name: 'preprocessing'}">Update Courses Data</router-link>
        </li>
      </ul>
  </div>
  <div class="dashboard-cards">
    <div class="row row-cards">
      <div class="col s12 m12 l6 plain-element text-center">
        <div class="card pyplot">
              <providers-chart  :chart-data="getProvidersChartData()" :styles="chartStyles"></providers-chart>
        </div>
      </div>
      <div class="col s12 m12 l6 plain-element text-center">
        <div class="card pyplot">
              <nfq-chart  :chart-data="getNfqChartData()" :styles="chartStyles"></nfq-chart>
        </div>
      </div>
    </div>
    <div class="row row-cards">
      <div class="col s12 m12 l3 plain-element text-left">
        <div class="card pyplot">
            <ects-chart  :chart-data="getEctsChartData()" :styles="chartStyles"></ects-chart>
        </div>
      </div>
      <div class="col s12 m12 l6 plain-element text-center">
        <div class="card pyplot">
            <category-chart  :chart-data="getCategoryChartData()" :styles="chartStyles"></category-chart>
        </div>
      </div>
      <div class="col s12 m12 l3 plain-element text-center">
        <div class="card pyplot">
            <mode-chart  :chart-data="getModeChartData()" :styles="chartStyles"></mode-chart>
        </div>
      </div>
    </div>
  </div>
</div>


</template>


<script>
import MessageComponent from "@/components/MessageComponent.vue";
import EctsChart from "@/common/EctsChart.js";
import ModeChart from "@/common/ModeChart.js";
import NfqChart from "@/common/NfqChart.js";
import ProvidersChart from "@/common/ProvidersChart.js";
import CategoryChart from "@/common/CategoryChart.js";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "CourseStatistics",
  components: {
    MessageComponent,
    EctsChart,
    ModeChart,
    NfqChart,
    ProvidersChart,
    CategoryChart,
  },
  data() {
    return {
    }
  },
  methods: {
    ...mapGetters(["getEctsChartData", "getModeChartData", "getNfqChartData",
                    "getProvidersChartData", "getCategoryChartData"]),
    ...mapActions(["statisticData"]),
    getStatisticData() {
      this.statisticData()

    }

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