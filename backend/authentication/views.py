from itertools import permutations
from urllib import response
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed
from rest_framework.viewsets import ModelViewSet
from authentication.models import User
from authentication.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from video.models import Video
from director.models import Director
from actor.models import Actor

# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    @action(methods=['POST'], permission_classes=[AllowAny], detail=False, url_path='register')
    def regiser(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'massage': 'success'})

    @action(methods=['POST'], permission_classes=[AllowAny], detail=False, url_path='login')
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

        refresh = RefreshToken.for_user(user)

        response = Response()
        response.set_cookie('refresh', str(refresh))
        response.set_cookie('access', str(refresh.access_token))
        response.data = {'access': str(refresh.access_token), 'refresh': str(refresh)}
        return response

    
    
    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='me')
    def get_user(self, request):
        user = request.user
        data = self.serializer_class(user).data
        return Response(data)


    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated], url_path='logout')
    def logout(self, request):
        response = Response()
        user = request.user
        refresh = RefreshToken().for_user(user)
        refresh.blacklist()
        response.data = {'logout': 'successfully'}
        return response
    
    # @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated], url_path='refresh')
    # def refresh(self, request):
    #     ref = request.COOKIES.get('refresh') 
    #     refresh = RefreshToken.for_user(request.user)
    #     response = Response()
    #     refresh.blacklist()
    #     response.delete_cookie('refresh')
    #     response.set_cookie('refresh', str(refresh))

    #     response.data = {'access': str(refresh.access_token), 'refresh': str(refresh)}
    #     return response

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated], url_path='toggle-favourite-video')
    def toggle_favourite_video(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            raise NotFound('user not found')
        try:
            video_id = request.POST.get('video_id')
            video = Video.objects.get(id=video_id)
        except Video.DoesNotExist:
            raise NotFound('video not found')
        try:
            user.video.get(id=video_id)
            videos = user.video.exclude(id=video_id)
            user.video.set(videos, clear=True)
            return Response({'message': 'removed'})
        except:
            user.video.add(video)
            return Response({'message': 'added'})

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated], url_path='toggle-favourite-director')
    def toggle_favourite_director(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            raise NotFound('user not found')
        try:
            director_id = request.POST.get('director_id')
            director = Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise NotFound('director not found')
        try:
            user.director.get(id=director_id)
            directors = user.director.exclude(id=director_id)
            user.director.set(directors, clear=True)
            return Response({'message': 'removed'})
        except:
            user.director.add(director)
            return Response({'message': 'added'})
    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated], url_path='toggle-favourite-actor')
    def toggle_favourite_actor(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            raise NotFound('user not found')
        try:
            actor_id = request.POST.get('actor_id')
            actor = Actor.objects.get(id=actor_id)
        except Actor.DoesNotExist:
            raise NotFound('actor not found')
        try:
            user.actor.get(id=actor_id)
            actors = user.actor.exclude(id=actor_id)
            user.actor.set(actors, clear=True)
            return Response({'message': 'removed'})
        except:
            user.actor.add(actor)
            return Response({'message': 'added'})
