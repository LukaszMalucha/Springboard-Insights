import Vuex from 'vuex';
import Vue from 'vue';
import courses from './modules/courses';

// Connect Vue with Vuex
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    courses
  }
});