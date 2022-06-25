from rest_framework.viewsets import ModelViewSet
from genre.serializers import GenreSerializer
from genre.models import Genre

class ActorViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 
