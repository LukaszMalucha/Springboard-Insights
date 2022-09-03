<template>
<div class="row plain-element">
  <div class="row row-break">

  </div>

  <div class="dashboard-cards">

    <div class="row row-title-cards">
         <div class="col s12 m4 l3">
            <div class="card menu-card">
                <div class="card-image">
                    <img src="https://springboard-analytics.s3-eu-west-1.amazonaws.com/static/img/online-degree.jpg" class="img responsive">
                </div>
                <div class="card-content">
                    <span class="card-title">Online Degrees</span>
                    <p>Presenting online degrees from the latest course offer.</p>
                </div>
                <router-link class="btn btn-enter" :to="{ name: 'online-courses' }">
                    <span>Continue <i class="far fa-arrow-alt-circle-right"></i></span>
                </router-link>
            </div>
        </div>
        <div class="col s12 m4 l3">
            <div class="card menu-card">
                <div class="card-image">
                    <img src="https://springboard-analytics.s3-eu-west-1.amazonaws.com/static/img/preprocessing.jpg" class="img responsive">
                </div>
                <div class="card-content">
                    <span class="card-title">Fast Bachelor</span>
                    <p>Fast Bachelor degrees available in the latest Springboard offer.</p>
                </div>
                 <router-link class="btn btn-enter" :to="{ name: 'fastest-bsc' }">
                    <span>Continue <i class="far fa-arrow-alt-circle-right"></i></span>
                  </router-link>
            </div>
        </div>


        <div class="col s12 m4 l3">
            <div class="card menu-card">
                <div class="card-image">
                    <img src="https://springboard-analytics.s3-eu-west-1.amazonaws.com/static/img/insights.jpg" class="img responsive">
                </div>
                <div class="card-content">
                    <span class="card-title">Fast Diploma</span>
                    <p>Fast Diplomas available in the latest Springboard offer.</p>
                </div>
                <router-link class="btn btn-enter" :to="{ name: 'fastest-diploma' }">
                    <span>Continue <i class="far fa-arrow-alt-circle-right"></i></span>
                </router-link>
            </div>
        </div>
        <div class="col s12 m4 l3">
            <div class="card menu-card">
                <div class="card-image">
                    <img src="https://springboard-analytics.s3-eu-west-1.amazonaws.com/static/img/statistics.jpg" class="img responsive">
                </div>
                <div class="card-content">
                    <span class="card-title">Courses Statistics</span>
                    <p>Latest Springboard.ie course offer's. With Chart.js</p>
                </div>
                <router-link class="btn btn-enter" :to="{ name: 'course-statistics' }">
                    <span>Continue <i class="far fa-arrow-alt-circle-right"></i></span>
                </router-link>
            </div>

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
}
</script>