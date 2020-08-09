from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

#file:bookstore/views.py

from . import models

def add_view(request):
    if request.method == 'GET':
                #templates/bookstore/add_book.html
        return render(request,'bookstore/add_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        #数值,一定得给默认值
        price = float(request.POST.get('price','0'))
        m_price = float(request.POST.get('m_price','0'))
        try:
            models.Book.objects.create(
                title=title,
                price=price,
                market_price=m_price,
                pub=pub
            )
            # return HttpResponse('添加成功!')
            return HttpResponseRedirect('/bookstore/all')
        except:
            return HttpResponse('添加失败!')

def show_all(request):
    books = models.Book.objects.all()
    #__gt是>,__lt是<
    # books = models.Book.objects.filter(price__gt=80)

    #查找价格在50~80之间的
    # books = models.Book.objects.filter(price__range=(50,80))

    #筛选不是清华大学的，exclude（）不符和条件的
    # books = models.Book.objects.exclude(pub__contains='清华大学')

    #查询不是清华大学出版社，或定价不是大于50的
    # books = models.Book.objects.exclude(pub="清华大学出版社", price__gt=50)

    # for abook in books:
    #     print("书名:"+abook.title)
    # return HttpResponse("查询成功")
    return render(request,'bookstore/list.html',locals())


def mod_view(request,id):
    try:
        abook = models.Book.objects.get(id=id)
    except:
        return HttpResponse("没有id为"+ id + "的数据记录")
    if request.method == 'GET':
        return render(request,'bookstore/mod.html',locals())

    elif request.method == 'POST':
        # 获取数值时要转浮点数，也要给默认值
        m_price = float(request.POST.get('m_price','0'))
        abook.market_price = m_price #修改字段值
        abook.save()
        # 重新定向
        return HttpResponseRedirect('/bookstore/all')

#添加删除功能
def del_view(request,id):
    try:
        abook = models.Book.objects.get(id=id)

    except Exception as err:
        return HttpResponse("删除失败")

    abook.delete()
    #重定向回来
    return HttpResponseRedirect('/bookstore/all')
