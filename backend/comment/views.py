from rest_framework.viewsets import ModelViewSet
from comment.serializers import CommentSerializer
from comment.models import Comment

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
