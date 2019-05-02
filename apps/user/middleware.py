# -*- coding: utf-8 -*-
# @DATE    : 2019/4/4 
# @Author  : licg
# @Email   : licgbeyond@foxmail.com

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class ExceptionProcessMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        ret_json = {
            'code': getattr(exception, 'code', 0),
            'msg': getattr(exception, 'msg', 'error'),
            'data': None
        }
        return JsonResponse(ret_json)