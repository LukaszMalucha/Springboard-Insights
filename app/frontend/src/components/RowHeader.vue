<template>
      <div class="row top-menu">
          <ul>
            <li>
              <router-link :to="{name: 'preprocessing'}">Course Data Collection</router-link>
            </li>

            <li>
              <router-link :to="{name: 'online-courses'}">Online Degrees</router-link>
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
          </ul>
      </div>
</template>

<script>
export default {
    name: "RowHeaderComponent"
}

</script>