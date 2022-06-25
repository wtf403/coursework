from rest_framework.viewsets import ModelViewSet
from studio.serializers import StudioSerializer
from studio.models import Studio

class StudioViewSet(ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer 
