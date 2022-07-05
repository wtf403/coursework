from rest_framework.routers import DefaultRouter
from actor.views import ActorViewSet
from video.views import VideoViewSet
from director.views import DirectorViewSet
from studio.views import StudioViewSet
from video_type.views import VideoTypeViewSet
from comment.views import CommentViewSet
from authentication.views import UserViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register(r'videos', VideoViewSet)
comment_router = routers.NestedSimpleRouter(router, r'videos', lookup='video')
comment_router.register(r'comments', CommentViewSet, basename='comment')
router.register('actors', ActorViewSet)
router.register('comments', CommentViewSet)
router.register('directors', DirectorViewSet)
router.register('studios', StudioViewSet)
router.register('video_types', VideoTypeViewSet)
router.register('user', UserViewSet)

