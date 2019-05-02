# -*- coding: utf-8 -*-
# @DATE    : 2019/4/18 
# @Author  : licg
# @Email   : licgbeyond@foxmail.com

from django.urls import path

from apps.order.views import OrderListView, OrderEditView, OrderSubmitView, OrderCreateView

app_name = 'order'

urlpatterns = [
    path('list/', OrderListView.as_view(), name='order_list'),

    # 完善订单信息
    path('edit/', OrderEditView.as_view(), name='order_edit'),

    # 提交订单
    path('submit/<order_num>', OrderSubmitView.as_view(), name='order_submit'),

    # 用户下单
    path('create/', OrderCreateView.as_view(), name='order_create'),
]