from rest_framework.serializers import ModelSerializer
from .models import Topic
from replay.serializers import ReplaySerializer


class TopicSerializer(ModelSerializer):

    class Meta:

        model = Topic
        fields = '__all__'
