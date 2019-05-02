# -*- coding: utf-8 -*-
# @DATE    : 2019/4/4
# @Author  : licg
# @Email   : licgbeyond@foxmail.com
import xadmin

from .models import Order, SMSMsg, PayMsg


class OrderAdmin(object):
    list_display = ['order_number', 'waiter_phone', 'customer_phone',  'customer_address', 'total_money', 'commodities_desc', 'status', 'create_time']
    search_fields = ['order_number', 'waiter_phone', 'customer_phone', 'create_time']

    def has_add_permission(self):
        return False

    def has_change_permission(self):
        return False

    def has_delete_permission(self):
        return False

    # def has_add_permission(self):
    #     """ 取消后台添加附件功能 """
    #     # 社区用户才拥有添加订单的功能
    #     if self.user.role == 0:
    #         return True
    #     return False
    #
    # def queryset(self):
    #     qs = super(OrderAdmin, self).queryset()
    #     if self.user.role == 0:
    #         return qs.filter(customer_name=self.user)
    #     else:
    #         return qs.filter(waiter_name=self.user)


class SMSMsgAdmin(object):
    list_display = ['scrap_user_phone', 'sent_time']
    search_fields = ['scrap_user_phone', 'sent_time']


class PayMsgAdmin(object):
    list_display = ['customer', 'money', 'time']
    search_fields = ['customer', 'money', 'time']


xadmin.site.register(Order, OrderAdmin)
xadmin.site.register(SMSMsg, SMSMsgAdmin)
xadmin.site.register(PayMsg, PayMsgAdmin)