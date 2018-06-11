from django.shortcuts import render
from django.http import HttpResponse
from . models import BookInfo

def booklist(request):

    #通过模型来查询数据
    books = BookInfo.objects.all()

    #组织上下文
    context = {
        'books':books

    }
    return render(request,'book/booklist.html',context)
    # return HttpResponse('ok')



# Create your views here.
#第一个参数是HttpRequest对象
def index(request):

    name = "宋雨希"
    #视图函数 必须有响应HttpResponse 对象或者子类

    context = {
        'name':name
    }
    return render(request,'book/index.html',context)

def center(request):
    weather = "阴天"

    context = {
        'weather':weather

    }
    return render(request,'book/center.html', context)