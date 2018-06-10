"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

#这个是固定写法，列表存储路径信息的
urlpatterns = [
    #http://127.0.0.1:8000/index/
    #这个url只会拿index/来进行匹配
    #url会依次和url里面的正则进行匹配
    #如果和admin/匹配则引导到对应的应用
    #第一个参数：正则匹配，r防转移 ^严格的以什么开始 $ 严格的以什么结束
    url(r'^admin/', admin.site.urls),
    #不匹配：如果没有符合条件的就是404

    #添加一条匹配正则，不是admin/都转到book应用里面去
    url(r'^', include('book.urls'))

]
