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
        VIDEO_COUNT_PER_PAGE = 3
        page = int(req.GET.get('page', 1))
        video = Video.objects.all()
        start_page = page - 1
        total_page = video.count()
        videos = video[start_page * VIDEO_COUNT_PER_PAGE : (start_page + 1) * VIDEO_COUNT_PER_PAGE]
        pager = {}
        pager['current'] = page
        pager['per_page'] = VIDEO_COUNT_PER_PAGE
        pager['total_page'] = total_page + VIDEO_COUNT_PER_PAGE
        serializer = VideoSerializer(videos, many=True)
        return render(req, 'admin_templates/video/list.html', {"videos" : serializer.data, 'page': page,'pager': pager})



