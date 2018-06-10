#coding:utf8
from django.conf.urls import url
from . import views

urlpatterns = [
    #index/
    #url
    url(r'index/', views.index)

]