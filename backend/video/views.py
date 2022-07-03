from rest_framework.viewsets import ModelViewSet
from video.serializers import VideoSerializer
from video.models import Video
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from comment.models import Comment
from comment.serializers import CommentSerializer

class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer 
