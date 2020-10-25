from rest_framework.serializers import ModelSerializer
from .models import Topic
from replay.serializers import ReplaySerializer

from account.serializers import AccountSerializer


class TopicSerializer(ModelSerializer):
    """ members = AccountSerializer(many=True, read_only=True) """
    class Meta:

        model = Topic
        fields = '__all__'
