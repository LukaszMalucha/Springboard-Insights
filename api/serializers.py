from rest_framework import serializers
from core.models import Course



class CourseSerializer(serializers.ModelSerializer):
    """Serializer for Springboard courses"""

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('id',)






