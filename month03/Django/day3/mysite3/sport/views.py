from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def sport_view(request):

    return HttpResponse('我是sport的主页')