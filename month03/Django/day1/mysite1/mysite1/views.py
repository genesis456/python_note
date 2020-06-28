
from django.http import HttpResponse

#处理index的视图函数
def index_view(request):
    html = "<h1>这是首页</h1>"
    return HttpResponse(html)


def login_view(request):
    html = "<h3>这是登录页面</h3>"
    return HttpResponse(html)


def page1_view(request):
    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(html)

def page2_view(request):
    html = "<h1>这是第二个页面</h1>"
    return HttpResponse(html)

def page3_view(request):
    html = "<h1>这是第三个页面</h1>"
    return HttpResponse(html)


def pagen_view(request,n):
    html = '<h1>这是第%s个页面</h1>' % n
    return HttpResponse(html)


def math_view(request,x,oop,y):
    result = None
    if oop == 'add':
        result = int(x) + int(y)
    elif oop == 'sub':
        result = int(x) - int(y)
    elif oop == 'mul':
        result = int(x) * int(y)
    if result is None:
        return HttpResponseRedirect("https://www.baidu.com")

    return HttpResponse('结果为:'+str(result))


def person_view(request,name,age):
    '''*args接收整体的位置传参
       **kwargs接收整体的关键字传参'''
    # return HttpResponse(str(kwargs))
    return HttpResponse("<h1>name:%s age:%s</h1>" %(name,age))


def brithday_view(request,yy,mm,dd):
    html = "<h1>生日是:%s年%s月%s日</h1>" %(yy,mm,dd)
    return HttpResponse(html)


def test(request):
    # d = str(dict(request.GET))
    # return HttpResponse(d + str(request.GET.getlist('a')))
    return HttpResponse(request.GET.get('m','没有这个值'))

