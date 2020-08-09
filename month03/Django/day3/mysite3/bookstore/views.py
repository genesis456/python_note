from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#file:bookstore/views.py

from . import models

def add_view(request):
    try:
        #插入方法1
        # #每执行一次，都会插入一次
        # abook = models.Book.objects.create(
        #     title = "C++",price=68)

        #方法2
        # abook = models.Book(price=98)
        # abook.title = '西游'
        # abook.save()   #真正执行SQL语句的
        return HttpResponse("添加图书成功!")
    except Exception as err:
        return HttpResponse('添加图书失败!')