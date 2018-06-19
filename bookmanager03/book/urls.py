from django.conf.urls import url
from . import views
from . views import login_required
urlpatterns = [
    #url第一个参数是正则：第二参数是是视图函数名
    #第三个参数是url的名字
    url(r'^index/$',views.index, name='lalalala'),
    #根据正则匹配数字
    # url(r'^index/$',views.index),
    # url(r'^index/(\d+)/(\d+)/$',views.index),
    #使用关键字传参
    # url(r'^index/(?P<category_id>\d+)/(?P<goods_id>\d+)/$',views.index),
    # url(r'^register/$',views.register)

    url(r'^register/$',views.RegisterView.as_view()),
    # url(r'^center/$',login_required(views.CenterView.as_view()))
    url(r'^center/$',views.CenterView.as_view()),
    url(r'session/$',views.session)
]