from rest_framework import serializers
from video.models import VideoType
class VideoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoType
        fields = '__all__' 
