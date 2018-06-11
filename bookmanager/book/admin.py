from django.contrib import admin
# from models import *
#倒入模型
from book.models import BookInfo,PeopleInfo
# Register your models here.
# class BookInfoAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title','pub_date']
# class PeopleInfoAdmin(admin.ModelAdmin):
#     list_display = ['id','name','content','gender','book']
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
