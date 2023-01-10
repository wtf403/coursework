from tkinter.tix import Tree
from rest_framework import serializers
from authentication.models import User
from director.models import Director
from actor.models import Actor
from video.models import Video
from django.contrib.auth.hashers import make_password
from drf_writable_nested import WritableNestedModelSerializer


class DirectorSerializerForUser(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']

        
class ActorSerializerForUser(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields =  ['id', 'name']
    
class VideoSerializerForUser(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title']

class UserSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    videos = VideoSerializerForUser(source='video', required=False)
    directors = DirectorSerializerForUser(source='director', required=False)
    actors = ActorSerializerForUser(source='actor', required=False)

    class Meta:
        model = User
        exclude = ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(
            **validated_data
        )
        if password is not None:
            instance.set_password(password)
        instance.is_active = True
        instance.save()
            
        return instance

    def update(self, instance, validated_data):
        print('aldflajdslfj')
        return super().update(instance, validated_data)
