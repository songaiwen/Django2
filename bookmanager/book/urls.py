#coding:utf8
from django.conf.urls import url
from . import views

urlpatterns = [
    #index/
    #url
    url(r'index/', views.index),
    url(r'booklist/',views.booklist),
    url(r'center/', views.center),
]