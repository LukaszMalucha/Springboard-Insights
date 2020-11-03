import { apiService } from "@/common/api.service.js";

export default {
  extractData() {
    let endpoint = "/api/extract-data/"
    return apiService(endpoint)
  },
  onlineDegrees() {
    let endpoint = "/api/online-courses"
    return apiService(endpoint)
  },
  fastestDiploma() {
    let endpoint = "/api/fastest-diploma"
    return apiService(endpoint)
  },
  fastestBsc() {
    let endpoint = "/api/fastest-bachelor"
    return apiService(endpoint)
  },
  statisticalData() {
    let endpoint = "api/course-statistics"
    return apiService(endpoint)
  },
}