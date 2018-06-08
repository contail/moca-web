from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from video.models import Video
from video.serializers import VideoSerializer

@api_view(['GET', 'POST'])
def VideoView(req):
    if req.method == 'GET':
        # video = get_object_or_404(Video)
        video = Video.objects.all()
        serializer = VideoSerializer(video, many=True)
        return render(req, 'admin_ss/video/list.html', {"videos" : serializer.data})



