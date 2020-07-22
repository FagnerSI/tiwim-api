from rest_framework import viewsets
from rest_framework import authentication, permissions
from .models import Role
from .serializers import RoleSerializer


class RoleView(viewsets.ModelViewSet):

    queryset = Role.objects.all()
    serializer_class = RoleSerializer
