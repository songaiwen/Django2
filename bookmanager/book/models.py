from django.db import models

"""
create your models here
定义模型类
模型迁移
操作数据库
"""
#1.定义模型需要集成model.Model
#准备书籍列表信息的模型类
class BookInfo(models.Model):
    #创建字段，字段类型，自动创建主键并自动增长
    name = models.CharField(max_length=20)

    def __str__(self):
        #将模型类以字符串的方式输出
        return self.name

#准备人物列表信息的模型类
class PeopleInfo(models.Model):

    name = models.CharField(max_length=20)
    gender = models.BooleanField()

    #外键约束，人物属于哪本书
    book = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.name
