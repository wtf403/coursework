from django.urls import path
from video.views import video_list

urlpatterns = [
    path('videos', video_list)
]
