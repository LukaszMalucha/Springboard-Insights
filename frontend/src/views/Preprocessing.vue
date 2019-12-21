<template>
<div class="row plain-element">
  <RowHeader/>
  <div class="row banner">
        <div class="col-xs-0 col-sm-0 col-md-3 col-lg-2 text-left plain-element">
            <img src="https://springboard-analytics.s3-eu-west-1.amazonaws.com/static/img/preprocessing-banner.jpg" class="img responsive img-banner">
        </div>
        <div class="col-xs-12 col-sm-12 col-md-8 col-lg-6 plain-element">
            <div class="row summary">
                 <div class="box">
                    <h5>Data Extraction </h5>
                    <h6>Scrape Springboardcourses.ie course data with Beautifulsoup4. Then fix date formats and remove whitespaces.
                        Once it's ready, load extracted course data into connected database. </h6>

                    <form @submit.prevent="onSubmit">
                    <button class="btn btn-algorithm">
                      <span>Run Webcrawler</span>
                    </button>
                    </form>
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
          <th class="text-center" onclick="sortTable(2)">NFQ</th>
          <th class="text-center" onclick="sortTable(3)">ECTS Credits</th>
          <th class="text-center"  onclick="sortTable(4)">Mode</th>
          <th class="text-center" onclick="sortTable(5)">Deadline</th>
          <th class="text-center" onclick="sortTable(6)">Website</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="course in filteredList" :key="course.pk">
          <td class="col-course">{{ course.title }}</td>
          <td class="col-course text-center">{{ course.provider }}</td>
          <td class="text-center">{{ course.nfq }}</td>
          <td class="text-center">{{ course.ects_credits }}</td>
          <td class="text-center">{{ course.mode }}</td>
          <td class="text-center">{{ course.deadline }}</td>
          <td class="text-center"><a target="_blank" :href="course.link">Website</a></td>

        </tr>
        </tbody>
      </table>
       <div class="loader" id="courseLoader"></div>
    </div>
  </div>
</div>
</template>


<script>
import { apiService } from "@/common/api.service.js";
import RowHeader from "@/components/RowHeader.vue";
let endpoint = "/api/extract-data/";
export default {
  name: "Preprocessing",
  components: {
    RowHeader
  },
  data() {
    return {
      courseList: [],
      search: '',
    }
  },
  methods: {
    onSubmit() {
      document.getElementById("courseLoader").style.display = "block";

      apiService(endpoint)
      .then(data => {
        this.courseList = data.results;
        document.getElementById("courseLoader").style.display = "none";
      })
    },
  },
  computed: {
//  Search courses function
    filteredList() {
      return this.courseList.filter(course => {
        return course.title.toLowerCase().includes(this.search.toLowerCase()) ||
         course.provider.toLowerCase().includes(this.search.toLowerCase()) ||
         course.nfq.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  created() {
    document.title = "Course Data Extraction";
  }

}
</script>