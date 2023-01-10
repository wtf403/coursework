from types import NoneType
from rest_framework import serializers
from director.models import Director
from actor.models import Actor
from video.models import Video
from genre.models import Genre
from studio.models import Studio
from video_type.models import VideoType

class DirectorSerializerForVideo(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']
        
class ActorSerializerForVideo(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name']
        
class StudioSerializerForVideo(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ['id', 'name']
        
class GenreSerializerForVideo(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'title']

class TypeSerializerForVideo(serializers.ModelSerializer):
    class Meta:
        model = VideoType
        fields = ['video_type', 'id']


class VideoSerializer(serializers.ModelSerializer):
    directors = DirectorSerializerForVideo(source='director', many=True)
    actors = ActorSerializerForVideo(source='actor', many=True)
    studios = StudioSerializerForVideo(source='studio', many=True)
    genres = GenreSerializerForVideo(source='genre', many=True)
    type =  TypeSerializerForVideo(source="v_type")
    class Meta:
        model = Video
        # fields = '__all__' 
        exclude = ['director', 'actor', 'studio', 'genre', 'v_type']
