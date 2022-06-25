from rest_framework import serializers
from director.models import Director
from actor.models import Actor
from video.models import Video
from genre.models import Genre
from studio.models import Studio

class DirectorSerializerForVideo(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
        
class ActorSerializerForVideo(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
        
class StudioSerializerForVideo(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'
        
class GenreSerializerForVideo(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    directors = DirectorSerializerForVideo(source='director', many=True)
    actors = ActorSerializerForVideo(source='actor', many=True)
    studios = StudioSerializerForVideo(source='studio', many=True)
    genres = GenreSerializerForVideo(source='genre', many=True)
    class Meta:
        model = Video
        # fields = '__all__' 
        exclude = ['director', 'actor', 'studio', 'genre']
