from rest_framework import serializers

from core.models import CourseModel


class CourseSerializer(serializers.ModelSerializer):
    """Serializer for Springboard courses"""

    class Meta:
        model = CourseModel
        fields = '__all__'
        read_only_fields = ('id',)






