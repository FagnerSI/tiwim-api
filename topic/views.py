from rest_framework import viewsets
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Topic
from .serializers import TopicSerializer
from replay.serializers import ReplaySerializerAll, ReplaySerializer


class TopicView(viewsets.ModelViewSet):

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    @action(detail=True, methods=['get'])
    def replays(self, request, pk):
        topic = Topic.objects.get(id=pk)
        queryset = topic.replays.all().order_by('created_at')

        serializer = ReplaySerializerAll(
            queryset.reverse(), many=True, context={"request": request}
        )

        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def last_replay_of_user(self, request, pk):
        account = self.request.user
        topic = Topic.objects.get(id=pk)

        queryset = topic.replays.filter(
            author=account).last()

        serializer = ReplaySerializer(queryset)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def filter_replays(self, request, pk):
        kind_speech = request.query_params.get('kind_speech', None)
        roles_in = request.query_params.get('roles_in', None)
        roles_for = request.query_params.get('roles_for', None)

        topic = Topic.objects.get(id=pk)
        queryset = topic.replays.all()

        if kind_speech:
            queryset = queryset.filter(kind_speech=kind_speech)

        if roles_in:
            queryset = queryset.filter(roles_in=roles_in)

        if roles_for:
            queryset = queryset.filter(roles_for=roles_for)

        serializer = ReplaySerializerAll(
            queryset.reverse(), many=True, context={"request": request}
        )
        return Response(serializer.data)
