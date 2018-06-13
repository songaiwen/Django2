from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import BookInfo

def aaaa(request):
    ######增加数据#########
    from book.models import BookInfo

    book = BookInfo(name='水浒传')

    book

    book = BookInfo.objects.create(name='三国演义')

    #############修改数据#########
    #第一种方式
    #先获取到数据，然后再修改数据的字段
    book.readcount = 100
    #注意调用save方法
    book.save()
    #第二种修改数据的方式

    BookInfo.objects.filter(id=6).update(commentcount=200)


    #################删除数据###############

    #第一种方法
    book.delete()

    #第二种方法
    BookInfo.objects.filter(id=5).delete()




    ########查询##########
    #get查询单一结果，如果不存在抛出模型类，异常
    book = BookInfo.objects.get(id=1)
    book = BookInfo.objects.get(pk=1) #primary
    #DoesNotExist不存在的异常
    book = BookInfo.objects.get(id=10)
    #all查询所有
    book = BookInfo.objects.all()
    #count查询数量
    count = BookInfo.objects.all().count()

    #where


    #filter过滤出多个结果，一个或者0个

    # exclude排除符合条件的剩下的结果  相当于not

    #get单一的结果

    #以filter为例子说明一下语法形式
    #filter（字段名__运算符=值）

    # 查询编号为1的图书
    book = BookInfo.objects.get(id__exact=1)
    book = BookInfo.objects.get(id=1)
    book = BookInfo.objects.get(pk=1)
    #返回的结果是列表，如果需要拿到数据需要遍历
    book = BookInfo.objects.filter(pk=1)
    # 查询书名包含'湖'的图书
    books = BookInfo.objects.filter(name__contains='湖')
    # 查询书名以'部'结尾的图书
    books = BookInfo.objects.filter(name__endswith='湖')
    # 查询书名为空的图书
    books = BookInfo.objects.filter(name__isnull=True)
    books = BookInfo.objects.filter(pub_date__isnull=True)
    # 查询编号为1或3或5的图书
    books = BookInfo.objects.filter(id_in=(1,3))
    # 查询编号大于3的图书
    # gt 大于
    #gte大于等于
    #lt小于
    #lte小于等于
    books = BookInfo.objects.filter(id_gt=3)
    #查询编号不等于3的书籍
    books = BookInfo.objects.exclude(id=3)

    # 查询1980年发表的图书
    books = BookInfo.objects.filter(pub_date__year='2018')
    # 查询1990年1月1日后发表的图书
    books = BookInfo.objects.filter(pub_date__gt='1990-1-1')

    #查询评论数大于阅读数量的书籍

    from django.db.models import F
    #F（‘字段’）
    #只需要把常量值换成F
    books = BookInfo.objects.filter(commentcount__gt=F('readcount'))
    #查询评论数大于阅读数量2倍的书籍
    books = BookInfo.objects.filter(commentcount__gt=F('readcount')*2)



    #多个逻辑关系
    #查询阅读数量大于30并且id>3的书籍
    #第一种写法
    books = BookInfo.objects.filter(readcount__gt=30,id__gt=3)

    #第二种写法
    books = BookInfo.objects.filter(readcount__gt=30).filter(id__gt=3)
    # Q对象就是相当于or
    #语法形式Q（字段__运算符=值）|  Q（字段__运算符=值）
    from django.db.models import Q

    book = BookInfo.objects.filter(Q(readcount__gt=30)|Q(id__gt=3))

    #查询id不等于3的
    #还可以使用～Q查询
    books = BookInfo.objects.filter(~Q(id=3))

    #聚合函数
    #aggregate 和 聚合函数Avg  Sum Man Min Count配合使用
    from django.db.models import Sum,Max,Min,Avg,Count

    book = BookInfo.objects.aggregate(Sum('readcount'))

    #order_by(字段)
    #默认升序
    book = BookInfo.objects.all().order_by('id')

    #降序
    book = BookInfo.objects.all().order_by('-id')

    #多个字段排序的原理是第一个字段的值相等，按着第二个字段排序
    books = BookInfo.objects.all().order_by('readcount', 'commentcount')


    #关联查询
    # 查询书籍为1的所有人物信息
    #先找到书籍为1的书，再通过书查到任务信息
    books = BookInfo.objects.get(id=1)
    people = books.peopleinfo_set.all()
    # 查询人物为1的书籍信息
    #先查询人物再查寻书记
    from book.models import PeopleInfo
    person = PeopleInfo.objects.get(id=1)
    person.book.name

    #关联查询的筛选
    # 查询图书，要求图书人物为    "郭靖"  一对多的查询
    #先查询出图书，再查出图书中名字为郭靖的人
    book = BookInfo.objects.filter(peopleinfo__name='郭靖')

    # 查询图书，要求图书中人物的描述包含    "八"
    book = BookInfo.objects.filter(peopleinfo__description__contains='八')

    #多对一

    # 查询书名为“天龙八部”的所有人物
    people = PeopleInfo.objects.filter(book__name='天龙八部')

    # 查询图书阅读量大于30的所有人物
    people = PeopleInfo.objects.filter(book__readcount__gt=30)

    # filter order_by , exclude  all
    #他们都是chacun结果，可以理解为对象列表
    books = BookInfo.objects.all()

    #缓存就是将数据放置到一个地方（本地）
    # [book.id for book in BookInfo.objects.all()]

    # limit offset page
    #限制查询结果集
    books = BookInfo.objects.all()[0:2]


    return HttpResponse('ok')


def booklist(request):
    book = BookInfo.objects.create(
        name='红楼梦',
        pub_date='2018-1-1',
        readcount=100,
        commentcount = 200
    )

    books = BookInfo.objects.all()
    for book in books:
        print(book.name)

    context = {
        'books':books
    }



    return render(request,'booklist.html', context)

def index(request):

    name = '宋雨希'
    context = {

        'name':name
    }

    return render(request, 'index.html', context)
    # return HttpResponse('ok')
