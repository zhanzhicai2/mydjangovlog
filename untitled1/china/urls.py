#coding=utf-8

from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
   path('hello/', views.hello)
]