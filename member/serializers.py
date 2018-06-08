from django.utils import decorators
from rest_framework import serializers

from member.models import *

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields =('id', 'name', 'email', )


