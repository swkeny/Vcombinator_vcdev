from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # url(r'^$', views.mainimages, name='mainimages'),
    url(r'^$', views.mainpage.as_view(), name='mainpage'),
]