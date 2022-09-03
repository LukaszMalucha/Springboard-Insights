<template>
<div class="row plain-element">
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
          <router-link :to="{name: 'preprocessing'}">Update Courses Data</router-link>
        </li>
      </ul>
  </div>
  <div class="row banner">
      <div class="row summary">
      <br><br>
        <div class="box">

          <h5>404 - Page Not Found</h5>
          <h6>HTTP 404 Error - The page you are were looking for appears to have been moved, deleted or does not exist.</h6>
        </div>
      </div>
    </div>
</div>
</template>


<script>

export default {
  name: "NotFound",
  components: {
  },
  data() {
    return {
      message: "404 - Page Not Found"
    }
  }
}
</script>