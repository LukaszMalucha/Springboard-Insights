from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

app_name = "api"

router = DefaultRouter()
# router.register("courses", views.CourseViewSet, basename="courses")

urlpatterns = [
    path("", include(router.urls)),
    path("extract-data", views.ExtractDataView.as_view(), name="extract-data"),
]
