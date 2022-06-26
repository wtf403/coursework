from itertools import permutations
from urllib import response
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed
from rest_framework.viewsets import ModelViewSet
from authentication.models import User
from authentication.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from video.models import Video
# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False, url_path='register')
    def regiser(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'massage': 'success'})

    @action(methods=['POST'], detail=False, url_path='login')
    def login(self, request):
        if 'email' not in request.data:
            raise ValidationError({'error': 'email must not be empty'})
        if 'password' not in request.data:
            raise ValidationError({'error': 'password must not be empty'})
        try:
            user = User.objects.get(email=request.data['email'])
        except User.DoesNotExist:
            raise NotFound({'error': 'user with this email was not found'})
        
        if not user.check_password(request.data['password']):
            raise AuthenticationFailed({'error': 'incorrect password'})

        refrash = RefreshToken.for_user(user)
        response = Response()
        response.data = {'access': str(refrash.access_token)}
        return response
    
    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='me')
    def get_user(self, request):
        user = request.user
        data = self.serializer_class(user).data
        return Response(data)

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated], url_path='toggle-favorite-video')
    def toggle_favorite(self, request, pk=None):
        video_id = request.POST.get('video_id')
        try:
            print('try')
            User.objects.get(id=pk).video.get(id=video_id)
            videos = User.objects.get(id=pk).video.exclude(id=video_id)
            User.objects.get(id=pk).video.set(videos, clear=True)
            return Response({'message': 'removed'})
        except:
            print('except')
            video = Video.objects.get(id=video_id)
            print(type(video))
            User.objects.get(id=pk).video.add(video)
            return Response({'message': 'added'})






