from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
import uuid

from . import views

urlpatterns = [
   # url(r'^projectlist', views.projectdetails, name='projectdetails'),
    url(r'^$', views.index, name='index'),
    url(r'^submitproject$', views.submitproject, name='submitproject'),
    url(r'^submitprojectresource$', views.submitprojectresource, name='submitprojectresource'),
    url(r'^projectform', views.projectform.as_view(), name='projectform'),
    url(r'^projectdetails/(?P<project_id>[^/]+)/$',views.projectdetails)
]

