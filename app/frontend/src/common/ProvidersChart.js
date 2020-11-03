import { HorizontalBar, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: HorizontalBar,
  mixins: [reactiveProp],
  data(){
    return {
      options: {
        responsive: true,
        maintainAspectRatio: false,
        title: {
            fontSize: 14,
            fontColor: 'black',
            display: true,
            text: 'Top Course Providers',
            fontFamily: 'Play, sans-serif',
        },
        scales: {
          xAxes: [{
              gridLines: {
                  color: "rgba(0, 0, 0, 0)",
                  zeroLineColor: "rgba(0, 0, 0, 0)",
              },
              ticks: {
                fontSize: 10,
                suggestedMin: 0,
                beginAtZero: true,
                fontFamily: 'Play, sans-serif',
              }
          }],
          yAxes: [{
              gridLines: {
                  color: "rgba(0, 0, 0, 0)",
                  zeroLineColor: "rgba(0, 0, 0, 0)",
              },
              ticks: {
                fontSize: 10,
                stepSize: 10,
                suggestedMin: 0,
                beginAtZero: true,
                fontFamily: 'Play, sans-serif',
              }
          }],

        },
        legend: {
          display: false
        },
        tooltips: {
          enabled: true,
          callbacks: {
            label: function(tooltipItem,data) {
              return data['datasets'][0]['data'][tooltipItem['index']] + " courses";
            },
          }
        }
      }
    }
  },
  mounted () {
    this.renderChart(
      this.chartData,
      this.options
      )
  }
}
