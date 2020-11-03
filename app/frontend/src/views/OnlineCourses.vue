<template>
<div class="row plain-element">
  <MessageComponent/>
  <div class="row top-menu">
      <ul>
        <li>
          <router-link class="active" :to="{name: 'online-courses'}">Get Online Degree</router-link>
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
          <router-link :to="{name: 'preprocessing'}">Update Courses Data</router-link>
        </li>
      </ul>
  </div>
  <div class="dashboard-cards">
    <div class="row"></div>
    <div class="row row-cards">
      <div class="col m9 l10 plain-element"></div>
      <div class="col m3 l2 plain-element">
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
          <th class="text-center" onclick="sortTableInt(2)">NFQ</th>
          <th class="text-center" onclick="sortTableInt(3)">Duration</th>
          <th class="text-center"  onclick="sortTable(4)">Mode</th>
          <th class="text-center" onclick="sortTableInt(5)">Deadline</th>
          <th class="text-center" onclick="sortTable(6)">Website</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="course in filteredList" :key="course.pk">
          <td class="col-course">{{ course[1]}}</td>
          <td class="col-course text-center">{{ course[2] }}</td>
          <td class="text-center">{{ course[9] }}</td>
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
import MessageComponent from "@/components/MessageComponent.vue";
import { mapGetters, mapActions } from "vuex";


export default {
  name: "OnlineCourses",
  components: {
    MessageComponent
  },
  data() {
    return {
      search: "",
    }
  },
  methods: {
    ...mapGetters(['getCourses', ]),
    ...mapActions(['fetchOnlineDegrees',]),
   },
  computed: {
//  Search courses function
    filteredList() {
      return this.getCourses().filter(course => {
        return course[1].toLowerCase().includes(this.search.toLowerCase()) ||
               course[2].toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  created() {
    this.fetchOnlineDegrees()
    document.title = "Online Courses";
  }
}
</script>