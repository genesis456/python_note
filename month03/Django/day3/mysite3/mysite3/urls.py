"""mysite3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from oth er_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^page1$', views.page1_view),
    #url反向解析
    url(r'^pageabc2$', views.page2_view, name='page2'),
    url(r'page(\d+)', views.pagen_view, name='pagen'),
    #社保计算器
    url(r'^shebao$', views.shebao),
    #127.0.0.1:8000/sport/add
    #127.0.0.1:8000/sport/mul
    url(r'^index/',include('index.urls')),
    url(r'^sport/', include('sport.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^news/', include('news.urls')),

    url(r'^bookstore/',include('bookstore.urls')),


]
