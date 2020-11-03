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
          <router-link :to="{name: 'course-statistics'}">Course Statistics</router-link>
        </li>
        <li>
          <router-link class="active" :to="{name: 'preprocessing'}">Update Courses Data</router-link>
        </li>
      </ul>
  </div>
  <div class="row banner">
    <div class="col s12 m12 l12 plain-element">
        <div class="row summary">
             <form @submit.prevent="dataExtraction">
                <button class="btn btn-algorithm">
                  <span>Update Courses</span>
                </button>
             </form>
        </div>
    </div>
  </div>
  <div class="dashboard-cards">
    <div class="row"></div>
    <div v-if="getMessage()"  class="row row-cards">
      <div class="col m9 l10 plain-element"></div>
      <div class="col m3 l2 plain-element">
        <div class="search-wrapper">
          <label> Search Course:</label>
          <input type="text" v-model="search"/>
        </div>
      </div>
    </div>
    <div  class="row row-cards">
      <table v-if="getMessage()" id="courseTable">
        <thead>
          <tr>
            <th onclick="sortTable(0)">Title</th>
            <th class="text-center" onclick="sortTable(1)">Provider</th>
            <th class="text-center" onclick="sortTableInt(2)">NFQ</th>
            <th class="text-center" onclick="sortTableInt(3)">ECTS Credits</th>
            <th class="text-center"  onclick="sortTable(4)">Mode</th>
            <th class="text-center" onclick="sortTableInt(5)">Deadline</th>
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
            <td class="text-center"><a target="_blank" :href="course.link"><i class="fas fa-external-link-alt"></i></a></td>
          </tr>
        </tbody>
      </table>
       <div class="loader" id="courseLoader"></div>
    </div>
  </div>
</div>
</template>


<script>
import { mapGetters, mapActions } from "vuex";

import MessageComponent from "@/components/MessageComponent.vue";


export default {
  name: "Preprocessing",
  components: {
    MessageComponent
  },
  data() {
    return {
      courseList: this.getCourses(),
      search: '',
      found: false,
    }
  },
  methods: {
    ...mapGetters(['getCourses', 'getError', 'getMessage']),
    ...mapActions(['clearMessages', 'extractData']),
    dataExtraction() {
      this.extractData()
    }
  },
  computed: {
//  Search courses function
    filteredList() {
      return this.getCourses().filter(course => {
        return course.title.toLowerCase().includes(this.search.toLowerCase()) ||
         course.provider.toLowerCase().includes(this.search.toLowerCase()) ||
         course.nfq.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  created() {
    this.clearMessages();
    document.title = "Course Data Extraction";
  }

}
</script>