#file: music/urls.py
"""此模块实现music 应用中的子路由配置"""

from django.conf.urls import url
from . import views

urlpatterns= [

    url(r'^music', views.music_view),

]