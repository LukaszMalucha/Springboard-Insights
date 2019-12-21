from rest_framework import viewsets, status, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api import serializers
from api.utils import data_extractor
from db_manager.utils import database_upload
from core.models import Course
from core.permissions import IsAdminOrReadOnly
from api.utils import statistical_data, fastest_diploma, fastest_bachelor, online_courses


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        return queryset.order_by('-title')

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExtractDataView(views.APIView):
    # serializer_class = serializers.CourseSerializer
    # queryset = Course.objects.all()

    def get(self, request):
        # try:
        courses = data_extractor()
        # except:
        #     return Response({'message': "Invalid Request - error while extracting website data"},
        #                     status=status.HTTP_400_BAD_REQUEST)
        # try:
        #     database_upload(courses)
        # except:
        #     return Response({'message': "Invalid Request - error while uploading to database"},
        #                     status=status.HTTP_400_BAD_REQUEST)
        # queryset = self.queryset

        # return queryset.order_by('-title')
        return Response({'results': courses})


class CourseStatisticsView(views.APIView):

    def get(self, request):
        statistics = statistical_data()

        return Response(statistics)


class FastestDiplomaView(views.APIView):

    def get(self, request):
        queryset = Course.objects.all().filter(nfq="8")
        results = fastest_diploma(queryset)

        return Response(results)


class FastestBachelorView(views.APIView):

    def get(self, request):
        queryset = Course.objects.all()
        results = fastest_bachelor(queryset)

        return Response(results)


class OnlineCoursesView(views.APIView):

    def get(self, request):
        queryset = Course.objects.all()
        results = online_courses(queryset)

        return Response(results)
