<template>
<div class="row plain-element">
  <div class="row header">
        <div class="col-xs-0 col-sm-0 col-md-3 col-lg-2 text-left plain-element">
            <img src="@/assets/img/statistics.jpg" class="img responsive img-header">
        </div>
        <div class="col-xs-12 col-sm-12 col-md-8 col-lg-8 plain-element">
            <div class="row summary">
                 <div class="box">
                    <h5>Data Extraction </h5>
                    <h6>Scrape Springboardcourses.ie course data with Beautifulsoup4. Fix date formats and featurize skill column with Pandas.
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
</div>
</template>


<script>


export default {
  name: "CourseStatistics",
  components: {
  },

}
</script>