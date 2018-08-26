from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from video.models import Video
from video.serializers import VideoSerializer
import os
@api_view(['GET', 'POST'])
#TODO 로컬디렉토리에서 비디오 리스트 불러오기
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

@api_view(['GET', 'POST'])
#TODO 로컬디렉토리에서 비디오 리스트 불러오기
def VideoView_v2(req):
    if req.method == 'GET':
        VIDEO_COUNT_PER_PAGE = 1
        page = int(req.GET.get('page', 1))
        path = '/Users/contail/Projects/moca_web/moca-web/video_files'
        video = search(path)
        start_page = page - 1
        total_page = len(video)
        videos = video[start_page * VIDEO_COUNT_PER_PAGE : (start_page + 1) * VIDEO_COUNT_PER_PAGE]
        pager = {}
        pager['current'] = page
        pager['per_page'] = VIDEO_COUNT_PER_PAGE
        pager['total_page'] = total_page + VIDEO_COUNT_PER_PAGE
        return render(req, 'admin_templates/video/list.html', {"videos" : videos, 'page': page,'pager': pager})
def search(dirname):
    video_list = []
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1]
        title =filename
        if ext == '.mp4':
            video_list.append({
                'title' : title,
            })
    return video_list