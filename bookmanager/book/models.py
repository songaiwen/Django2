from django.db import models

"""
create your models here
定义模型类
模型迁移
操作数据库
"""
#1.定义模型需要集成model.Model
class BookInfo(models.Model):
    #自动创建主键
    name = models.CharField(max_length=20)

    def __str__(self):
        pass

class PeopleInfo(models.Model):

    name = models.CharField(max_length=20)
    gender = models.BooleanField()

    #外键
    book = models.ForeignKey(BookInfo)
