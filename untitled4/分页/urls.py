# coding = utf-8

from django.conf.urls import url
from . import views

urlpatterns = [

    # url(r'^$', views.index_view),
    url('index/', views.index2_view)
]
