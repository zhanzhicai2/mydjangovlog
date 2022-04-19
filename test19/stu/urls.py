#coding=utf-8
from django.urls import path
from . import views

urlpatterns = (
    path('index/', views.index2view),
    path('', views.IndexView.as_view()),
)
