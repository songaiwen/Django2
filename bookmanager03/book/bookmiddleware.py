from django.http import HttpResponse

def mymiddleware(get_response):
    #这里是初始化或者中间件第一次加载的地方
    print('init')
    def middleware(request):
        #这里是请求前
        print('before request')
        response = get_response(request)
        #这里是响应后
        print('after response')
        return response
    return middleware