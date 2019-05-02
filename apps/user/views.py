import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.
from django.urls import reverse

from django.views.generic.base import View
from user.forms import *
from apps.user.models import UserProfile, VerifyCode, Banner
from aliyun.my_sms.send_sms import send_sms_verify_code
from user.exception import *
from utils.mixin_utils import LoginRequiredMixin


class IndexView(View):
    """
    首页
    """
    def get(self, request):
        # 轮播图
        banners = Banner.objects.all().order_by('index')
        return render(request, 'index.html', {
            'banners': banners
        })


class RegisterView(View):
    """
    用户注册
    """
    # 返回注册页面
    def get(self, request):
        # 添加验证码
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        # 表单验证
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            phone = request.POST.get('phone')

            if UserProfile.objects.filter(username=phone):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '用户已存在'})
            password = request.POST.get('password')
            role = request.POST.get('role')
            code = request.POST.get('code')

            if VerifyCode.objects.get(phone_account=phone, code=code) is None:
                return render(request, 'register.html', {'register_form': register_form, 'msg': '验证码错误'})
            # 保存用户
            user = UserProfile()
            user.username = phone
            user.phone = phone
            user.role = role
            # 密码加密
            user.password = make_password(password)
            user.is_active = True
            user.save()
            # 返回登录页面
            return render(request, 'login.html')

        else:
            return render(request, 'register.html', {'register_form': register_form})


class UserLoginView(View):
    """
    用户登录
    """
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username').strip()
            password = request.POST.get('password').strip()

            # django自带用户验证
            user = authenticate(username=username, password=password)

            if user and user.is_active:
                login(request, user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


# 查看个人信息
class UserProfileView(LoginRequiredMixin, View):
    """
    个人中心 - 个人信息
    """
    def get(self, request):
        return render(request, 'user-info.html', {})

    def post(self, request):
        userinfo_form = UserInfoForm(request.POST)
        if userinfo_form.is_valid():
            request.user.username = request.POST.get('phone')
            request.user.phone = request.POST.get('phone')
            request.user.account = request.POST.get('account')
            request.user.address = request.POST.get('address')
            request.user.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'failure', 'msg': userinfo_form.errors})


class SendPhoneVerifyCode(View):
    """
    个人中心 - 发送手机验证码（修改手机号）
    """
    def post(self, request):
        phone_verify_code_form = PhoneVerifyCodeForm(request.POST)
        if phone_verify_code_form.is_valid():
            phone = request.POST.get('phone')
            code = ''.join(str(random.choice(range(10))) for _ in range(6))
            # 保存验证码
            VerifyCode(code, phone).save()

            # 发送手机验证码
            send_sms_verify_code(phone, code)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'failure'})


class SendAccountVerifyCode(LoginRequiredMixin, View):
    """"
    个人中心 - 发送手机验证码（修改支付宝账号）
    """
    def post(self, request):
        if request.user.phone:
            code = ''.join(str(random.choice(range(10))) for _ in range(6))
            # 保存验证码
            VerifyCode(code, request.user.account).save()

            # 发送手机验证码
            send_sms_verify_code(request.user.phone, code)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'failure'})


class UpdatePhone(LoginRequiredMixin, View):
    """
    个人中心 - 修改手机号
    """
    def post(self, request):
        phone = request.POST.get('phone', '')
        code = request.POST.get('code', '')
        if VerifyCode.objects.filter(phone_account=phone, code=code):
            request.user.phone = phone
            request.user.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'email': '验证码出错'})


class UpdateAccount(LoginRequiredMixin, View):
    """
    个人中心 - 修改账号
    """
    def post(self, request):
        account = request.POST.get('account', '')
        code = request.POST.get('code', '')
        if VerifyCode.objects.filter(phone_account=account, code=code):
            request.user.account = account
            request.user.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'failure'})


class UpdatePwdView(LoginRequiredMixin, View):
    """
    个人中心 - 修改密码
    """
    def post(self, request):
        modify_form = ModifyForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            if pwd1 != pwd2:
                return HttpResponse("{'status': 'fail', 'msg': '密码不一致'}", content_type='application/json')
            user = request.user
            user.password = make_password(pwd2)
            user.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse(modify_form.errors)


class LogoutView(LoginRequiredMixin, View):
    """
    用户退出
    """
    def get(self, request):
        logout(request)
        # django重定向
        return HttpResponseRedirect(reverse('index'))


def page_not_found(request, **kwargs):
    """
    配置404页面函数
    """
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


# def page_error(request):
#     """
#     配置500页面函数
#     """
#     response = render_to_response('500.html', {})
#     response.status_code = 500
#     return response