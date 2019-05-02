
from django.db import models

# Create your models here.


# 订单
class Order(models.Model):
    order_number = models.CharField(max_length=100, null=False, blank=False, verbose_name='订单号')
    waiter_phone = models.CharField(max_length=11, null=False, blank=False, verbose_name='回收人员手机号')
    customer_phone = models.CharField(max_length=11, null=False, blank=False, verbose_name='社区用户手机号')
    customer_address = models.CharField(max_length=200, null=False, blank=False, verbose_name='社区人员地址')
    total_money = models.FloatField(null=False, blank=False, verbose_name='总金额')
    commodities_desc = models.TextField(verbose_name='废品描述')
    status = models.IntegerField(choices=((1, '处理中'), (2, '已支付')), default=1, verbose_name='订单状态')
    create_time = models.DateTimeField(verbose_name='下单时间', auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_number

    def __init__(self, order_number, customer_phone, customer_address, customer_name, waiter_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order_number = order_number
        self.customer_phone = customer_phone
        self.customer_address = customer_address
        self.customer_name = customer_name
        self.waiter_phone = waiter_phone
        self.total_money = 0.0


class SMSMsg(models.Model):
    scrap_user_phone = models.CharField(max_length=11, verbose_name='回收人员手机号')
    sent_time = models.DateTimeField(verbose_name='短信发送时间', auto_now_add=True)

    class Meta:
        verbose_name = '短信发送历史记录'
        verbose_name_plural = verbose_name

    def __init__(self, scrap_user_name, scrap_user_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scrap_user_name = scrap_user_name
        self.scrap_user_phone = scrap_user_phone


class PayMsg(models.Model):
    customer = models.CharField(max_length=11, verbose_name='顾客')
    money = models.FloatField(verbose_name='转账金额')
    time = models.DateTimeField(verbose_name='转账时间', auto_now_add=True)

    class Meta:
        verbose_name = '转账历史记录'
        verbose_name_plural = verbose_name

    def __init__(self, customer, money, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customer = customer
        self.money = money



