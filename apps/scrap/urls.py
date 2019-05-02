# -*- coding: utf-8 -*-
# @DATE    : 2019/4/13 
# @Author  : licg
# @Email   : licgbeyond@foxmail.com
from django.urls import path

from apps.scrap.views import ScrapListView

app_name = 'scrap'

urlpatterns = [
    path('list/', ScrapListView.as_view(), name='scrap_list'),
]