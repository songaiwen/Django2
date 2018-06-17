from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
# Create your views here.


#装饰器已经定义完成
def login_required(func):
    def wrapper(request, *args, **kwargs):
        if True:
            return func(request,*args,**kwargs)
        else:
            return HttpResponse('您暂未登陆')

    return wrapper

#python是多继承的
#因为我们在进行url正则匹配的时候，试图类都需要调用as_view方法
#所以采用多继承的方法来重写as_view方法
#多继承是按着从左到有右的顺序继承的
class LoginRequireMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super().as_view()
        view = login_required(view)

        return view




#定义个人中心页面，有get和post请求
#第一个参数是需要填写的装饰器名
#第二个参数，是需要作用的函数名
#method_decorator可以选择性的作用于某个函数
#dispatch负责分发
# @method_decorator(login_required, name='dispatch')
class CenterView(LoginRequireMixin,View):
    """

    get获取个人中心页面
    post是修改个人中心信息
    个人中心必须是登陆用户才能进入
    所以需要判断用户是否登陆，如果没有登陆需要给出提示信息
    """

    def get(self,request):
        # if True:
            return HttpResponse('get center')
        # else:
        #     return HttpResponse('您还没有登陆')

    def post(self,request):
        # if True:

            return HttpResponse('post center')
        # else:
        #     return HttpResponse('您暂未登陆')



# 类视图和装饰器

class RegisterView(View):
    """类视图
    可以在类里面定义get  post  delete  等
    """

    def get(self,request):

        return  HttpResponse('get')

    def post(self,request):
        return HttpResponse('post')

    def put(self,request):
        return HttpResponse('put')




def register(request):
    if request.method == 'GET':
        return HttpResponse('get页面')
    else:
        return HttpResponse('post页面')

#一个页面有两个逻辑，可以何在一起写
# def register2(request):
#     return HttpResponse('post页面')


#如果参数多了
#category_id分类id
#goods_id商品id
#顺序打乱了，使用关键字参数传参
def index(request,goods_id,category_id):
    ####################状态保持  cookie##############
    #未登陆的购物车数据应该放在cookie里面
    res = HttpResponse('cookie')
    # 将数据写入到cookie
    res.set_cookie('cart','1')

    #读取cookie
    cookie = request.COOKIES
    print(cookie)

    #cookie删除

    res.delete_cookie('cart')
    return res


    ##session

    # request.session['name'] = 'itcast'
    # name = request.session['name']
    # del request.session['name']
    #
    #










    #如果设置了命名空间参数，需要采用命名空间
    # 提取URL的特定部分，如 / weather / beijing / 2018，可以在服务器端的路由中用正则表达式截取；
    print(category_id, goods_id)
    # 查询字符串（querystring)，形如key1 = value1 & key2 = value2；
    getdata = request.GET
    print(getdata)

    #一键一值
    # a = getdata.get('a')
    # print(a)
    #一键多值
    # a = getdata.getlist('a')
    # print(a)


    # 请求体（body）中发送的数据，比如表单数据、json、xml；
    # postdata = request.POST
    # print(postdata)

    # #一键一值
    # name = postdata.get('name')
    # print(name)
    # #一键多值
    # name = postdata.getlist('name')
    # print(name)


    # body = request.body
    # print(body)
    #
    # body_str = body.decode()
    # print(body_str)
    # import json
    # body_json = json.loads(body_str)
    # print(body_json)
    # key = body_json.get('key')
    # print(key)

    # 在http报文的头（header）中。
    # print(request.META)
    # print(request.META['CONTENT_TYPE'])
    # print(request.META['HTTP_NAME'])
    # print(request.method)



    ##################redirect#############
    # return redirect("http://www.itheima.com")



    # print(request.user)
    #########################JsonResponse####################
    from django.http import JsonResponse
    res = JsonResponse({'key':'value'})
    return res



    #############################HttpResponse###################3
    # content就是返回的内容

    res = HttpResponse('数据')

    #content-type是数据类型MIME类名
    #MIME   类型语法   大类/小类

    #status
    #200 300 400 500 404  403
    res.status_code = 400
    return res



    # url的名字，可以通过reverse获取它的路径
    # 获取url名字
    path = reverse('book:lalalala')
    print(path)
    return render(request, 'index.html')