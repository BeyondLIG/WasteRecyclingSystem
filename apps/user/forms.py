# -*- coding: utf-8 -*-
# @DATE    : 2019/3/31 
# @Author  : licg
# @Email   : licgbeyond@foxmail.com
import re

from django import forms


# 注册表单
from apps.user.models import UserProfile


class RegisterForm(forms.Form):
    phone = forms.CharField(required=True, max_length=11, min_length=11)
    password = forms.CharField(required=True, min_length=6)
    role = forms.IntegerField(required=True)
    code = forms.CharField(max_length=6, min_length=6, required=True)


# 修改信息表单
class ProfileModifyForm(forms.Form):
    phone = forms.CharField(required=True, max_length=11, min_length=11)
    address = forms.CharField(required=True)


# 登录表单
class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class PhoneVerifyCodeForm(forms.Form):
    phone = forms.CharField(required=True, max_length=11, min_length=11)

    # 手机号的正则表达式验证
    def clean_phone(self):
        mobile = self.cleaned_data['phone']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")


# 密码验证表单
class ModifyForm(forms.Form):
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)


class UserInfoForm(forms.Form):
    phone = forms.CharField(required=True)
    address = forms.CharField(required=True)
    gender = forms.CharField(required=True)
    account = forms.CharField(required=True)