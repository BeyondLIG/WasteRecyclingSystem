# -*- coding: utf-8 -*-
# @DATE    : 2019/4/1 
# @Author  : licg
# @Email   : licgbeyond@foxmail.com


class ScrapBusyException(Exception):
    code = 700
    msg = '当前无空闲的回收人员'
    data = None