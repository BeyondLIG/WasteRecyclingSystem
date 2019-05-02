# -*- coding: utf-8 -*-
# @DATE    : 2019/4/1 
# @Author  : licg
# @Email   : licgbeyond@foxmail.com


import uuid


# 生成订单号
def generate_order_number():
    return str(uuid.uuid1())


if __name__ == '__main__':
    print(generate_order_number())