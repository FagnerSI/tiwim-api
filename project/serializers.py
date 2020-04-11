from rest_framework.serializers import ModelSerializer
from .models import Project


class ProjectSerializer(ModelSerializer):
    """  topics = TopicSerializer(many=True, read_only=True) """
    class Meta:

        model = Project
        fields = '__all__'
        """ depth = 1 """
