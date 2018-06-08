from django.utils import decorators
from rest_framework import serializers

from video.models import *

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields ='__all__'


