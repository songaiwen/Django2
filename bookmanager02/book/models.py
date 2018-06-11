from django.db import models

# Create your models here.

class BookInfo(models.Model):

    # 自动会我们创建主键, 主键的字段名为 id
    #书籍名
    name = models.CharField(max_length=20)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    #字段名不能是 python, mysql 的关键字
    # 字段名不能有 两个 __

    # 字段名 , 字段类型 ,字段 选项
    class Meta:
        #元选项
        #用于改变数据库的相关信息
        #修改表名字
        db_table = 'bookinfo'

# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name
