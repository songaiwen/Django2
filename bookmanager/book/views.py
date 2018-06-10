from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#第一个参数是HttpRequest对象
def index(request):

    #视图函数 必须有响应HttpResponse 对象或者子类

    return HttpResponse('ok')