from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Course
from api.serializers import CourseSerializer



COURSES_URL = reverse("api:courses-list")
EXTRACT_DATA_URL = reverse("api:extract-data-list")
COURSE_STATISTICS_URL = reverse("api:course-statistics")
FASTEST_DIPLOMA_URL = reverse("api:fastest-diploma")
FASTEST_BACHELOR_URL = reverse("api:fastest-bachelor")
ONLINE_COURSES_URL = reverse("api:online-courses")


class CoursesApiTests(TestCase):
    """Test courses api view"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_courses_list(self):
        """Test retrieving courses list"""
        Course.objects.create(
            title="test",
            provider="test",
            award="test",
            ects_credits="test",
            mode="test",
            deadline="test",
            start_date="test",
            end_date="test",
            nfq="test",
            ote_flag="test",
            link="test",
            skills="test",
            delivery="test",
        )
        Course.objects.create()

        companies = Course.objects.all()
        serializer = CourseSerializer(companies, many=True)
        response = self.client.get(COURSES_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_create_course_successful(self):


