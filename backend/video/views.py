from rest_framework.viewsets import ModelViewSet
from video.serializers import VideoSerializer
from video.models import Video
from rest_framework.decorators import action
from authentication.models import User
from rest_framework.permissions import IsAuthenticated

class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer 
    