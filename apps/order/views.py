from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

import json

from django.views.generic.base import View
from order.utils import generate_order_number
from apps.order.models import Order, SMSMsg, PayMsg
from apps.scrap.models import Scrap
from pure_pagination import Paginator, PageNotAnInteger


from apps.user.models import UserProfile
from aliyun.my_alipay.pay import alipay_transfer
from aliyun.my_sms.send_sms import send_sms_notify


# 用户下单
from utils.mixin_utils import LoginRequiredMixin


class OrderCreateView(LoginRequiredMixin, View):
    @transaction.atomic
    def post(self, request):
        if request.user.role == 0:
            # 获取空闲的回收人员
            scrap_users = UserProfile.objects.filter(role=1, deleted=0, work_status=0)
            if scrap_users:
                scrap_user = scrap_users[0]
                # 修改回收人员的状态
                scrap_user.work_status = 1
                scrap_user.save()

                # 创建订单
                order = Order(generate_order_number(), request.user.phone, request.user.address, request.user.username,
                              scrap_user.phone)
                order.save()

                # 给废品回收人员发送订单通知
                send_sms_notify(scrap_user.phone, order.order_number)
                # 保存短信发送记录
                SMSMsg(scrap_user.username, scrap_user.phone).save()
                return JsonResponse({'status': 'success', 'msg': '下单成功'})
            else:
                return JsonResponse({'status': 'failure', 'msg': '回收人员繁忙，请稍后再试'})
        else:
            return JsonResponse({'status': 'failure', 'msg': '你没有该操作的权限'})


# 订单信息完善
# @transaction.atomic
class OrderEditView(LoginRequiredMixin, View):
    @transaction.atomic
    def post(self, request):
        # 支付并修改订单的状态
        order_number = request.POST.get('order_number')
        order = Order.objects.get(order_number=order_number)
        # 幂等操作
        if order.status != 1:
            return render(request, 'order-list.html', {})

        total_money = 0.0
        commodities = json.loads(request.POST.get('commodities'))
        desc = ''
        for commodity in commodities:
            scrap_name = commodity.get('scrap_name')
            weight = float(commodity.get('weight'))
            scrap = Scrap.objects.get(name=scrap_name)
            scrap_money = weight * scrap.price
            total_money += scrap_money
            desc += "{'商品名: {scrap_name}, '重量': {weight}, '单价': {price}}, ".format(scrap_name=scrap_name, weight=weight, price=scrap.price)

        commodities_desc = '[{0}]'.format(desc)
        order.commodities_desc = commodities_desc
        order.total_money = total_money
        # 修改订单状态
        order.status = 2
        order.save()

        # 转账
        alipay_transfer(total_money, request.user.account)

        # 保存转账记录
        PayMsg(order.customer_phone, total_money).save()

        # 修改回收人员的状态
        UserProfile.objects.filter(role=1, id=order.waiter_id).update(work_status=0)
        return render(request, 'order-list.html', {})


# 提交订单
class OrderSubmitView(LoginRequiredMixin, View):
    def get(self, request, order_num):
        return render(request, 'order-edit.html', {'order_num': order_num})


# 订单列表
class OrderListView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.role == 1:
            # 回收人员订单列表
            orders = Order.objects.filter(waiter_phone=request.user.username)
        else:
            # 社区用户订单列表
            orders = Order.objects.filter(customer_phone=request.user.username)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 分页
        p = Paginator(orders, 5, request=request)
        orders = p.page(page)
        return render(request, 'order-list.html', {'orders': orders})


