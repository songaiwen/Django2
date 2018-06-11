from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    name = '宋雨希'
    context = {

        'name':name
    }

    return render(request, 'index.html', context)
    # return HttpResponse('ok')
