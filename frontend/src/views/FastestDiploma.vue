<template>
<div class="row plain-element">
  <RowHeader/>
  <div class="row banner">
    <div class="col-xs-0 col-sm-0 col-md-3 col-lg-2 text-left plain-element">
      <img src="https://springboard-analytics.s3-eu-west-1.amazonaws.com/static/img/diploma-banner.jpg" class="img responsive img-banner">
    </div>
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-8 plain-element">
      <div class="row summary">
        <div class="box">
          <h5>The Fastest Diploma</h5>
          <h6>Most lucrative jobs often require a master's degree. Springboard offers several options through which you can earn diploma
              leading to qualifications in areas where there are employment opportunities in the economy.</h6>
        </div>
      </div>
    </div>
  </div>
  <div class="dashboard-cards">
    <div class="row"></div>
    <div class="row row-cards">
      <div class="col-md-10 col-lg-10 plain-element"></div>
      <div class="col-md-2 col-lg-2 plain-element">
        <div class="search-wrapper">
          <label> Search Course:</label>
          <input type="text" v-model="search"/>
        </div>
      </div>
    </div>
    <div class="row row-cards">
       <table id="courseTable">
        <thead>
        <tr>
          <th onclick="sortTable(0)">Title</th>
          <th class="text-center" onclick="sortTable(1)">Provider</th>
          <th class="text-center" onclick="sortTable(2)">Duration</th>
          <th class="text-center"  onclick="sortTable(4)">Mode</th>
          <th class="text-center" onclick="sortTable(5)">Deadline</th>
          <th class="text-center" onclick="sortTable(6)">Website</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="course in courses" :key="course.pk">
          <td class="col-course">{{ course[1]}}</td>
          <td class="col-course text-center">{{ course[2] }}</td>
          <td class="text-center">{{ course[15]}} Days</td>
          <td class="text-center">{{ course[5] }}</td>
          <td class="text-center">{{ course[6] }}</td>
          <td class="text-center"><a target="_blank" :href="course[11]">Website</a></td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</template>


<script>
import RowHeader from "@/components/RowHeader.vue";
import { apiService } from "@/common/api.service.js";

let endpoint = "api/fastest-diploma";

export default {
  name: "FastestDiploma",
  components: {
    RowHeader,
  },
  data() {
    return {
      search: "",
      courses: []
    }
  },
  methods: {
    getCoursesData() {
      apiService(endpoint)
        .then(data => {

          this.courses = data
        })
      }
   },
   filters: {
      truncate (value, limit) {
          if (value.length > limit) {
              value = value.substring(0, limit) + "...";
          }
          return value
      }
  },
  computed: {
//  Search courses function
    filteredList() {
      return this.courseList.filter(course => {
        return course.title.toLowerCase().includes(this.search.toLowerCase()) ||
               course.provider.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  created() {
    this.getCoursesData()
    document.title = "Fastest Diplomas";
  }
}
</script>