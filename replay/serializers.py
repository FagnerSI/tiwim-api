from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Replay


class ReplaySerializer(ModelSerializer):
    image_details = Base64ImageField()
    class Meta:

        model = Replay
        fields = '__all__'


class ReplaySerializerAll(ModelSerializer):

    class Meta:

        model = Replay
        fields = '__all__'
        depth = 1
