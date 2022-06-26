from tkinter.tix import Tree
from rest_framework import serializers
from authentication.models import User
from director.models import Director
from actor.models import Actor
from video.models import Video


class DirectorSerializerForUser(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
        
class ActorSerializerForUser(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
    
class VideoSerializerForUser(serializers.ModelSerializer):
    actors = ActorSerializerForUser(source='actor', many=True)
    directors = DirectorSerializerForUser(source='director', many=True)
    class Meta:
        model = Video
        exclude = ['director', 'actor', 'genre', 'studio']

class UserSerializer(serializers.ModelSerializer):
    videos = VideoSerializerForUser(source='video', many=True)
    directors = DirectorSerializerForUser(source='director', many=True)
    actors = ActorSerializerForUser(source='actor', many=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'photo', 'password', 'is_active', 'actors', 'directors', 'videos']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_active = True

        if password is not None:
            instance.set_password(password)
        instance.save()
            
        return instance
