"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import re

import os
from django.conf.urls import url
from django.urls import path
from django.views.static import serve
from rest_framework import routers

from web import settings
router = routers.SimpleRouter()

def staticfiles_short_urlpatterns(prefix, view=serve, **kwargs):
    # No-op if not in debug mode or an non-local prefix
    return url(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), view, kwargs=kwargs)


urlpatterns = [
    path('admin/', include('frontend.urls')),

]
urlpatterns.append(staticfiles_short_urlpatterns('images', document_root=os.path.join(settings.STATIC_ROOT, 'images')))
urlpatterns.append(staticfiles_short_urlpatterns('css', document_root=os.path.join(settings.STATIC_ROOT, 'css')))
urlpatterns.append(staticfiles_short_urlpatterns('fonts', document_root=os.path.join(settings.STATIC_ROOT, 'fonts')))
urlpatterns.append(staticfiles_short_urlpatterns('font-awesome', document_root=os.path.join(settings.STATIC_ROOT, 'font-awesome')))
urlpatterns.append(staticfiles_short_urlpatterns('chrome-app', document_root=os.path.join(settings.STATIC_ROOT, 'chrome-app')))
urlpatterns.append(staticfiles_short_urlpatterns('less', document_root=os.path.join(settings.STATIC_ROOT, 'less')))
urlpatterns.append(staticfiles_short_urlpatterns('bs3', document_root=os.path.join(settings.STATIC_ROOT, 'bs3')))
urlpatterns.append(staticfiles_short_urlpatterns('js', document_root=os.path.join(settings.STATIC_ROOT, 'js')))
urlpatterns.append(staticfiles_short_urlpatterns('bucket-ico-fonts', document_root=os.path.join(settings.STATIC_ROOT, 'bucket-ico-fonts')))
urlpatterns.append(staticfiles_short_urlpatterns('static', document_root=settings.STATIC_ROOT))
print (settings.VIDEO_ROOT, "====================")
urlpatterns.append(staticfiles_short_urlpatterns('video_files', document_root=settings.VIDEO_ROOT))