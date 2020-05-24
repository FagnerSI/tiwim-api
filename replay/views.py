from rest_framework import viewsets
from rest_framework import authentication, permissions
from .models import Replay
from .serializers import ReplaySerializer


class ReplayView(viewsets.ModelViewSet):

    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer
