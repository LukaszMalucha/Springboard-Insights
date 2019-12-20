<template>
<div class="row plain-element">
  <RowHeader/>
  <div class="row banner">
    <div class="col-xs-0 col-sm-0 col-md-3 col-lg-2 text-left plain-element">
      <img src="@/assets/img/404-banner.jpg" class="img responsive img-banner">
    </div>
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-8 plain-element">
      <div class="row summary">
        <div class="box">
          <h5>404 - Page Not Found</h5>
          <h6>HTTP 404 Error - The page you are were looking for appears to have been moved, deleted or does not exist.</h6>
        </div>

      </div>
    </div>
  </div>
</div>
</template>


<script>
import RowHeader from "@/components/RowHeader.vue";

export default {
  name: "NotFound",
  components: {
    RowHeader,
  },
  data() {
    return {
      message: "404 - Page Not Found"
    }
  }
}
</script>