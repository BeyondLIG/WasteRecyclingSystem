# -*- coding: utf-8 -*-
# @DATE    : 2019/4/1 
# @Author  : licg
# @Email   : licgbeyond@foxmail.com


# 自定义异常
class UserNameRepeatException(Exception):
    code = 600
    msg = '用户名重复'


class LoginProfileException(Exception):
    code = 601
    msg = '用户名或密码错误'


class PhoneVerifyCodeException(Exception):
    code = 602
    msg = '验证码错误'