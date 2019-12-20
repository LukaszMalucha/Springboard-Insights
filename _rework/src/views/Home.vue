<template>
<div class="row plain-element">
  <div class="row row-break">

  </div>

  <div class="dashboard-cards">

    <div class="row row-title-cards">
        <div class="col-md-3">
            <div class="card menu-card">
                <div class="card-image">
                    <img src="@/assets/img/preprocessing.jpg" class="img responsive">
                </div>
                <div class="card-content">
                    <span class="card-title">Data Preprocessing</span>
                    <p>Preparing Dataset for future analytics with BS4 & Pandas.</p>
                </div>
                 <router-link class="btn btn-enter" :to="{ name: 'preprocessing' }">
                    <span>Continue <i class="far fa-arrow-alt-circle-right"></i></span>
                  </router-link>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card menu-card">
                <div class="card-image">
                    <img src="@/assets/img/statistics.jpg" class="img responsive">
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
        <div class="col-md-3">
            <div class="card menu-card">
                <div class="card-image">
                    <img src="@/assets/img/insights.jpg" class="img responsive">
                </div>
                <div class="card-content">
                    <span class="card-title">Courses Insights</span>
                    <p>Presenting critical data from the latest course offer.</p>
                </div>
                <button onclick="window.location=''" type="submit" class="btn btn-enter"><span>Continue <i class="far fa-arrow-alt-circle-right"></i></span></button>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card menu-card">
                <div class="card-image">
                    <img src="@/assets/img/insights.jpg" class="img responsive">
                </div>
                <div class="card-content">
                    <span class="card-title">Courses Insights</span>
                    <p>Presenting critical data from the latest course offer.</p>
                </div>
                <button onclick="window.location=''" type="submit" class="btn btn-enter"><span>Continue <i class="far fa-arrow-alt-circle-right"></i></span></button>
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