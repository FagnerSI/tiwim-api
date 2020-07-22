from rest_framework.serializers import ModelSerializer
from .models import Replay


class ReplaySerializer(ModelSerializer):

    class Meta:

        model = Replay
        fields = '__all__'


class ReplaySerializerAll(ModelSerializer):

    class Meta:

        model = Replay
        fields = '__all__'
        depth = 1
