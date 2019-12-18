from rest_framework import viewsets, status, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api import serializers
from api.utils import data_extractor
from db_manager.utils import database_upload
from core.models import Course
from core.permissions import IsAdminOrReadOnly


class CourseViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminOrReadOnly)
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

    def get(self, request):
        # try:
        courses = data_extractor()
        database_upload(courses)
        #
        # except:
        #     return Response({'message': "Invalid Request"},
        #                     status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": str(courses)})
