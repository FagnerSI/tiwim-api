from rest_framework import authentication, permissions
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets


class UserView(viewsets.ModelViewSet):

    """ authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated] """

    queryset = User.objects.all()
    serializer_class = UserSerializer

