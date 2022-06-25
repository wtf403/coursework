from rest_framework.routers import DefaultRouter
from actor.views import ActorViewSet
from video.views import VideoViewSet
from director.views import DirectorViewSet
from studio.views import StudioViewSet
from video_type.views import VideoTypeViewSet
from comment.views import CommentViewSet
from authentication.views import UserViewSet


router = DefaultRouter()
router.register('videos', VideoViewSet)
router.register('actors', ActorViewSet)
router.register('directors', DirectorViewSet)
router.register('studios', StudioViewSet)
router.register('video_types', VideoTypeViewSet)
router.register('comments', CommentViewSet)
router.register('auth', UserViewSet)
