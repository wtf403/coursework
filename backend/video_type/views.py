from rest_framework.viewsets import ModelViewSet
from video_type.serializers import VideoTypeSerializer
from video_type.models import VideoType

class VideoTypeViewSet(ModelViewSet):
    queryset = VideoType.objects.all()
    serializer_class = VideoTypeSerializer 
