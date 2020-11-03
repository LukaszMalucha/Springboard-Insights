import api from "../../api/api.js";


const state = {
  courses: [],
  error: null,
  message: null,
  ectsChartData: {},
  modeChartData: {},
  nfqChartData: {},
  providersChartData: {},
  categoryChartData: {},

}

const getters = {
  getCourses: state => state.courses,
  getError: state => state.error,
  getMessage: state => state.message,
  getEctsChartData: state => state.ectsChartData,
  getModeChartData: state => state.modeChartData,
  getNfqChartData: state => state.nfqChartData,
  getProvidersChartData: state => state.providersChartData,
  getCategoryChartData: state => state.categoryChartData,
};


const actions = {
  clearMessages({ commit }) {
    commit("setError", null);
    commit("setMessage", null);
  },
  async fetchOnlineDegrees({ commit }) {
      const response = await api.onlineDegrees();
      commit("setCourses", response);
  },
  async fetchFastestDiploma({ commit }) {
      const response = await api.fastestDiploma();
      commit("setCourses", response);
  },
  async fetchFastestBsc({ commit }) {
      const response = await api.fastestBsc();
      commit("setCourses", response);
  },
  async extractData({ commit }) {
    document.getElementById("courseLoader").style.display = "block";
    try {
      const response = await api.extractData();
      commit("setCourses", response.results);
      commit("setError", null);
      commit("setMessage", "Course Data extracted successfully.");
      document.getElementById("alertSuccess").style.display = "block";
      setTimeout(() => document.getElementById("alertSuccess").style.display = "none", 5000);
    } catch (error) {
      window.console.log(error);
      commit("setError", "Error while extracting Springboard data.");
      document.getElementById("alert").style.display = "block";
      setTimeout(() => document.getElementById("alert").style.display = "none", 5000);
      commit("setMessage", null);
    }
    document.getElementById("courseLoader").style.display = "none"
  },
  async statisticData({ dispatch }) {
    const response = await api.statisticalData();
    dispatch ("fillEctsChart", response.lt50_dict);
    dispatch ("fillModeChart", response.mode_dict);
    dispatch ("fillNfqChart", response.nfq_dict);
    dispatch ("fillProvidersChart", response.top_providers_dict);
    dispatch ("fillCategoryChart", response.category_dict);

  },
  fillEctsChart({ commit }, dataset) {
    const dataLabels = Object.keys(dataset)
    const dataValues = Object.values(dataset)
    const ectsChartData = {
      labels: dataLabels,
      datasets: [
        {
          backgroundColor: ["#4e79a7", "#f28e2b"],
          data: dataValues
        }
      ]
    }
    commit("setEctsChartData", ectsChartData)
  },
  fillModeChart({ commit }, dataset) {
    const dataLabels = Object.keys(dataset)
    const dataValues = Object.values(dataset)
    const modeChartData = {
      labels: dataLabels,
      datasets: [
        {
          backgroundColor: ["#4e79a7", "#f28e2b"],
          data: dataValues
        }
      ]
    }
    commit("setModeChartData", modeChartData)
  },
  fillNfqChart({ commit }, dataset) {
    const dataLabels = Object.keys(dataset)
    const dataValues = Object.values(dataset)
    const nfqChartData = {
      labels: dataLabels,
      datasets: [
        {
          backgroundColor: ['#3e6085', '#7193b8','#94aeca','#c9d6e4','#c9d6e4','#c9d6e4' ],
          data: dataValues
        }
      ]
    }
    commit("setNfqChartData", nfqChartData)
  },
  fillProvidersChart({ commit }, dataset) {
    const dataLabels = Object.keys(dataset)
    const dataValues = Object.values(dataset)
    const providersChartData = {
      labels: dataLabels,
      datasets: [
        {
          backgroundColor: ["#4e79a7", '#f28e2b', '#e15759','#76b7b2','#59a14f','#b07aa1' ],
          data: dataValues
        }
      ]
    }
    commit("setProvidersChartData", providersChartData)
  },
  fillCategoryChart({ commit }, dataset) {
    const dataLabels = Object.keys(dataset)
    const dataValues = Object.values(dataset)
    const categoryChartData = {
      labels: dataLabels,
      datasets: [
        {
          backgroundColor: ["#4e79a7", '#f28e2b', '#e15759','#76b7b2','#59a14f','#b07aa1'],
          data: dataValues
        }
      ]
    }
    commit("setCategoryChartData", categoryChartData)
  },

}


const mutations = {
  setCourses: (state, courses) => {
    state.courses = courses;
  },
  setError: (state, error) => {
    state.error = error;
  },
  setMessage: (state, message) => {
    state.message = message;
  },
  setEctsChartData: (state, ectsChartData) => {
    state.ectsChartData = ectsChartData;
  },
  setModeChartData: (state, modeChartData) => {
    state.modeChartData = modeChartData;
  },
  setNfqChartData: (state, nfqChartData) => {
    state.nfqChartData = nfqChartData;
  },
  setProvidersChartData: (state, providersChartData) => {
    state.providersChartData = providersChartData;
  },
  setCategoryChartData: (state, categoryChartData) => {
    state.categoryChartData = categoryChartData;
  },



}

export default {
  state,
  getters,
  actions,
  mutations
}