<template>
  <div class="row header">
      <div class="row top-menu">
        <div class="col-md-1 col-lg-2">

        </div>
        <div class="col-sm-12 col-md-10 col-lg-8 plain-element">
          <ul>
            <li>
              <router-link :to="{name: 'preprocessing'}">Data Extraction</router-link>
            </li>
            <li>
              <router-link :to="{name: 'course-statistics'}">Course Statistics</router-link>
            </li>
            <li>
              <router-link :to="{name: 'online-courses'}">Online Degrees</router-link>
            </li>
           <li>
              <router-link :to="{name: 'fastest-diploma'}">The Fastest Diploma</router-link>
            </li>
              <router-link :to="{name: 'fastest-bsc'}">The Fastest Bsc.</router-link>
          </ul>
        </div>
        <div class="col-md-2 col-lg-2">

        </div>
      </div>
    </div>
</template>

<script>
export default {
    name: "RowHeaderComponent"
}

</script>