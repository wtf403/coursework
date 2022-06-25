from rest_framework.viewsets import ModelViewSet
from director.serializers import DirectorSerializer
from director.models import Director

class DirectorViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer 
