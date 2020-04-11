from rest_framework import authentication, permissions
from project.models import Project
from .serializers import ProjectSerializer
from rest_framework import viewsets


class ProjectView(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
