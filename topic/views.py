from rest_framework import viewsets
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Topic
from .serializers import TopicSerializer
from replay.serializers import ReplaySerializerAll


class TopicView(viewsets.ModelViewSet):

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    @action(detail=True, methods=['get'])
    def replays(self, request, pk):
        topic = Topic.objects.get(id=pk)
        queryset = topic.replays.all().order_by('created_at')

        serializer = ReplaySerializerAll(queryset.reverse(), many=True)
        return Response(serializer.data)
