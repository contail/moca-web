from django.urls import path
from rest_framework import routers

from frontend.views import main_index
from video.views import VideoView_v2

urlpatterns = [
    path('', main_index, name='main_index'),
    path('video', VideoView_v2),
]
