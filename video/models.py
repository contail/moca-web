from django.db import models

# Create your models here.
from member.models import Member


class Video(models.Model):
    user = models.ForeignKey(Member, related_name='member', null=True, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100, null =True)
    url = models.CharField(max_length=100, null=True)
    created_time = models.DateTimeField(null= True)

    def __str__(self):
        return "{0} {1}".format(self.user.name, self.title)