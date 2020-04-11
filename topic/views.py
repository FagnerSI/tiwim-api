from rest_framework import viewsets
from rest_framework import authentication, permissions
from .models import Topic
from .serializers import TopicSerializer


class TopicView(viewsets.ModelViewSet):

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
