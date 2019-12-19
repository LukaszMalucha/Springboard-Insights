import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import NotFound from "./views/NotFound.vue";
import Preprocessing from "./views/Preprocessing.vue";
import CourseStatistics from "./views/CourseStatistics.vue";

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
