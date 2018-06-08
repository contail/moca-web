from django.shortcuts import render, redirect
from rest_framework.decorators import api_view




@api_view(['GET'])
def main_index(req):
    return render(req, 'admin_ss/index.html', {})

@api_view(['GET'])
def get_video_list(req):

    return render('')

