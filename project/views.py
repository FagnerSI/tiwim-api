from rest_framework import viewsets

from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer


class ProjectView(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    """ def get_queryset(self):
        account = self.request.user
        return reversed(Project.objects.filter(members=account)) """

    def list(self, request, *args, **kwargs):
        account = self.request.user
        queryset = reversed(Project.objects.filter(members=account))

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    """ def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy', 'list']:
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [AllowAny, ]
        return super(self.__class__, self).get_permissions() """
