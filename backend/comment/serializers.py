from csv import field_size_limit
from rest_framework import serializers
from comment.models import Comment
from authentication.models import User
from video.models import Video


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class UserSerializerCommentList(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email']

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 

class VideoSerializerCommentList(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title']
    
class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializerCommentList(read_only=True)
    video = VideoSerializerCommentList(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
