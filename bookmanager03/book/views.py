from django.shortcuts import render
from django.urls import reverse
# Create your views here.
def index(request):
    # 获取url名字
    #url的名字，可以通过reverse获取它的路径
    #如果设置了命名空间参数，需要采用命名空间
    path = reverse('book:lalalala')
    print(path)
    return render(request, 'index.html')