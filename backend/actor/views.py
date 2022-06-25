from rest_framework.viewsets import ModelViewSet
from actor.serializers import ActorSerializer
from actor.models import Actor

class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer 
