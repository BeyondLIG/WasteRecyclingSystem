# -*- coding: utf-8 -*-
# @DATE    : 2019/4/3 
# @Author  : licg
# @Email   : licgbeyond@foxmail.com
import os
import re
from datetime import datetime

from alipay import AliPay

dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app_private_key_string = open(dir_name + "\\app_private_key.txt").read()
alipay_public_key_string = open(dir_name + "\\app_public_key.txt").read()

alipay = AliPay(
    appid="",
    app_notify_url=None,  # 默认回调url
    app_private_key_string=app_private_key_string,
    # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2",   # RSA 或者 RSA2
    debug=True         # 默认False
)


def alipay_transfer(amount, account):
    result = alipay.api_alipay_fund_trans_toaccount_transfer(
        datetime.now().strftime("%Y%m%d%H%M%S"),
        payee_type="ALIPAY_LOGONID",
        payee_account=account,
        amount=amount
    )
    return result


if __name__ == '__main__':
    print(alipay_transfer(1000, ""))

