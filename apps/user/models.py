from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserProfile(AbstractUser):
    gender = models.CharField(choices=(('male', '男'), ('female', "女")), default='male', max_length=10, verbose_name='性别')
    phone = models.CharField(max_length=11, null=False, blank=False, verbose_name='手机号码')
    address = models.CharField(max_length=200, verbose_name='住址')
    role = models.IntegerField(choices=((0, '社区用户'), (1, '废品回收人员')), default=0, verbose_name='角色')
    account = models.CharField(max_length=50, verbose_name='支付宝账号')
    deleted = models.IntegerField(choices=((0, '未注销'), (1, '已注销')), default=0, verbose_name='是否注销')
    work_status = models.IntegerField(choices=((0, '空闲'), (1, '忙碌')), default=0, verbose_name='工作状态')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    code = models.CharField(max_length=6, null=False, blank=False, verbose_name='手机验证码')
    phone_account = models.CharField(max_length=50, null=False, blank=False, verbose_name='手机号')
    send_time = models.DateTimeField(verbose_name='发送时间', auto_now_add=True)

    def __init__(self, code, phone_account, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.code = code
        self.phone_account = phone_account


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='轮播图')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name




