# -*- coding: utf-8 -*-
# @DATE    : 2019/4/4
# @Author  : licg
# @Email   : licgbeyond@foxmail.com
import xadmin

from .models import Scrap


class ScrapAdmin(object):
    list_display = ['name', 'price', 'delete', 'time']
    search_fields = ['name', 'delete', 'time']


xadmin.site.register(Scrap, ScrapAdmin)