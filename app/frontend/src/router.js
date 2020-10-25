import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import OnlineCourses from "./views/OnlineCourses.vue";
import FastestDiploma from "./views/FastestDiploma.vue";
import FastestBsc from "./views/FastestBsc.vue";
import CourseStatistics from "./views/CourseStatistics.vue";
import Preprocessing from "./views/Preprocessing.vue";
import NotFound from "./views/NotFound.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/preprocessing",
      name: "preprocessing",
      component: Preprocessing
    },
    {
      path: "/online-courses",
      name: "online-courses",
      component: OnlineCourses
    },
    {
      path: "/fastest-diploma",
      name: "fastest-diploma",
      component: FastestDiploma
    },
    {
      path: "/fastest-bsc",
      name: "fastest-bsc",
      component: FastestBsc
    },
    {
      path: "/course-statistics",
      name: "course-statistics",
      component: CourseStatistics
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound,
    },
  ]
});
