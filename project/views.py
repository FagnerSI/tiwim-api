from rest_framework import viewsets
from rest_framework import authentication, permissions
from .models import Project
from .serializers import ProjectSerializer


class ProjectView(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    """ def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy', 'list']:
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [AllowAny, ]
        return super(self.__class__, self).get_permissions() """
