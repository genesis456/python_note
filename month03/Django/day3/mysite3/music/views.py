from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def music_view(request):

    return HttpResponse('我是music主页')