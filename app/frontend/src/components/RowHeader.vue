<template>
  <div class="row header">
      <div class="row top-menu">
        <div class="col m1 l2">

        </div>
        <div class="col s12 m10 l8 plain-element">
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
            <li>
              <router-link :to="{name: 'fastest-bsc'}">The Fastest Bsc.</router-link>
            </li>
          </ul>
        </div>
        <div class="col m2 l2">

        </div>
      </div>
    </div>
</template>

<script>
export default {
    name: "RowHeaderComponent"
}

</script>