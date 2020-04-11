from rest_framework import authentication, permissions
from role.models import Role
from .serializers import RoleSerializer
from rest_framework import viewsets


class RoleView(viewsets.ModelViewSet):

    queryset = Role.objects.all()
    serializer_class = RoleSerializer
