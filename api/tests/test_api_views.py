from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Course
from api.serializers import CourseSerializer
from django.contrib.auth import get_user_model

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
            ects_credits="12",
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
        self.assertEqual(response.data["count"], 2)

    def test_create_course_successful(self):
        """Test create new course"""
        self.superuser = get_user_model().objects.create_superuser(
            "test@gmail.com",
            "testpass"
        )
        self.client.force_authenticate(self.superuser)
        payload = {"title": "test course"}
        self.client.post(COURSES_URL, payload)
        exist = Course.objects.filter(
            title=payload["title"],
        ).exists()
        self.assertTrue(exist)


class ExtractDataViewTests(TestCase):
    """Testing data extraction functionality"""

    def setUp(self):
        self.client = APIClient()

    def test_accessing_extract_data_view(self):
        """Accessing extract data view"""
        Course.objects.create(
            title="test",
            provider="test",
            award="test",
            ects_credits="12",
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

        response = self.client.get(EXTRACT_DATA_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['count'] > 1)


class CourseStatisticsViewTests(TestCase):
    """Testing course statistics view functionality"""

    def setUp(self):
        self.client = APIClient()

    def test_accessing_course_statistics_view(self):
        """Accessing course statistics view"""
        Course.objects.create(
            title="test",
            provider="test",
            award="test",
            ects_credits="12",
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

        response = self.client.get(COURSE_STATISTICS_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['top_providers_dict'], {'test': 1})

    def test_accessing_online_courses_empty_view(self):
        """Accessing view with no matching query"""
        Course.objects.create()
        response = self.client.get(COURSE_STATISTICS_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FastestDiplomaViewTests(TestCase):
    """Testing fastest diploma view functionality"""

    def setUp(self):
        self.client = APIClient()

    def test_accessing_fastest_diploma_view(self):
        """Accessing fastest diploma view"""

        Course.objects.create(
            title="Higher Diploma in Data",
            provider="Institute of Technology",
            award="Higher Diploma",
            ects_credits="12",
            mode="Full Time",
            deadline="2019/09/20",
            start_date="2019/09/23",
            end_date="2021/05/31",
            nfq="8",
            ote_flag="Yes",
            link="test",
            skills="test",
            delivery="Online",
        )
        response = self.client.get(FASTEST_DIPLOMA_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data[0]) > 1)

    def test_accessing_online_courses_empty_view(self):
        """Accessing view with no matching query"""
        Course.objects.create()
        response = self.client.get(FASTEST_DIPLOMA_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])


class FastestBachelorViewTests(TestCase):
    """Testing fastest bachelor view functionality"""

    def setUp(self):
        self.client = APIClient()

    def test_accessing_fastest_bachelor_view(self):
        """Accessing fastest bachelor view"""

        Course.objects.create(
            title="Higher Bachelor in Data",
            provider="Institute of Technology",
            award="Higher Diploma",
            ects_credits="12",
            mode="Full Time",
            deadline="2019/09/20",
            start_date="2019/09/23",
            end_date="2021/05/31",
            nfq="8",
            ote_flag="Yes",
            link="test",
            skills="test",
            delivery="Online",
        )
        response = self.client.get(FASTEST_BACHELOR_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data[0]) > 1)

    def test_accessing_online_courses_empty_view(self):
        """Accessing view with no matching query"""
        Course.objects.create()
        response = self.client.get(FASTEST_BACHELOR_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])


class OnlineCoursesViewTests(TestCase):
    """Testing online courses view functionality"""

    def setUp(self):
        self.client = APIClient()

    def test_accessing_online_courses_view(self):
        """Accessing online courses view"""

        Course.objects.create(
            title="Higher Bachelor in Data",
            provider="Institute of Technology",
            award="Higher Diploma",
            ects_credits="12",
            mode="Full Time",
            deadline="2019/09/20",
            start_date="2019/09/23",
            end_date="2021/05/31",
            nfq="8",
            ote_flag="Yes",
            link="test",
            skills="test",
            delivery="Online",
        )
        response = self.client.get(ONLINE_COURSES_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data[0]) > 1)

    def test_accessing_online_courses_empty_view(self):
        """Accessing view with no matching query"""
        Course.objects.create()
        response = self.client.get(ONLINE_COURSES_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
