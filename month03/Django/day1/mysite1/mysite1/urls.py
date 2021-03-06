"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index_view),
    url(r'^login', views.login_view),

    # url(r'^page1$',views.page1_view),
    url(r'^page2$', views.page2_view),
    url(r'^page3$', views.page3_view),
    url(r'^page(\d+)', views.pagen_view),
    url(r'^(\d+)/(\w{3})/(\d+)', views.math_view),
    url(r'^person/(?P<name>\w+)/(?P<age>\d+)', views.person_view),
    url(r'^brithday/(?P<yy>\d{4})/(?P<mm>\d{1,2})/(?P<dd>\d{1,2})', views.brithday_view),
    url(r'^brithday/(?P<dd>\d{1,2})/(?P<mm>\d{1,2})/(?P<yy>\d{4})', views.brithday_view),

    url(r'^test', views.test),
]
