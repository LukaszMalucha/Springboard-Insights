from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

app_name = "api"

router = DefaultRouter()
router.register("courses", views.CourseViewSet, basename="courses")
router.register("extract-data", views.ExtractDataViewSet, basename="extract-data")


urlpatterns = [
    path("", include(router.urls)),
    path("course-statistics/", views.CourseStatisticsView.as_view(), name="course-statistics"),
    path("fastest-diploma/", views.FastestDiplomaView.as_view(), name="fastest-diploma"),
    path("fastest-bachelor/", views.FastestBachelorView.as_view(), name="fastest-bachelor"),
    path("online-courses/", views.OnlineCoursesView.as_view(), name="online-courses")
]
