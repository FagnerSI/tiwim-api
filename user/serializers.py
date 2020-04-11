from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    # projects = UsersProjectsSerializer(many=True, read_only=True)
    class Meta:

        model = User
        """ exclude = ['is_active'] """
        fields = '__all__'
