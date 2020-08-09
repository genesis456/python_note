#file: bookstore/admin.py
from django.contrib import admin

# Register your models here.

#注册添加自定义的模型类到admin站点管理中
from . import models

#模型管理器类
class BookManager(admin.ModelAdmin):
    #将字段放入list_display列表中，显示在后台
    list_display = ['id','title','pub','price','market_price']

    #将字段变为超链接形式
    list_display_links = ['id','title']

    #修改列表页面右侧栏中的过滤器,显示某一类别的
    list_filter = ['pub']

    #页面上的搜索框,搜索某一字段
    search_fields = ['title','pub']

    #允许可以直接在列表页面上进行编辑更改
    list_editable = ['market_price']

class AuthorManager(admin.ModelAdmin):
    list_display=['id','name','age']

    list_display_links = ['age']
admin.site.register(models.Book,BookManager)

admin.site.register(models.Author,AuthorManager)

class WifeManager(admin.ModelAdmin):
    list_display=['id','name','author']
admin.site.register(models.Wife,WifeManager)