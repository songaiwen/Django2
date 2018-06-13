from django.conf.urls import url
from . import views

urlpatterns = [
    #url第一个参数是正则：第二参数是是视图函数名
    #第三个参数是url的名字
    url(r'^index/$',views.index, name='lalalala')
]