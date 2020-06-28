# file:mysite3/views.py
from django.http import HttpResponse
from django.shortcuts import render

def page1_view(request):

    return render(request, 'page1.html')

def page2_view(request):

    return render(request, 'page2.html')

def pagen_view(request, n):

    return HttpResponse('我是第%s页'%(n))

def shebao(request):

    if request.method == 'GET':
        return render(request, 'shebao.html')
    elif request.method == 'POST':
        #处理数据阶段
        base = request.POST.get('base', '0')
        base = float(base)
        is_city = request.POST.get('is_city', '1')
        #计算社保
        #养老保险
        yl_gr = base * 0.08
        yl_dw = base * 0.19
        #失业
        sy_dw = base * 0.008
        if is_city:
            #城镇户口
            sy_gr = base * 0.002
        else:
            sy_gr = 0
        # 工伤保险
        gs_gr = 0
        gs_dw = base * 0.005
        #生育保险
        ss_gr = 0
        ss_dw = base * 0.008
        #医疗保险
        yy_gr = (base*0.002)+3
        yy_dw = base * 0.10
        #公积金
        gj_gr = base * 0.12
        gj_dw = base * 0.12

        return render(request, 'shebao.html', locals())





















    return HttpResponse('---Please use GET or POST !---')












