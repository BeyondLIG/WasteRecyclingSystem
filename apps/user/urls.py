# -*- coding: utf-8 -*-
# @DATE    : 2019/3/31 
# @Author  : licg
# @Email   : licgbeyond@foxmail.com
from django.urls import path

from user.views import *

app_name = 'user'

urlpatterns = [
    # 注册
    path('register/', RegisterView.as_view(), name='register'),

    # 登录
    path('login/', UserLoginView.as_view(), name='login'),

    # 个人信息
    path('info/', UserProfileView.as_view(), name='info'),

    # 修改信息
    # path('<int:user_id>/modify/', UserProfileModifyView.as_view(), name='UserProfileModify'),

    # 发送手机验证码（修改手机号）
    path('send_phone_code/', SendPhoneVerifyCode.as_view(), name='send_phone_code'),

    # 发送手机验证码（修改支付宝）
    path('send_account_code/', SendAccountVerifyCode.as_view(), name='send_account_code'),

    # 修改手机号
    path('update_phone/', UpdatePhone.as_view(), name='update_phone'),

    # 修改支付宝账号
    path('update_account/', UpdateAccount.as_view(), name='update_account'),

    # 修改密码
    path('update/pwd/', UpdatePwdView.as_view(), name='update_pwd'),

    # 用户退出
    path('logout/', LogoutView.as_view(), name='logout'),

]