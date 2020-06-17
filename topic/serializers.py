from rest_framework.serializers import ModelSerializer
from .models import Topic


class TopicSerializer(ModelSerializer):
    """  replays = ReplaySerializer(many=True, read_only=True) """

    class Meta:

        model = Topic
        fields = '__all__'
