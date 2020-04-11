from rest_framework import authentication, permissions
from replay.models import Replay
from .serializers import ReplaySerializer
from rest_framework import viewsets


class ReplayView(viewsets.ModelViewSet):

    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer
