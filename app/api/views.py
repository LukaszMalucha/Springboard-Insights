from rest_framework import viewsets, status, views
from rest_framework.response import Response

from api import serializers
from api.utils import data_extractor
from api.utils import statistical_data, fastest_diploma, fastest_bachelor, online_courses
from core.models import CourseModel


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CourseSerializer
    queryset = CourseModel.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        return queryset.order_by('-title')

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExtractDataViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CourseSerializer
    queryset = CourseModel.objects.all()

    def get_queryset(self):
        try:
            data_extractor()
        except:
            pass
        queryset = self.queryset

        return queryset.order_by('-title')


class CourseStatisticsView(views.APIView):

    def get(self, request):
        statistics = statistical_data()

        return Response(statistics)


class FastestDiplomaView(views.APIView):

    def get(self, request):
        queryset = CourseModel.objects.all().filter(nfq="8")
        results = fastest_diploma(queryset)

        return Response(results)


class FastestBachelorView(views.APIView):

    def get(self, request):
        queryset = CourseModel.objects.all()
        results = fastest_bachelor(queryset)

        return Response(results)


class OnlineCoursesView(views.APIView):

    def get(self, request):
        queryset = CourseModel.objects.all()
        results = online_courses(queryset)

        return Response(results)
