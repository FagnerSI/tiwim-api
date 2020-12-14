
from rest_framework.decorators import action
from rest_framework import viewsets, status, authentication, permissions
from rest_framework.response import Response
from .models import Replay
from .serializers import ReplaySerializer


class ReplayView(viewsets.ModelViewSet):

    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer

    def create(self, request, *args, **kwargs):
        author = self.request.user
        dataSerializer = {'author': author.id, **request.data}

        serializer = self.get_serializer(data=dataSerializer)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'])
    def last_replay_of_user(self, request):
        account = self.request.user
        queryset = Replay.objects.filter(
            author=account).order_by('-created_at')[:1]
        serializer = ReplaySerializer(queryset, many=True)
        return Response(serializer.data)
