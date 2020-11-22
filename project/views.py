from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Project
from .serializers import ProjectSerializer, ProjectListSerializer
from topic.serializers import TopicSerializer


class ProjectView(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    """ def get_queryset(self):
        account = self.request.user
        return reversed(Project.objects.filter(members=account)) """

    """ def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy', 'list']:
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [AllowAny, ]
        return super(self.__class__, self).get_permissions() """

    def list(self, request, *args, **kwargs):
        account = self.request.user
        queryset = Project.objects.filter(
            members=account).order_by('-created_at')

        serializer = ProjectListSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def topics(self, request, pk):
        account = self.request.user
        project = Project.objects.get(id=pk)
        queryset = project.topics.filter(
            members=account).order_by('-created_at')

        serializer = TopicSerializer(queryset, many=True)
        return Response(serializer.data)
