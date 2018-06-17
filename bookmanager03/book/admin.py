from django.contrib import admin
from .models import BookInfo,PeopleInfo
# Register your models here.
#定义图书管理类，需要继承自admin.ModesAdmin
class BookInfoAdmin(admin.ModelAdmin):
    #显示的字段
    list_display = ['id', 'name', 'readcount', 'commentcount', 'title']
    list_per_page = 2

    #动作action
    actions_on_top = True
    actions_on_bottom = True

    #搜索
    search_fields = ['name']

    #筛选
    list_filter = ['name']
    #自定义字段


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(PeopleInfo)