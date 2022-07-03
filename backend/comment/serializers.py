from csv import field_size_limit
from rest_framework import serializers
from comment.models import Comment
from authentication.serializers import UserSerializer
from authentication.models import User
from video.serializers import VideoSerializer

class UserSerializerForComment(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class CommentSerializer(serializers.ModelSerializer):
    name = UserSerializerForComment(source='user')
    class Meta:
        model = Comment
        fields = '__all__'

